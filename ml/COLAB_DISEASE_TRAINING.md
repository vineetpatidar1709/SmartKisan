# Colab Disease Training

Use these cells in Google Colab to train the disease classifier with the same script used by this project.

## 1. Install dependencies

```python
!pip install -q torch torchvision scikit-learn pillow
```

## 2. Mount Google Drive

```python
from google.colab import drive
drive.mount("/content/drive")
```

## 3. Copy the project into Colab

This assumes the project folder is already in Google Drive.

```python
PROJECT_DIR = "/content/drive/MyDrive/smart_agriculture_ai"
WORK_DIR = "/content/smart_agriculture_ai"
!rm -rf "$WORK_DIR"
!cp -r "$PROJECT_DIR" "$WORK_DIR"
%cd /content/smart_agriculture_ai
```

## 4. Train a crop-specific model

This is the recommended option because each crop has its own disease classes.

```python
DATA_ZIP = "/content/drive/MyDrive/disease_images_trainready_best.zip"
OUT_DIR = "/content/drive/MyDrive/disease_model_outputs"

!python ml/train_disease_classifier.py \
  --dataset-zip "$DATA_ZIP" \
  --extract-dir "/content/datasets" \
  --data-dir "/content/datasets/disease_images_trainready_best" \
  --crop tomato \
  --profile best \
  --epochs 20 \
  --num-workers 2 \
  --out-dir "$OUT_DIR" \
  --package-output
```

## 5. Train one model for all crops

Use this only if you want a combined classifier with labels like `tomato__late_blight`.

```python
DATA_ZIP = "/content/drive/MyDrive/disease_images_trainready_best.zip"
OUT_DIR = "/content/drive/MyDrive/disease_model_outputs_all"

!python ml/train_disease_classifier.py \
  --dataset-zip "$DATA_ZIP" \
  --extract-dir "/content/datasets" \
  --data-dir "/content/datasets/disease_images_trainready_best" \
  --profile best \
  --epochs 20 \
  --num-workers 2 \
  --out-dir "$OUT_DIR" \
  --package-output
```

## 6. Download the output bundle

For a crop-specific run, the bundle name includes the crop.

```python
from google.colab import files

files.download("/content/drive/MyDrive/disease_model_outputs/disease_bundle_tomato.zip")
```

## Output files

The trainer saves:

- `disease_classifier_<crop>.pt`: model weights
- `disease_labels_<crop>.json`: class labels
- `disease_meta_<crop>.json`: training metadata
- `disease_history_<crop>.json`: per-epoch metrics
- `disease_bundle_<crop>.zip`: packaged download bundle when `--package-output` is used

If you train all crops together, the filenames are the same without the crop suffix.
