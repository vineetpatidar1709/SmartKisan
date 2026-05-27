"""
Shared Constants and Utilities
Centralized module for constants and functions used across multiple files
to eliminate code duplication.
"""

import os
import streamlit as st
from typing import Optional

# ==================== MONTH MAPPING ====================
MONTH_TO_NUM = {
    "January": 1, "February": 2, "March": 3, "April": 4,
    "May": 5, "June": 6, "July": 7, "August": 8,
    "September": 9, "October": 10, "November": 11, "December": 12,
}

NUM_TO_MONTH = {v: k for k, v in MONTH_TO_NUM.items()}


# ==================== FALLBACK SUITABLE MONTHS ====================
FALLBACK_SUITABLE_MONTHS = {
    "Chickpea": [10, 11],
    "Pigeon Pea": [6, 7],
    "Green Gram": [6, 7],
    "Red Lentil": [10, 11],
    "Cucumber": [2, 3, 6, 7],
    "Watermelon": [2, 3, 4],
}


# ==================== STATES ====================
# 26 states for ML models (matching yield estimator)
STATES = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Gujarat", "Haryana", "Himachal Pradesh", "Jammu & Kashmir", "Jharkhand",
    "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Meghalaya",
    "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim",
    "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"
]


# ==================== SOIL TYPES ====================
SOIL_TYPES = ["Black", "Alluvial", "Red", "Sandy", "Clay"]


# ==================== IRRIGATION METHODS ====================
IRRIGATION_METHODS = ["Rainfed", "Canal", "Tube Well", "Drip", "Sprinkler"]


# ==================== CROP NAME MAPPING ====================
# Maps data/crops file names to CSV crop names
# CSV uses: "Gram (Chana)", "Tur (Arhar)", "Moong", etc.
# data/crops uses: "chickpea", "pigeon_pea", "green_gram", etc.

CROP_NAME_MAPPING = {
    # CSV Name -> data/crops file name
    "bajra": "bajra",
    "barley": "barley",
    "cotton": "cotton",
    "Gram (Chana)": "chickpea",
    "groundnut": "groundnut",
    "jowar": "jowar",
    "maize": "maize",
    "moong": "green_gram",
    "mustard": "mustard",
    "onion": "onion",
    "potato": "potato",
    "rice": "rice",
    "soybean": "soybean",
    "sugarcane": "sugarcane",
    "tomato": "tomato",
    "Tur (Arhar)": "pigeon_pea",
    "urad": "urad",
    "wheat": "wheat",
}

# Reverse mapping: data/crops file name -> CSV name
CSV_CROP_MAPPING = {v: k for k, v in CROP_NAME_MAPPING.items()}


# ==================== API UTILITIES ====================
def get_data_gov_api_key() -> str:
    """
    Get Data.gov.in API key from Streamlit secrets or environment.
    Returns empty string if not available.
    """
    api_key = ""
    
    # Try Streamlit secrets first
    try:
        api_key = st.secrets.get("DATA_GOV_IN_API_KEY", "")
    except Exception:
        pass
    
    # Fallback to environment variable
    if not api_key:
        api_key = os.getenv("DATA_GOV_IN_API_KEY", "")
    
    return str(api_key).strip()


def get_api_key_with_warning() -> str:
    """Get API key and return warning status"""
    api_key = get_data_gov_api_key()
    has_key = bool(api_key)
    return api_key, has_key
