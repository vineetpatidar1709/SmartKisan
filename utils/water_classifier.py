"""
Water Availability Classification Utility

This module provides functions to classify water availability into 5 categories:
- Very Low: 0-200 mm
- Low: 200-400 mm
- Medium: 400-600 mm
- High: 600-1000 mm
- Very High: >1000 mm
"""


def classify_water_availability(mm_value: float) -> str:
    """
    Classify water availability into 5 categories based on mm value.
    
    Args:
        mm_value: Water availability in millimeters
        
    Returns:
        Category string: "Very Low", "Low", "Medium", "High", or "Very High"
    """
    if mm_value <= 200:
        return "Very Low"
    elif mm_value <= 400:
        return "Low"
    elif mm_value <= 600:
        return "Medium"
    elif mm_value <= 1000:
        return "High"
    else:
        return "Very High"


def get_water_category_info() -> dict:
    """
    Get information about all water availability categories.
    
    Returns:
        Dictionary with category names and their mm ranges
    """
    return {
        "Very Low": {"min": 0, "max": 200, "description": "Very limited water, suitable for drought-tolerant crops"},
        "Low": {"min": 200, "max": 400, "description": "Limited water, suitable for pulse crops and barley"},
        "Medium": {"min": 400, "max": 600, "description": "Moderate water, suitable for wheat, maize, vegetables"},
        "High": {"min": 600, "max": 1000, "description": "Good water availability, suitable for most crops"},
        "Very High": {"min": 1000, "max": None, "description": "Abundant water, suitable for rice, sugarcane, tea"}
    }


def get_water_requirement_for_crop(crop_name: str, crop_database: dict = None) -> str:
    """
    Get the water requirement category for a specific crop.
    
    Args:
        crop_name: Name of the crop
        crop_database: Optional crop database dictionary
        
    Returns:
        Water requirement category string
    """
    if crop_database is None:
        try:
            from data.crop_database import CROP_DATABASE
            crop_database = CROP_DATABASE
        except ImportError:
            return "Unknown"
    
    crop_info = crop_database.get(crop_name, {})
    water_mm = crop_info.get("Water Availability (mm)", "")
    
    if not water_mm:
        return "Unknown"
    
    # Parse the range (e.g., "450-650" or "1000-2000")
    try:
        if "-" in str(water_mm):
            min_val = int(str(water_mm).split("-")[0].strip())
            # Use the midpoint for classification
            max_val = int(str(water_mm).split("-")[1].strip())
            avg_value = (min_val + max_val) / 2
        else:
            avg_value = int(water_mm)
        
        return classify_water_availability(avg_value)
    except:
        return "Unknown"


def get_mm_from_category(category: str) -> float:
    """
    Get the midpoint mm value from a water category name.
    
    Args:
        category: Category string like "Very Low", "Low", "Medium", "High", "Very High"
        
    Returns:
        Midpoint mm value for the category (used for ML model input)
    """
    category_mm = {
        "Very Low": 100,    # midpoint of 0-200
        "Low": 300,         # midpoint of 200-400
        "Medium": 500,      # midpoint of 400-600
        "High": 800,        # midpoint of 600-1000
        "Very High": 1500   # midpoint of 1000-2000
    }
    return category_mm.get(category, 500)  # default to Medium
