# data/crop_loader.py

import importlib
import pkgutil
from data.crop_schema import CropSchemaV2


def _normalize_name(crop_name: str) -> str:
    return crop_name.strip().lower().replace(" ", "_").replace("-", "_")


def _extract_payload(crop_module):
    # Support both historic uppercase and current lowercase conventions.
    raw = getattr(crop_module, "CROP_DATA", None)
    if raw is None:
        raw = getattr(crop_module, "crop_data", None)
    if not isinstance(raw, dict):
        return None

    # Current crop files are usually {"rice": {...}}; unwrap to the inner payload.
    if len(raw) == 1:
        only_value = next(iter(raw.values()))
        if isinstance(only_value, dict):
            return only_value
    return raw


# Define which fields belong to each mode
MODE_FIELDS = {
    "brief": [
        "name", "scientific_name", "family", "category", "crop_type",
        "season", "duration_days", "climate", "ideal_temperature",
        "water_requirement_level", "average_yield_per_acre"
    ],
    "detailed": [
        "name", "scientific_name", "family", "category", "crop_type",
        "season", "duration_days", "climate", "ideal_temperature", "germination_temperature",
        "rainfall_requirement_mm", "water_requirement_level", "sunlight_requirement",
        "soil_type", "soil_ph_range", "soil_depth_requirement", "salinity_tolerance", "drainage_requirement",
        "major_states",
        "land_preparation",
        "seed_information",
        "sowing_method", "row_spacing", "plant_spacing", "sowing_depth",
        "growth_stages",
        "irrigation_schedule",
        "fertilizer_management",
        "average_yield_per_acre"
    ],
    "expert": [
        "major_weeds",
        "major_pests",
        "major_diseases",
        "harvesting_details",
        "post_harvest",
        "nutrition_per_100g",
        "nutrition_explanation",
        "health_benefits",
        "economic_importance",
        "risk_factors",
        "images"
    ],
    "legacy": []
}


def _filter_by_mode(data: dict, mode: str) -> dict:
    """Filter crop data based on mode."""
    if mode == "legacy":
        return data
    allowed_fields = MODE_FIELDS.get(mode, [])
    if not allowed_fields:
        return data
    filtered = {}
    for key in allowed_fields:
        if key in data:
            filtered[key] = data[key]
    return filtered


def load_crop(crop_name: str, mode: str = "detailed") -> dict:
    """
    Loads crop data in requested mode.
    Modes:
        - brief: Basic info (name, season, duration, water, yield)
        - detailed: Cultivation details (soil, land prep, seed, irrigation, fertilizer)
        - expert: Pests, diseases, weeds, harvesting, risks
        - legacy: All data
    """
    try:
        module_path = f"data.crops.{_normalize_name(crop_name)}"
        crop_module = importlib.import_module(module_path)
    except ModuleNotFoundError:
        return {"error": "Crop not found"}

    # V2 format
    if CropSchemaV2.is_v2_format(crop_module):
        crop_data = crop_module.CROP_DATA
        if mode in crop_data:
            return crop_data[mode]
        return _filter_by_mode(crop_data.get("detailed", {}), mode)

    payload = _extract_payload(crop_module)
    if payload is None:
        return {"error": "Invalid crop structure"}

    # If payload is mode-keyed
    if isinstance(payload, dict) and mode in payload and isinstance(payload[mode], dict):
        return _filter_by_mode(payload[mode], mode)

    # Apply mode filtering
    return _filter_by_mode(payload, mode)


def load_all_crops() -> dict:
    """
    Loads all crop modules under data.crops and returns a name-keyed map.
    """
    crops = {}
    package = importlib.import_module("data.crops")
    for module_info in pkgutil.iter_modules(package.__path__):
        module = importlib.import_module(f"data.crops.{module_info.name}")
        payload = _extract_payload(module)
        if not isinstance(payload, dict):
            continue
        common_name = payload.get("name") or module_info.name.replace("_", " ").title()
        crops[common_name] = payload
    return crops
