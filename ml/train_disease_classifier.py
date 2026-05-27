import argparse
import json
import random
import zipfile
from pathlib import Path
from typing import List, Optional

import torch
from sklearn.model_selection import train_test_split
from torch import nn
from torch.utils.data import DataLoader, Dataset, WeightedRandomSampler
from torchvision import models, transforms
from torchvision.datasets.folder import default_loader


IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".webp"}


def set_seed(seed: int):
    random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def build_transforms(image_size: int):
    train_tf = transforms.Compose([
        transforms.RandomResizedCrop(image_size, scale=(0.8, 1.0)),
        transforms.RandomHorizontalFlip(),
        transforms.RandomVerticalFlip(),
        transforms.RandomRotation(20),
        transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2),
        transforms.RandomApply([transforms.GaussianBlur(kernel_size=3)], p=0.2),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
        transforms.RandomErasing(p=0.25),
    ])
    val_tf = transforms.Compose([
        transforms.Resize((image_size, image_size)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
    ])
    return train_tf, val_tf


def build_model(model_name: str, num_classes: int, pretrained: bool):
    model_name = model_name.lower()
    if model_name == "efficientnet_b0":
        weights = None if not pretrained else models.EfficientNet_B0_Weights.DEFAULT
        model = models.efficientnet_b0(weights=weights)
    elif model_name == "efficientnet_b3":
        weights = None if not pretrained else models.EfficientNet_B3_Weights.DEFAULT
        model = models.efficientnet_b3(weights=weights)
    else:
        raise SystemExit(f"Unsupported model: {model_name}")
    model.classifier[1] = nn.Linear(model.classifier[1].in_features, num_classes)
    return model


def normalize_crop_name(value: Optional[str]) -> Optional[str]:
    if not value:
        return None
    return value.strip().lower().replace(" ", "_").replace("-", "_")


def iter_image_files(folder: Path):
    for path in sorted(folder.rglob("*")):
        if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS:
            yield path


def discover_class_dirs(root: Path, crop: Optional[str]):
    first_level_dirs = sorted([path for path in root.iterdir() if path.is_dir()])
    if not first_level_dirs:
        raise SystemExit(f"No class folders found under {root}")

    if crop:
        crop_dir = root / crop
        if not crop_dir.exists():
            available = ", ".join(path.name for path in first_level_dirs)
            raise SystemExit(
                f"Crop '{crop}' not found under {root}. Available crops: {available}"
            )
        class_dirs = [(path.name, path) for path in sorted(crop_dir.iterdir()) if path.is_dir()]
        if not class_dirs:
            raise SystemExit(f"No disease folders found under {crop_dir}")
        return class_dirs

    nested_dirs = []
    flat_dirs = []
    for directory in first_level_dirs:
        child_dirs = sorted([path for path in directory.iterdir() if path.is_dir()])
        if child_dirs:
            nested_dirs.append(directory)
        else:
            flat_dirs.append(directory)

    if nested_dirs and flat_dirs:
        raise SystemExit(
            f"Mixed flat and nested class folders under {root}. "
            "Use a consistent layout or pass --crop for crop-specific training."
        )

    if nested_dirs:
        return [
            (f"{crop_dir.name}__{disease_dir.name}", disease_dir)
            for crop_dir in nested_dirs
            for disease_dir in sorted(crop_dir.iterdir())
            if disease_dir.is_dir()
        ]

    return [(path.name, path) for path in flat_dirs]


class DiseaseImageDataset(Dataset):
    def __init__(self, root: Path, transform=None, crop: Optional[str] = None):
        self.root = Path(root)
        self.transform = transform
        self.crop = normalize_crop_name(crop)

        class_dirs = discover_class_dirs(self.root, self.crop)
        self.classes = []
        self.class_to_idx = {}
        self.samples = []
        self.targets = []

        for class_name, class_dir in class_dirs:
            image_paths = list(iter_image_files(class_dir))
            if not image_paths:
                continue
            class_index = len(self.classes)
            self.classes.append(class_name)
            self.class_to_idx[class_name] = class_index
            self.samples.extend((path, class_index) for path in image_paths)
            self.targets.extend([class_index] * len(image_paths))

        if not self.samples:
            raise SystemExit(f"No images found under {self.root}")

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, index: int):
        image_path, target = self.samples[index]
        image = default_loader(str(image_path))
        if self.transform is not None:
            image = self.transform(image)
        return image, target


class TransformSubset(Dataset):
    def __init__(self, dataset: DiseaseImageDataset, indices: List[int], transform):
        self.dataset = dataset
        self.indices = list(indices)
        self.transform = transform
        self.classes = dataset.classes
        self.class_to_idx = dataset.class_to_idx
        self.targets = [dataset.targets[index] for index in self.indices]

    def __len__(self):
        return len(self.indices)

    def __getitem__(self, index: int):
        image, target = self.dataset[self.indices[index]]
        if self.transform is not None:
            image = self.transform(image)
        return image, target


def describe_dataset(name: str, dataset):
    counts = torch.bincount(torch.tensor(dataset.targets), minlength=len(dataset.classes))
    print(f"{name}: {len(dataset)} images across {len(dataset.classes)} classes")
    for class_name, count in zip(dataset.classes, counts.tolist()):
        print(f"  - {class_name}: {count}")


def is_split_dataset_root(path: Path) -> bool:
    if not path.exists() or not path.is_dir():
        return False
    return (path / "train").is_dir() and (path / "val").is_dir()


def resolve_extracted_data_dir(extract_dir: Path, requested_data_dir: Path, dataset_zip: Path) -> Path:
    if requested_data_dir.exists():
        return requested_data_dir

    candidates = []
    if is_split_dataset_root(extract_dir):
        candidates.append(extract_dir)

    for child in sorted(extract_dir.iterdir()):
        if child.is_dir() and is_split_dataset_root(child):
            candidates.append(child)

    if not candidates:
        raise SystemExit(
            f"Could not find an extracted dataset under {extract_dir}. "
            f"Pass --data-dir to the extracted dataset root."
        )

    if len(candidates) == 1:
        return candidates[0]

    preferred_names = {requested_data_dir.name.lower(), dataset_zip.stem.lower()}
    for candidate in candidates:
        if candidate.name.lower() in preferred_names:
            return candidate

    candidate_names = ", ".join(candidate.name for candidate in candidates)
    raise SystemExit(
        "Multiple extracted dataset roots were found: "
        f"{candidate_names}. Pass --data-dir to choose the correct one."
    )


def prepare_data_dir(data_dir: Path, dataset_zip: Optional[Path], extract_dir: Optional[Path]) -> Path:
    if dataset_zip is None:
        if not data_dir.exists():
            raise SystemExit(f"Data directory not found: {data_dir}")
        return data_dir

    if not dataset_zip.exists():
        raise SystemExit(f"Dataset zip not found: {dataset_zip}")

    target_extract_dir = extract_dir or data_dir.parent
    target_extract_dir.mkdir(parents=True, exist_ok=True)
    print(f"Extracting dataset zip: {dataset_zip}")
    print(f"Extraction directory: {target_extract_dir}")
    with zipfile.ZipFile(dataset_zip, "r") as archive:
        archive.extractall(target_extract_dir)

    resolved_data_dir = resolve_extracted_data_dir(target_extract_dir, data_dir, dataset_zip)
    print(f"Using dataset directory: {resolved_data_dir}")
    return resolved_data_dir


def build_datasets(data_dir: Path, train_tf, val_tf, crop: Optional[str], val_split: float, seed: int):
    train_dir = data_dir / "train"
    val_dir = data_dir / "val"
    test_dir = data_dir / "test"

    if train_dir.exists() and val_dir.exists():
        train_ds = DiseaseImageDataset(train_dir, transform=train_tf, crop=crop)
        val_ds = DiseaseImageDataset(val_dir, transform=val_tf, crop=crop)
        test_ds = DiseaseImageDataset(test_dir, transform=val_tf, crop=crop) if test_dir.exists() else None
        return train_ds, val_ds, test_ds

    base_ds = DiseaseImageDataset(data_dir, transform=None, crop=crop)
    indices = list(range(len(base_ds)))
    try:
        train_indices, val_indices = train_test_split(
            indices,
            test_size=val_split,
            random_state=seed,
            stratify=base_ds.targets,
        )
    except ValueError as exc:
        print(f"Stratified split unavailable ({exc}). Falling back to random split.")
        train_indices, val_indices = train_test_split(
            indices,
            test_size=val_split,
            random_state=seed,
            shuffle=True,
        )

    train_ds = TransformSubset(base_ds, train_indices, train_tf)
    val_ds = TransformSubset(base_ds, val_indices, val_tf)
    return train_ds, val_ds, None


def build_loader(dataset, batch_size: int, num_workers: int, shuffle: bool, sampler=None, pin_memory: bool = False):
    loader_kwargs = {
        "batch_size": batch_size,
        "shuffle": shuffle if sampler is None else False,
        "sampler": sampler,
        "num_workers": num_workers,
        "pin_memory": pin_memory,
    }
    if num_workers > 0:
        loader_kwargs["persistent_workers"] = True
    return DataLoader(dataset, **loader_kwargs)


def evaluate(model, loader, criterion, device, use_amp: bool):
    model.eval()
    total_loss = 0.0
    total_correct = 0
    total_samples = 0

    with torch.no_grad():
        for images, labels in loader:
            images = images.to(device, non_blocking=True)
            labels = labels.to(device, non_blocking=True)
            with torch.cuda.amp.autocast(enabled=use_amp):
                outputs = model(images)
                loss = criterion(outputs, labels)
            total_loss += loss.item() * labels.size(0)
            total_correct += (outputs.argmax(dim=1) == labels).sum().item()
            total_samples += labels.size(0)

    avg_loss = total_loss / max(1, total_samples)
    accuracy = 100.0 * total_correct / max(1, total_samples)
    return avg_loss, accuracy


def package_outputs(bundle_path: Path, files: List[Path]):
    with zipfile.ZipFile(bundle_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for file_path in files:
            archive.write(file_path, arcname=file_path.name)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=str, default="data/disease_images")
    parser.add_argument("--dataset-zip", type=str, default=None,
                        help="Optional zip archive containing the disease image dataset. Helpful in Colab.")
    parser.add_argument("--extract-dir", type=str, default=None,
                        help="Where to extract --dataset-zip. Defaults to the parent of --data-dir.")
    parser.add_argument("--crop", type=str, default=None,
                        help="Train only one crop's disease classes, e.g. tomato or wheat.")
    parser.add_argument("--image-size", type=int, default=224)
    parser.add_argument("--batch-size", type=int, default=32)
    parser.add_argument("--epochs", type=int, default=12)
    parser.add_argument("--lr", type=float, default=1e-3)
    parser.add_argument("--weight-decay", type=float, default=1e-4)
    parser.add_argument("--val-split", type=float, default=0.2)
    parser.add_argument("--out-dir", type=str, default="ml/models")
    parser.add_argument("--no-pretrained", action="store_true")
    parser.add_argument("--num-workers", type=int, default=0)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--model", type=str, default="efficientnet_b0",
                        choices=["efficientnet_b0", "efficientnet_b3"])
    parser.add_argument("--profile", type=str, default="standard",
                        choices=["standard", "best"])
    parser.add_argument("--no-balanced-sampling", action="store_true")
    parser.add_argument("--patience", type=int, default=5)
    parser.add_argument("--package-output", action="store_true",
                        help="Zip the saved model artifacts into one bundle for easier download from Colab.")
    args = parser.parse_args()

    if args.profile == "best":
        args.model = "efficientnet_b3"
        args.image_size = 300
        args.batch_size = 16
        args.epochs = max(args.epochs, 20)
        args.lr = 3e-4

    args.crop = normalize_crop_name(args.crop)
    data_dir = prepare_data_dir(
        data_dir=Path(args.data_dir),
        dataset_zip=Path(args.dataset_zip) if args.dataset_zip else None,
        extract_dir=Path(args.extract_dir) if args.extract_dir else None,
    )
    set_seed(args.seed)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    use_amp = device.type == "cuda"
    if device.type == "cuda" and hasattr(torch.backends, "cudnn"):
        torch.backends.cudnn.benchmark = True
    if hasattr(torch, "set_float32_matmul_precision"):
        torch.set_float32_matmul_precision("high")

    print(f"Device: {device}")
    if args.crop:
        print(f"Training crop-specific model for: {args.crop}")

    train_tf, val_tf = build_transforms(args.image_size)
    train_ds, val_ds, test_ds = build_datasets(
        data_dir=data_dir,
        train_tf=train_tf,
        val_tf=val_tf,
        crop=args.crop,
        val_split=args.val_split,
        seed=args.seed,
    )

    if train_ds.classes != val_ds.classes:
        raise SystemExit("Train and validation class lists do not match.")
    if test_ds is not None and train_ds.classes != test_ds.classes:
        raise SystemExit("Train and test class lists do not match.")

    num_classes = len(train_ds.classes)
    if num_classes < 2:
        raise SystemExit("Need at least 2 classes to train a classifier.")

    describe_dataset("Train", train_ds)
    describe_dataset("Validation", val_ds)
    if test_ds is not None:
        describe_dataset("Test", test_ds)

    sampler = None
    if not args.no_balanced_sampling:
        targets = torch.tensor(train_ds.targets)
        class_counts = torch.bincount(targets, minlength=num_classes).float()
        class_weights = 1.0 / torch.clamp(class_counts, min=1.0)
        sample_weights = class_weights[targets]
        sampler = WeightedRandomSampler(sample_weights, num_samples=len(sample_weights), replacement=True)

    pin_memory = device.type == "cuda"
    train_loader = build_loader(
        train_ds,
        batch_size=args.batch_size,
        num_workers=args.num_workers,
        shuffle=True,
        sampler=sampler,
        pin_memory=pin_memory,
    )
    val_loader = build_loader(
        val_ds,
        batch_size=args.batch_size,
        num_workers=args.num_workers,
        shuffle=False,
        pin_memory=pin_memory,
    )
    test_loader = None
    if test_ds is not None:
        test_loader = build_loader(
            test_ds,
            batch_size=args.batch_size,
            num_workers=args.num_workers,
            shuffle=False,
            pin_memory=pin_memory,
        )

    model = build_model(args.model, num_classes, pretrained=not args.no_pretrained).to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs)
    scaler = torch.cuda.amp.GradScaler(enabled=use_amp)

    best_acc = 0.0
    best_state = None
    patience_left = args.patience
    history = []

    for epoch in range(args.epochs):
        model.train()
        running_loss = 0.0
        samples_seen = 0

        for images, labels in train_loader:
            images = images.to(device, non_blocking=True)
            labels = labels.to(device, non_blocking=True)
            optimizer.zero_grad(set_to_none=True)

            with torch.cuda.amp.autocast(enabled=use_amp):
                outputs = model(images)
                loss = criterion(outputs, labels)

            scaler.scale(loss).backward()
            scaler.step(optimizer)
            scaler.update()

            running_loss += loss.item() * labels.size(0)
            samples_seen += labels.size(0)

        train_loss = running_loss / max(1, samples_seen)
        val_loss, val_acc = evaluate(model, val_loader, criterion, device, use_amp)
        scheduler.step()
        history.append(
            {
                "epoch": epoch + 1,
                "train_loss": train_loss,
                "val_loss": val_loss,
                "val_acc": val_acc,
                "lr": optimizer.param_groups[0]["lr"],
            }
        )

        print(
            f"Epoch {epoch + 1}/{args.epochs} - "
            f"Train Loss: {train_loss:.4f} - "
            f"Val Loss: {val_loss:.4f} - "
            f"Val Acc: {val_acc:.2f}%"
        )

        if val_acc > best_acc:
            best_acc = val_acc
            best_state = {key: value.cpu() for key, value in model.state_dict().items()}
            patience_left = args.patience
        else:
            patience_left -= 1
            if patience_left <= 0:
                print("Early stopping triggered.")
                break

    if best_state is None:
        best_state = {key: value.cpu() for key, value in model.state_dict().items()}

    model.load_state_dict(best_state)
    test_acc = None
    if test_loader is not None:
        test_loss, test_acc = evaluate(model, test_loader, criterion, device, use_amp)
        print(f"Test Loss: {test_loss:.4f} - Test Acc: {test_acc:.2f}%")

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    suffix = f"_{args.crop}" if args.crop else ""
    model_path = out_dir / f"disease_classifier{suffix}.pt"
    labels_path = out_dir / f"disease_labels{suffix}.json"
    meta_path = out_dir / f"disease_meta{suffix}.json"
    history_path = out_dir / f"disease_history{suffix}.json"

    torch.save(best_state, model_path)
    labels_path.write_text(json.dumps(train_ds.classes, indent=2), encoding="utf-8")
    meta_path.write_text(
        json.dumps(
            {
                "crop": args.crop,
                "classes": train_ds.classes,
                "num_classes": num_classes,
                "model": args.model,
                "image_size": args.image_size,
                "epochs": args.epochs,
                "lr": args.lr,
                "weight_decay": args.weight_decay,
                "balanced_sampling": not args.no_balanced_sampling,
                "best_val_acc": best_acc,
                "test_acc": test_acc,
                "dataset_dir": str(data_dir),
                "history_file": history_path.name,
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    history_path.write_text(json.dumps(history, indent=2), encoding="utf-8")
    print(f"Saved model to {model_path}")
    print(f"Saved labels to {labels_path}")
    print(f"Saved metadata to {meta_path}")
    print(f"Saved history to {history_path}")

    if args.package_output:
        bundle_path = out_dir / f"disease_bundle{suffix}.zip"
        package_outputs(bundle_path, [model_path, labels_path, meta_path, history_path])
        print(f"Saved output bundle to {bundle_path}")


if __name__ == "__main__":
    main()
