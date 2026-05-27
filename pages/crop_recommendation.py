"""
Crop Recommendation Page with ML-based predictions

This module contains:
- UI for crop recommendation
- Core recommendation logic (inlined from utils/crop_recommendation.py)
"""

import streamlit as st
import numpy as np
import joblib
from functools import lru_cache
from typing import List, Dict, Optional

from utils.enhanced_soil_estimator import estimate_npk
from data.crop_database import CROP_DATABASE
from utils.water_classifier import classify_water_availability, get_water_category_info, get_mm_from_category


st.set_page_config(
    page_title="Crop Recommendation",
    page_icon="🌾",
    layout="wide",
)

def apply_custom_styles():
    st.markdown("""
    <style>
    .section-header {
        font-size: 20px;
        font-weight: bold;
        color: #1B5E20;
        margin: 20px 0 15px 0;
        padding-bottom: 10px;
        border-bottom: 2px solid #4CAF50;
    }
    .card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        border-radius: 16px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        border-left: 5px solid #4CAF50;
    }
    </style>
    """, unsafe_allow_html=True)


# ==================== CROP CATEGORY DEFINITIONS ====================
# Priority: Food Crops > Oilseeds > Cash Crops > Other

CROP_CATEGORIES = {
    # Food Crops (Cereals, Pulses, Vegetables only - NO FRUITS)
    "Rice": "food",
    "Wheat": "food",
    "Maize": "food",
    "Bajra": "food",
    "Jowar": "food",
    "Barley": "food",
    "Chickpea": "food",
    "Pigeon Pea": "food",
    "Green Gram": "food",
    "Red Lentil": "food",
    "Urad": "food",
    "Potato": "food",
    "Tomato": "food",
    "Onion": "food",
    "Brinjal": "food",
    "Cabbage": "food",
    "Cucumber": "food",
    "Watermelon": "food",
    
    # Fruits - moved to OTHER category (low priority)
    "Banana": "other",
    "Mango": "other",
    "Apple": "other",
    "Orange": "other",
    "Guava": "other",
    "Litchi": "other",
    "Jackfruit": "other",
    "Peach": "other",
    "Pear": "other",
    "Plum": "other",
    "Apricot": "other",
    "Cherry": "other",
    "Walnut": "other",
    "Almond": "other",
    
    # Oilseed Crops
    "Soybean": "oilseed",
    "Groundnut": "oilseed",
    "Mustard": "oilseed",
    
    # Cash Crops (Commercial crops)
    "Cotton": "cash",
    "Sugarcane": "cash",
    "Tea": "cash",
    "Coffee": "cash",
    "Jute": "cash",
    "Tobacco": "cash",
    "Rubber": "cash",
    "Arecanut": "cash",
    "Coconut": "cash",
    "Pineapple": "cash",
    
    # Spices (Cash crops)
    "Chili": "cash",
    "Black Pepper": "cash",
    "Cardamom": "cash",
    "Large Cardamom": "cash",
    "Coriander": "cash",
    "Cumin": "cash",
    "Ginger": "cash",
    "Saffron": "cash",
    "Tapioca": "cash",
}

# Preference multipliers - MAXIMUM boosting for priority crops
# Increased confidence levels for food, oilseed and cash crops
PREFERENCE_MULTIPLIERS = {
    "food": 15.0,    # Food crops get 1500% boost (15x) - MAXIMUM priority
    "oilseed": 12.0,  # Oilseeds get 1200% boost (12x) - VERY HIGH priority
    "cash": 10.0,     # Cash crops get 1000% boost (10x) - HIGH priority
    "other": 0.1,     # Other crops (fruits) get 90% penalty - almost excluded
}


# ==================== CORE RECOMMENDATION LOGIC ====================
# (Inlined from utils/crop_recommendation.py)

MONTH_TO_NUM = {
    "January": 1, "February": 2, "March": 3, "April": 4,
    "May": 5, "June": 6, "July": 7, "August": 8,
    "September": 9, "October": 10, "November": 11, "December": 12,
}

FALLBACK_SUITABLE_MONTHS = {
    "Chickpea": [10, 11],
    "Pigeon Pea": [6, 7],
    "Green Gram": [6, 7],
    "Red Lentil": [10, 11],
    "Cucumber": [2, 3, 6, 7],
    "Watermelon": [2, 3, 4],
}


@lru_cache(maxsize=1)
def _load_model():
    """Load the trained XGBoost crop recommendation model (v2)"""
    return joblib.load("ml/models/crop_model_xgb_v2.pkl")


@lru_cache(maxsize=1)
def _load_crop_encoder():
    """Load the crop label encoder (v2)"""
    return joblib.load("ml/models/crop_encoder_v2.pkl")


@lru_cache(maxsize=1)
def _load_state_encoder():
    """Load the state encoder (v2)"""
    return joblib.load("ml/models/crop_state_encoder_v2.pkl")


@lru_cache(maxsize=1)
def _load_season_encoder():
    """Load the season encoder (v2)"""
    return joblib.load("ml/models/crop_season_encoder_v2.pkl")


@lru_cache(maxsize=1)
def _load_soil_encoder():
    """Load the soil encoder (v2)"""
    return joblib.load("ml/models/crop_soil_encoder_v2.pkl")


@lru_cache(maxsize=1)
def _load_irrig_encoder():
    """Load the irrigation encoder (v2)"""
    return joblib.load("ml/models/crop_irrigation_encoder_v2.pkl")


@lru_cache(maxsize=1)
def _load_features():
    """Load the features list (v2)"""
    return joblib.load("ml/models/crop_features_v2.pkl")


def recommend_crop(
    state: str,
    month,
    nitrogen: float,
    phosphorus: float,
    potassium: float,
    temperature: float,
    rainfall: float,
    ph: float = 6.5,
    soil_type: str = None,
    irrigation_method: str = "Canal",
    top_k: int = 5,
) -> List[Dict[str, float]]:
    """
    Returns a list of {'crop': str, 'probability': float} sorted by probability desc.
    Applies state/month filtering using CROP_DATABASE when available.
    Uses the improved XGBoost model v2 with 18 features.
    """
    # Load model and encoders
    model = _load_model()
    crop_encoder = _load_crop_encoder()
    state_encoder = _load_state_encoder()
    season_encoder = _load_season_encoder()
    soil_encoder = _load_soil_encoder()
    irrig_encoder = _load_irrig_encoder()
    
    # Convert month to number
    if isinstance(month, (int, float, np.integer)):
        month_num = int(month)
    else:
        month_num = MONTH_TO_NUM.get(str(month), 6)
    
    # Get season from month
    if month_num in [1, 2, 12]:
        season = "Rabi"
    elif month_num in [3, 4]:
        season = "Zaid"
    else:
        season = "Kharif"
    
    # Map soil type
    soil_map = {"Black": "Black", "Alluvial": "Alluvial", "Red": "Red", 
                "Sandy": "Sandy", "Clay": "Clay", "Laterite": "Laterite"}
    soil = soil_map.get(soil_type, "Alluvial")
    
    # Map irrigation
    irrigation_map = {"Rainfed": "Rainfed", "Canal": "Canal", "Tube Well": "Tube Well",
                    "Drip": "Drip", "Sprinkler": "Sprinkler", "Flood": "Flood"}
    irrigation = irrigation_map.get(irrigation_method, "Canal")
    
    # Encode categorical variables
    try:
        state_encoded = state_encoder.transform([state])[0]
    except:
        state_encoded = 0
    
    try:
        season_encoded = season_encoder.transform([season])[0]
    except:
        season_encoded = 0
    
    try:
        soil_encoded = soil_encoder.transform([soil])[0]
    except:
        soil_encoded = 0
    
    try:
        irrig_encoded = irrig_encoder.transform([irrigation])[0]
    except:
        irrig_encoded = 0
    
    # Feature engineering (must match training - 18 features)
    month_sin = np.sin(2 * np.pi * month_num / 12)
    month_cos = np.cos(2 * np.pi * month_num / 12)
    N_ratio = nitrogen / (phosphorus + 1)
    P_ratio = phosphorus / (potassium + 1)
    NPK_total = nitrogen + phosphorus + potassium
    temp_water = temperature * rainfall / 1000
    ph_deviation = abs(ph - 6.5)
    
    # Build feature array in correct order (18 features)
    features = np.array([[
        nitrogen, phosphorus, potassium, temperature, ph, rainfall,
        state_encoded, season_encoded, soil_encoded, irrig_encoded,
        NPK_total, N_ratio, P_ratio, temp_water,
        ph_deviation, month_sin, month_cos, month_num
    ]], dtype=float)

    # Get predictions from XGBoost model
    probs = model.predict_proba(features)[0]
    classes = crop_encoder.classes_

    # Apply preference multipliers based on crop category
    # This boosts food crops, oilseeds, and cash crops over other crops
    adjusted_probs = probs.copy()
    for i, crop_name in enumerate(classes):
        category = CROP_CATEGORIES.get(str(crop_name), None)
        multiplier = PREFERENCE_MULTIPLIERS.get(category, 1.0)
        adjusted_probs[i] = probs[i] * multiplier

    # Rank by adjusted probabilities
    ranked_indices = np.argsort(adjusted_probs)[::-1]

    def passes_filters(crop_name: str) -> bool:
        if month_num is None:
            return True

        info = CROP_DATABASE.get(crop_name)
        if info is not None:
            suitable_months = info.get("Suitable Months")
            if isinstance(suitable_months, list) and suitable_months and month_num not in suitable_months:
                return False
            major_states = info.get("Major States")
            if isinstance(major_states, list) and major_states and state and state not in major_states:
                return False
            return True

        fallback_months = FALLBACK_SUITABLE_MONTHS.get(crop_name)
        if isinstance(fallback_months, list) and fallback_months and month_num not in fallback_months:
            return False
        return True

    # Apply filters
    filtered = [i for i in ranked_indices if passes_filters(str(classes[i]))]
    chosen = filtered[: max(1, int(top_k))]
    
    if len(chosen) < max(1, int(top_k)):
        for i in ranked_indices:
            if i not in chosen:
                chosen.append(i)
            if len(chosen) == max(1, int(top_k)):
                break

    # Get probabilities for chosen crops - use ADJUSTED probabilities for display (not normalized)
    chosen_probs = np.array([probs[i] for i in chosen])
    chosen_adjusted = np.array([adjusted_probs[i] for i in chosen])
    
    # Normalize the ADJUSTED probabilities for display so they sum to 100%
    if chosen_adjusted.sum() > 0:
        display_probs = chosen_adjusted / chosen_adjusted.sum()
    else:
        display_probs = chosen_probs
    
    out = []
    for idx, i in enumerate(chosen):
        out.append({"crop": str(classes[i]), "probability": float(display_probs[idx])})
    return out


def generate_dashboard(
    state: str, month, nitrogen: float, phosphorus: float,
    potassium: float, temperature: float, rainfall: float
) -> Optional[List[Dict[str, float]]]:
    """Generate dashboard data - wrapper around recommend_crop"""
    return recommend_crop(
        state=state, month=month, nitrogen=nitrogen,
        phosphorus=phosphorus, potassium=potassium,
        temperature=temperature, rainfall=rainfall,
    )


# ==================== UI ====================

def main():
    apply_custom_styles()
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #4CAF50 0%, #2E7D32 100%);
        border-radius: 16px;
        padding: 25px;
        margin-bottom: 25px;
        text-align: center;
    ">
        <h1 style="color: white; margin: 0; font-size: 36px;">🌾 Crop Recommendation</h1>
        <p style="color: rgba(255,255,255,0.9); margin: 10px 0 0 0; font-size: 16px;">
            ML-powered crop suggestions based on soil and climate conditions
        </p>
    </div>
    """, unsafe_allow_html=True)

    # --- FARMER INPUTS ---
    st.markdown('<p class="section-header">🧪 Input Details</p>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        state = st.selectbox(
            "State",
            ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
             "Gujarat", "Haryana", "Himachal Pradesh", "Jammu & Kashmir", "Jharkhand",
             "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Meghalaya",
             "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim",
             "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"],
            index=12,
        )
        month = st.selectbox(
            "Month of Sowing",
            ["January", "February", "March", "April", "May", "June", 
             "July", "August", "September", "October", "November", "December"],
            index=5,
        )
        soil_type = st.selectbox(
            "Soil Type",
            ["Black", "Alluvial", "Red", "Sandy", "Clay"],
            index=1,
        )

    with col2:
        irrigation_method = st.selectbox(
            "Irrigation Method",
            ["Rainfed", "Canal", "Tube Well", "Drip", "Sprinkler"],
            index=1,
        )
        temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=60.0, value=25.0)
        
        # Water category selection (5 categories)
        water_category_options = [
            "🔴 Very Low (0-200 mm)",
            "🟠 Low (200-400 mm)", 
            "🟡 Medium (400-600 mm)",
            "🟢 High (600-1000 mm)",
            "🔵 Very High (>1000 mm)"
        ]
        water_category_display = st.selectbox("Water Availability", water_category_options, index=2)
        
        # Extract category name and mm value
        water_category = water_category_display.split(" (")[0].replace("🔴 ", "").replace("🟠 ", "").replace("🟡 ", "").replace("🟢 ", "").replace("🔵 ", "")
        water_availability = get_mm_from_category(water_category)
        
        ph = st.number_input("Soil pH", min_value=0.0, max_value=14.0, value=6.5)
        
        # Display selected water category info
        category_info = {
            "Very Low": "🔴 Very limited water - suitable for drought-tolerant crops",
            "Low": "🟠 Limited water - suitable for pulse crops and barley",
            "Medium": "🟡 Moderate water - suitable for wheat, maize, vegetables",
            "High": "🟢 Good water - suitable for most crops",
            "Very High": "🔵 Abundant water - suitable for rice, sugarcane, tea"
        }
        st.info(f"💧 {category_info.get(water_category, '')}")

    if st.button("Get Recommendations", type="primary"):
        npk_values = estimate_npk(soil_type)
        
        results = recommend_crop(
            state=state,
            month=month,
            nitrogen=npk_values["N"],
            phosphorus=npk_values["P"],
            potassium=npk_values["K"],
            temperature=temperature,
            rainfall=water_availability,
            ph=ph,
            top_k=5,
        )

        st.divider()
        st.markdown('<p class="section-header">🌱 Recommended Crops</p>', unsafe_allow_html=True)
        st.write(f"**State:** {state} | **Month:** {month} | **Soil:** {soil_type} | **Irrigation:** {irrigation_method} | **Water:** {water_category}")

        for result in results:
            crop_name = result["crop"]
            confidence = round(float(result["probability"]) * 100, 2)
            crop_info = CROP_DATABASE.get(crop_name, {})
            
            # Get crop category for display
            category = CROP_CATEGORIES.get(crop_name, "other")
            category_labels = {
                "food": "🍚 Food Crop",
                "oilseed": "🌻 Oilseed",
                "cash": "💰 Cash Crop"
            }
            category_label = category_labels.get(category, "📋 Other")
            
            with st.container():
                col_r1, col_r2 = st.columns([3, 1])
                with col_r1:
                    st.markdown(f"### 🌾 {crop_name}")
                    st.write(f"**{category_label}**")
                    st.write(f"**Water Requirement:** {crop_info.get('Water Requirement', 'N/A')}")
                    st.write(f"**Suitable Soil:** {crop_info.get('Soil', 'N/A')}")
                with col_r2:
                    st.metric("Confidence", f"{confidence}%")
                st.divider()


if __name__ == "__main__":
    main()
