import streamlit as st
import numpy as np
import pickle
from functools import lru_cache

from data.crop_loader import load_all_crops
from data.crop_database import CROP_DATABASE
from ml.ml_predictor import predict_yield as predict_yield_with_model
from utils.water_classifier import classify_water_availability, get_mm_from_category


# CSV crops that match training data (from utils.shared_constants)
CSV_CROP_MAPPING = {
    "bajra": "Bajra",
    "barley": "Barley",
    "cotton": "Cotton",
    "chickpea": "Gram (Chana)",
    "groundnut": "Groundnut",
    "jowar": "Jowar",
    "maize": "Maize",
    "green_gram": "Moong",
    "mustard": "Mustard",
    "onion": "Onion",
    "potato": "Potato",
    "rice": "Rice",
    "soybean": "Soybean",
    "sugarcane": "Sugarcane",
    "tomato": "Tomato",
    "pigeon_pea": "Tur (Arhar)",
    "urad": "Urad",
    "wheat": "Wheat",
}

# List of crops available in training data
TRAINING_CROPS = list(CSV_CROP_MAPPING.values())

# Month mapping
MONTH_TO_NUM = {
    "January": 1, "February": 2, "March": 3, "April": 4,
    "May": 5, "June": 6, "July": 7, "August": 8,
    "September": 9, "October": 10, "November": 11, "December": 12,
}

CROP_NAME_ALIASES = {
    "Bajra (Pearl Millet)": "Bajra",
    "Brinjal (Eggplant)": "Brinjal",
    "Chili (Hot Pepper)": "Chili",
    "Jowar (Sorghum)": "Jowar",
    "Urad (Black Gram)": "Urad",
}

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


# NEW MODEL LOADERS (v3 - using new CSV with Season support)
@lru_cache(maxsize=1)
def _load_yield_model_new():
    """Load the new yield prediction model (trained with augmented_crop_data_v2.csv)"""
    try:
        with open("ml/models/yield_model_new.pkl", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None


@lru_cache(maxsize=1)
def _load_yield_scaler_new():
    """Load the scaler for new model"""
    try:
        with open("ml/models/yield_scaler_new.pkl", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None


@lru_cache(maxsize=1)
def _load_crop_encoder_new():
    """Load the crop encoder for new model"""
    try:
        with open("ml/models/yield_crop_encoder_new.pkl", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None


@lru_cache(maxsize=1)
def _load_state_encoder_new():
    """Load the state encoder for new model"""
    try:
        with open("ml/models/yield_state_encoder_new.pkl", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None


@lru_cache(maxsize=1)
def _load_season_encoder_new():
    """Load the season encoder for new model"""
    try:
        with open("ml/models/yield_season_encoder_new.pkl", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None


# IMPROVED MODEL LOADERS (v2 with Crop and pH features)
@lru_cache(maxsize=1)
def _load_yield_model_improved():
    """Load the improved yield prediction model"""
    try:
        with open("ml/models/yield_model_improved.pkl", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None


@lru_cache(maxsize=1)
def _load_yield_scaler_improved():
    """Load the scaler for improved model"""
    try:
        with open("ml/models/yield_scaler_improved.pkl", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None


@lru_cache(maxsize=1)
def _load_crop_encoder_improved():
    """Load the crop encoder for improved model"""
    try:
        with open("ml/models/yield_crop_encoder_improved.pkl", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None


@lru_cache(maxsize=1)
def _load_state_encoder_improved():
    """Load the state encoder for improved model"""
    try:
        with open("ml/models/yield_state_encoder_improved.pkl", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None


# Fallback to original model loaders
@lru_cache(maxsize=1)
def _load_yield_model():
    """Load the trained yield prediction model"""
    try:
        with open("ml/models/yield_model.pkl", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None


@lru_cache(maxsize=1)
def _load_yield_scaler():
    """Load the scaler for feature preprocessing"""
    try:
        with open("ml/models/yield_scaler.pkl", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None


@lru_cache(maxsize=1)
def _load_state_encoder():
    """Load the state encoder"""
    try:
        with open("ml/models/yield_state_encoder.pkl", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None


# Try to import enhanced soil estimator, fallback to basic if not available
try:
    from utils.enhanced_soil_estimator import estimate_npk
except ImportError:
    # Basic fallback
    def estimate_npk(soil_type, state=None, month=None):
        defaults = {
            "Black": {"N": 80, "P": 45, "K": 40},
            "Alluvial": {"N": 70, "P": 40, "K": 35},
            "Red": {"N": 60, "P": 35, "K": 30},
            "Sandy": {"N": 50, "P": 30, "K": 25},
            "Clay": {"N": 75, "P": 42, "K": 38},
        }
        return defaults.get(soil_type, {"N": 60, "P": 35, "K": 30})


def predict_yield_ml(
    state: str,
    crop_name: str,
    month: str,
    nitrogen: float,
    phosphorus: float,
    potassium: float,
    temperature: float,
    water_availability: float,
    season: str = "Kharif"
) -> dict:
    """Predict crop yield using the shared ML predictor and saved feature schema."""

    normalized_crop_name = CROP_NAME_ALIASES.get(crop_name, crop_name)

    try:
        result = predict_yield_with_model(
            state=state,
            crop=normalized_crop_name,
            month=month,
            nitrogen=nitrogen,
            phosphorus=phosphorus,
            potassium=potassium,
            temperature=temperature,
            water_availability=water_availability,
            season=season,
        )
    except Exception as e:
        return {
            "error": f"Prediction error: {str(e)}",
            "predicted_yield": None,
            "confidence": "N/A"
        }

    if result.get("predicted_yield") is not None:
        result["crop"] = crop_name

    if result.get("error"):
        result["error"] = f"Prediction error: {result['error']}"

    return result


st.set_page_config(page_title="Yield Estimator", page_icon="📈", layout="wide")


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
        <h1 style="color: white; margin: 0; font-size: 36px;">📈 Yield Estimator</h1>
        <p style="color: rgba(255,255,255,0.9); margin: 10px 0 0 0; font-size: 16px;">
            ML-powered yield prediction with soil and climate inputs
        </p>
    </div>
    """, unsafe_allow_html=True)

    crops = load_all_crops()
    crop_names = sorted(crops.keys())

    if not crop_names:
        st.error("No crops found in `data/crops`.")
        return

    st.markdown('<p class="section-header">🧪 Input Details</p>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        crop_name = st.selectbox("Crop", crop_names, index=0)
        state = st.selectbox("State", ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
             "Gujarat", "Haryana", "Himachal Pradesh", "Jammu & Kashmir", "Jharkhand",
             "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Meghalaya",
             "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim",
             "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"], index=12)
        # Season selection (required for new model v3)
        season = st.selectbox("Season", ["Kharif", "Rabi", "Zaid", "Whole Year"], index=0)
    with col2:
        month = st.selectbox("Month of Sowing", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], index=5)
        soil_type = st.selectbox("Soil Type", ["Black", "Alluvial", "Red", "Sandy", "Clay"], index=1)
    with col3:
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
        
        # Display selected water category info
        category_info = {
            "Very Low": "🔴 Very limited water - suitable for drought-tolerant crops",
            "Low": "🟠 Limited water - suitable for pulse crops and barley",
            "Medium": "🟡 Moderate water - suitable for wheat, maize, vegetables",
            "High": "🟢 Good water - suitable for most crops",
            "Very High": "🔵 Abundant water - suitable for rice, sugarcane, tea"
        }
        st.info(f"💧 {category_info.get(water_category, '')}")

    st.markdown('<p class="section-header">🌱 Soil Nutrients (Optional)</p>', unsafe_allow_html=True)
    col_n1, col_n2, col_n3 = st.columns(3)
    with col_n1:
        nitrogen = st.number_input("Nitrogen (N)", min_value=0.0, max_value=200.0, value=None, placeholder="Auto-estimate")
    with col_n2:
        phosphorus = st.number_input("Phosphorus (P)", min_value=0.0, max_value=200.0, value=None, placeholder="Auto-estimate")
    with col_n3:
        potassium = st.number_input("Potassium (K)", min_value=0.0, max_value=200.0, value=None, placeholder="Auto-estimate")

    if st.button("Predict Yield"):
        if nitrogen is None or phosphorus is None or potassium is None:
            month_num = MONTH_TO_NUM.get(month, 6)
            npk_values = estimate_npk(soil_type, state, month_num)
            nitrogen = npk_values["N"]
            phosphorus = npk_values["P"]
            potassium = npk_values["K"]
            st.info(f"Using estimated NPK: N={nitrogen}, P={phosphorus}, K={potassium}")

        result = predict_yield_ml(state=state, crop_name=crop_name, month=month, nitrogen=nitrogen, phosphorus=phosphorus, potassium=potassium, temperature=temperature, water_availability=water_availability, season=season)

        if "error" in result:
            st.error(result["error"])
        else:
            st.markdown('<p class="section-header">📊 Yield Prediction Result</p>', unsafe_allow_html=True)
            
            # Custom styled result cards with better spacing
            st.markdown("""
            <style>
            .yield-result {
                background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
                border-radius: 15px;
                padding: 25px;
                color: white;
                text-align: center;
                margin: 10px 0;
            }
            .yield-value {
                font-size: 36px;
                font-weight: bold;
                margin: 10px 0;
            }
            .yield-label {
                font-size: 14px;
                opacity: 0.9;
            }
            .yield-details {
                display: flex;
                justify-content: space-around;
                margin-top: 15px;
                padding-top: 15px;
                border-top: 1px solid rgba(255,255,255,0.3);
            }
            .yield-detail-item {
                text-align: center;
            }
            .yield-detail-label {
                font-size: 12px;
                opacity: 0.8;
            }
            .yield-detail-value {
                font-size: 16px;
                font-weight: bold;
            }
            </style>
            """, unsafe_allow_html=True)
            
            # Display styled result
            yield_val = result.get('predicted_yield', '-')
            unit = result.get('unit', '')
            crop_val = result.get('crop', '-')
            state_val = result.get('state', '-')
            conf = result.get('confidence', '-')
            
            st.markdown(f"""
            <div class="yield-result">
                <div class="yield-label">Predicted Yield for {crop_val}</div>
                <div class="yield-value">{yield_val} {unit}</div>
                <div class="yield-details">
                    <div class="yield-detail-item">
                        <div class="yield-detail-label">State</div>
                        <div class="yield-detail-value">{state_val}</div>
                    </div>
                    <div class="yield-detail-item">
                        <div class="yield-detail-label">Model</div>
                        <div class="yield-detail-value">{conf}</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
