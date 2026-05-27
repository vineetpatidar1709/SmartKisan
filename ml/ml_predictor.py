"""Unified ML Prediction Module

This module provides a unified interface for:
- Crop Recommendation (using ensemble model)
- Yield Prediction (using ensemble model)

Features:
- Automatic model loading with fallback
- Feature engineering
- Error handling
- Logging
"""
import numpy as np
import joblib
import pickle
from typing import Dict, List, Optional, Tuple
import warnings
warnings.filterwarnings('ignore')

# Month mapping
MONTH_TO_NUM = {
    "January": 1, "February": 2, "March": 3, "April": 4,
    "May": 5, "June": 6, "July": 7, "August": 8,
    "September": 9, "October": 10, "November": 11, "December": 12,
}

# Season mapping
SEASON_FROM_MONTH = {
    1: "Rabi", 2: "Rabi", 3: "Zaid",
    4: "Zaid", 5: "Kharif", 6: "Kharif",
    7: "Kharif", 8: "Kharif", 9: "Kharif",
    10: "Rabi", 11: "Rabi", 12: "Rabi"
}

# ==================== CROP CATEGORY DEFINITIONS ====================
# Priority: Food Crops > Oilseeds > Cash Crops > Other

CROP_CATEGORIES = {
    # Food Crops (Cereals, Pulses, Vegetables only - NO FRUITS)
    "Rice": "food", "Wheat": "food", "Maize": "food", "Bajra": "food",
    "Jowar": "food", "Barley": "food", "Chickpea": "food", "Pigeon Pea": "food",
    "Green Gram": "food", "Red Lentil": "food", "Urad": "food", "Potato": "food",
    "Tomato": "food", "Onion": "food", "Brinjal": "food", "Cabbage": "food",
    "Cucumber": "food", "Watermelon": "food",
    
    # Fruits - moved to OTHER category (low priority)
    "Banana": "other", "Mango": "other", "Apple": "other", "Orange": "other",
    "Guava": "other", "Litchi": "other", "Jackfruit": "other", "Peach": "other",
    "Pear": "other", "Plum": "other", "Apricot": "other", "Cherry": "other",
    "Walnut": "other", "Almond": "other",
    
    # Oilseed Crops
    "Soybean": "oilseed", "Groundnut": "oilseed", "Mustard": "oilseed",
    
    # Cash Crops
    "Cotton": "cash", "Sugarcane": "cash", "Tea": "cash", "Coffee": "cash",
    "Jute": "cash", "Tobacco": "cash", "Rubber": "cash", "Arecanut": "cash",
    "Coconut": "cash", "Pineapple": "cash", "Chili": "cash", "Black Pepper": "cash",
    "Cardamom": "cash", "Large Cardamom": "cash", "Coriander": "cash", "Cumin": "cash",
    "Ginger": "cash", "Saffron": "cash", "Tapioca": "cash",
}

# Preference multipliers - MAXIMUM boosting for priority crops
# Increased confidence levels for food, oilseed and cash crops
PREFERENCE_MULTIPLIERS = {
    "food": 15.0,    # Food crops get 1500% boost (15x) - MAXIMUM priority
    "oilseed": 12.0,  # Oilseeds get 1200% boost (12x) - VERY HIGH priority
    "cash": 10.0,     # Cash crops get 1000% boost (10x) - HIGH priority
    "other": 0.1,     # Other crops (fruits) get 90% penalty - almost excluded
}


class CropRecommender:
    """Crop Recommendation using ML ensemble"""
    
    def __init__(self):
        self.model = None
        self.crop_encoder = None
        self.state_encoder = None
        self.season_encoder = None
        self.soil_encoder = None
        self.irrig_encoder = None
        self.scaler = None
        self.features = None
        self.ensemble_config = None
        self.model_label = "Model"
        self._load_models()

    def _configure_model_for_inference(self):
        """Keep inference compatible with restricted Windows environments."""
        if self.model is not None and hasattr(self.model, "n_jobs"):
            self.model.n_jobs = 1
    
    def _load_models(self):
        """Load all required models"""
        try:
            self.model = joblib.load("ml/models/crop_model_xgb_enhanced.pkl")
            self.crop_encoder = joblib.load("ml/models/crop_encoder_enhanced.pkl")
            self.state_encoder = joblib.load("ml/models/crop_state_encoder_enhanced.pkl")
            self.season_encoder = joblib.load("ml/models/crop_season_encoder_enhanced.pkl")
            self.soil_encoder = joblib.load("ml/models/crop_soil_encoder_enhanced.pkl")
            self.irrig_encoder = joblib.load("ml/models/crop_irrigation_encoder_enhanced.pkl")
            self.scaler = joblib.load("ml/models/crop_scaler_enhanced.pkl")
            self.features = joblib.load("ml/models/crop_features_enhanced.pkl")
            with open("ml/models/ensemble_config.pkl", "rb") as f:
                self.ensemble_config = pickle.load(f)
            self._configure_model_for_inference()
            print("Enhanced crop model loaded successfully")
        except FileNotFoundError:
            print("Enhanced crop model not found, trying legacy model...")
            try:
                self.model = joblib.load("ml/models/crop_model.pkl")
                self.crop_encoder = joblib.load("ml/models/crop_encoder.pkl")
                self.state_encoder = joblib.load("ml/models/state_encoder.pkl")
                self.season_encoder = joblib.load("ml/models/season_encoder.pkl")
                self.soil_encoder = joblib.load("ml/models/soil_encoder.pkl")
                self.irrig_encoder = joblib.load("ml/models/irrigation_encoder.pkl")
                self.scaler = joblib.load("ml/models/scaler.pkl")
                self.features = joblib.load("ml/models/feature_columns.pkl")
                self.ensemble_config = None
                self._configure_model_for_inference()
                print("Legacy crop model loaded successfully")
            except FileNotFoundError:
                print("No crop model found!")
                self.model = None
    
    def _get_season_from_month(self, month):
        """Get season from month number"""
        if isinstance(month, str):
            month = MONTH_TO_NUM.get(month, 6)
        return SEASON_FROM_MONTH.get(month, "Kharif")
    
    def _engineer_features(self, nitrogen, phosphorus, potassium, temperature, 
                          ph, water_requirement, state, season, soil, irrigation, month=None):
        """Engineer features for prediction"""
        # Encode categorical variables
        try:
            state_e = self.state_encoder.transform([state])[0]
        except:
            state_e = 0
        
        try:
            season_e = self.season_encoder.transform([season])[0]
        except:
            season_e = 0
        
        try:
            soil_e = self.soil_encoder.transform([soil])[0]
        except:
            soil_e = 0
        
        try:
            irrig_e = self.irrig_encoder.transform([irrigation])[0]
        except:
            irrig_e = 0
        
        # Month encoding
        month_num = month if month else 6
        if isinstance(month_num, str):
            month_num = MONTH_TO_NUM.get(month_num, 6)
        
        # Advanced feature engineering
        NPK_total = nitrogen + phosphorus + potassium
        N_ratio = nitrogen / (phosphorus + 1)
        P_ratio = phosphorus / (potassium + 1)
        N_K_ratio = nitrogen / (potassium + 1)
        
        N_deficit = 1 if nitrogen < 50 else 0
        P_deficit = 1 if phosphorus < 30 else 0
        K_deficit = 1 if potassium < 30 else 0
        
        ph_optimal = 1 if (ph >= 6.0 and ph <= 7.5) else 0
        ph_deviation = abs(ph - 6.5)
        ph_acidic = 1 if ph < 5.5 else 0
        ph_alkaline = 1 if ph > 8.0 else 0
        
        water_low = 1 if water_requirement < 400 else 0
        water_medium = 1 if (water_requirement >= 400 and water_requirement < 800) else 0
        water_high = 1 if water_requirement >= 800 else 0
        
        temp_optimal = 1 if (temperature >= 20 and temperature <= 30) else 0
        temp_deviation = abs(temperature - 25)
        
        soil_quality = (nitrogen + phosphorus + potassium) / 3
        soil_score = soil_quality * (1 - ph_deviation / 10)
        climate_score = (temp_optimal + ph_optimal + water_medium) / 3
        
        month_sin = np.sin(2 * np.pi * month_num / 12)
        month_cos = np.cos(2 * np.pi * month_num / 12)
        
        temp_water = temperature * water_requirement / 1000
        N_water = nitrogen * water_requirement / 1000
        
        # Build feature dictionary
        feature_dict = {
            "N": nitrogen, "P": phosphorus, "K": potassium,
            "temperature_c": temperature, "pH": ph,
            "water_requirement": water_requirement,
            "state_e": state_e, "season_e": season_e,
            "soil_e": soil_e, "irrig_e": irrig_e,
            "NPK_total": NPK_total, "N_ratio": N_ratio,
            "P_ratio": P_ratio, "N_K_ratio": N_K_ratio,
            "N_deficit": N_deficit, "P_deficit": P_deficit,
            "K_deficit": K_deficit, "ph_optimal": ph_optimal,
            "ph_deviation": ph_deviation, "ph_acidic": ph_acidic,
            "ph_alkaline": ph_alkaline, "water_low": water_low,
            "water_medium": water_medium, "water_high": water_high,
            "temp_optimal": temp_optimal, "temp deviation": temp_deviation,
            "soil_quality": soil_quality, "soil_score": soil_score,
            "climate_score": climate_score, "month_sin": month_sin,
            "month_cos": month_cos, "temp_water": temp_water,
            "N_water": N_water
        }
        
        # Create feature array in correct order
        features = np.array([[feature_dict.get(f, 0) for f in self.features]], dtype=float)
        
        return features
    
    def recommend(self, state, month, nitrogen, phosphorus, potassium,
                  temperature, rainfall, ph=6.5, soil_type="Alluvial",
                  irrigation_method="Canal", top_k=5) -> List[Dict]:
        """
        Recommend crops based on input parameters
        
        Returns list of dicts with 'crop' and 'probability' keys
        """
        if self.model is None:
            return [{"crop": "Error", "probability": 0, "error": "Model not loaded"}]
        
        # Get season from month
        if isinstance(month, str):
            month_num = MONTH_TO_NUM.get(month, 6)
        else:
            month_num = month
        
        season = self._get_season_from_month(month_num)
        
        # Engineer features
        features = self._engineer_features(
            nitrogen, phosphorus, potassium, temperature,
            ph, rainfall, state, season, soil_type, irrigation_method, month_num
        )
        
        # Get predictions
        try:
            probs = self.model.predict_proba(features)[0]
            classes = self.crop_encoder.classes_
            
            # Apply preference multipliers based on crop category
            # This boosts food crops, oilseeds, and cash crops over other crops
            adjusted_probs = probs.copy()
            for i, crop_name in enumerate(classes):
                category = CROP_CATEGORIES.get(str(crop_name), None)
                multiplier = PREFERENCE_MULTIPLIERS.get(category, 1.0)
                adjusted_probs[i] = probs[i] * multiplier
            
            # Sort by adjusted probability
            ranked_indices = np.argsort(adjusted_probs)[::-1]
            
            # Get top_k results and normalize confidence to sum to 100%
            top_k_indices = ranked_indices[:top_k]
            top_k_probs = probs[top_k_indices]
            top_k_adjusted = adjusted_probs[top_k_indices]
            
            # Normalize the ADJUSTED probabilities for display so they sum to 100%
            if top_k_adjusted.sum() > 0:
                display_probs = top_k_adjusted / top_k_adjusted.sum()
            else:
                display_probs = top_k_probs / top_k_probs.sum() if top_k_probs.sum() > 0 else top_k_probs
            
            results = []
            for idx, i in enumerate(top_k_indices):
                results.append({
                    "crop": str(classes[i]),
                    "probability": float(display_probs[idx])
                })
            
            return results
        except Exception as e:
            return [{"crop": "Error", "probability": 0, "error": str(e)}]


class YieldPredictor:
    """Yield Prediction using ML ensemble"""
    
    def __init__(self):
        self.model = None
        self.crop_encoder = None
        self.state_encoder = None
        self.season_encoder = None
        self.soil_encoder = None
        self.irrig_encoder = None
        self.scaler = None
        self.features = None
        self.ensemble_config = None
        self._load_models()

    def _configure_model_for_inference(self):
        """Keep inference compatible with restricted Windows environments."""
        if self.model is not None and hasattr(self.model, "n_jobs"):
            self.model.n_jobs = 1
    
    def _load_models(self):
        """Load all required models"""
        try:
            self.model = joblib.load("ml/models/yield_model_xgb_enhanced.pkl")
            self.crop_encoder = joblib.load("ml/models/yield_crop_encoder_enhanced.pkl")
            self.state_encoder = joblib.load("ml/models/yield_state_encoder_enhanced.pkl")
            self.season_encoder = joblib.load("ml/models/yield_season_encoder_enhanced.pkl")
            self.soil_encoder = joblib.load("ml/models/yield_soil_encoder_enhanced.pkl")
            self.irrig_encoder = joblib.load("ml/models/yield_irrigation_encoder_enhanced.pkl")
            self.scaler = joblib.load("ml/models/yield_scaler_enhanced.pkl")
            self.features = joblib.load("ml/models/yield_features_enhanced.pkl")
            with open("ml/models/yield_ensemble_config.pkl", "rb") as f:
                self.ensemble_config = pickle.load(f)
            self._configure_model_for_inference()
            self.model_label = "Enhanced Model"
            print("Enhanced yield model loaded successfully")
        except FileNotFoundError:
            print("Enhanced yield model not found, trying legacy model...")
            try:
                self.model = joblib.load("ml/models/yield_model.pkl")
                self.crop_encoder = joblib.load("ml/models/yield_crop_encoder.pkl")
                self.state_encoder = joblib.load("ml/models/yield_state_encoder.pkl")
                self.season_encoder = joblib.load("ml/models/yield_season_encoder.pkl")
                self.soil_encoder = joblib.load("ml/models/yield_soil_encoder.pkl")
                self.irrig_encoder = joblib.load("ml/models/yield_irrigation_encoder.pkl")
                self.scaler = joblib.load("ml/models/yield_scaler.pkl")
                self.features = joblib.load("ml/models/yield_features.pkl")
                self.ensemble_config = None
                self._configure_model_for_inference()
                self.model_label = "Legacy Model"
                print("Legacy yield model loaded successfully")
            except FileNotFoundError:
                print("No yield model found!")
                self.model = None
    
    def _get_season_from_month(self, month):
        """Get season from month number"""
        if isinstance(month, str):
            month = MONTH_TO_NUM.get(month, 6)
        return SEASON_FROM_MONTH.get(month, "Kharif")
    
    def _engineer_features(self, state, crop, season, soil, irrigation,
                          nitrogen, phosphorus, potassium, temperature, 
                          ph, water_requirement):
        """Engineer features for prediction"""
        # Encode categorical variables
        try:
            state_e = self.state_encoder.transform([state])[0]
        except:
            state_e = 0
        
        try:
            crop_e = self.crop_encoder.transform([crop])[0]
        except:
            crop_e = 0
        
        try:
            season_e = self.season_encoder.transform([season])[0]
        except:
            season_e = 0
        
        try:
            soil_e = self.soil_encoder.transform([soil])[0]
        except:
            soil_e = 0
        
        try:
            irrig_e = self.irrig_encoder.transform([irrigation])[0]
        except:
            irrig_e = 0
        
        # Advanced feature engineering
        N_P = nitrogen / (phosphorus + 1)
        N_K = nitrogen / (potassium + 1)
        P_K = phosphorus / (potassium + 1)
        NPK_total = nitrogen + phosphorus + potassium
        NPK_product = nitrogen * phosphorus * potassium / 1000
        NPK_balance = abs(nitrogen - phosphorus) + abs(phosphorus - potassium)
        
        N_high = 1 if nitrogen > 100 else 0
        P_high = 1 if phosphorus > 50 else 0
        K_high = 1 if potassium > 100 else 0
        
        ph_optimal = 1 if (ph >= 6.0 and ph <= 7.5) else 0
        ph_deviation = abs(ph - 6.5)
        ph_stress = 1 if (ph < 5.5 or ph > 8.5) else 0
        
        temp_optimal = 1 if (temperature >= 20 and temperature <= 30) else 0
        temp_stress = 1 if (temperature < 15 or temperature > 35) else 0
        temp_deviation = abs(temperature - 25)
        
        water_stress = 1 if water_requirement < 300 else 0
        water_excess = 1 if water_requirement > 1500 else 0
        
        Soil_Qual = (nitrogen + phosphorus + potassium) / 3
        Soil_Index = Soil_Qual * (1 - ph_deviation / 10) * temp_optimal
        Climate_Score = (temp_optimal + ph_optimal) / 2
        
        Temp_Water = temperature * water_requirement / 1000
        Temp_Water_Stress = temp_stress * water_stress
        
        # Month from season
        month_map = {"Kharif": 7, "Rabi": 11, "Zaid": 3, "Whole Year": 6}
        month_num = month_map.get(season, 6)
        month_sin = np.sin(2 * np.pi * month_num / 12)
        month_cos = np.cos(2 * np.pi * month_num / 12)
        
        soil_water = soil_e * water_requirement / 1000
        soil_temp = soil_e * temperature
        
        crop_season_interaction = crop_e * 10 + season_e
        
        Input_Score = nitrogen + phosphorus + potassium + water_requirement / 10
        
        # Build feature dictionary
        feature_dict = {
            "State_E": state_e, "Crop_E": crop_e, "Season_E": season_e,
            "Soil_E": soil_e, "Irrig_E": irrig_e,
            "N": nitrogen, "P": phosphorus, "K": potassium,
            "temperature_c": temperature, "pH": ph,
            "water_requirement": water_requirement,
            "N_P": N_P, "N_K": N_K, "P_K": P_K,
            "NPK_total": NPK_total, "NPK_product": NPK_product,
            "NPK_balance": NPK_balance,
            "N_high": N_high, "P_high": P_high, "K_high": K_high,
            "ph_optimal": ph_optimal, "ph_deviation": ph_deviation,
            "ph_stress": ph_stress,
            "temp_optimal": temp_optimal, "temp_stress": temp_stress,
            "temp_deviation": temp_deviation,
            "water_stress": water_stress, "water_excess": water_excess,
            "Soil_Qual": Soil_Qual, "Soil_Index": Soil_Index,
            "Climate_Score": Climate_Score,
            "Temp_Water": Temp_Water, "Temp_Water_Stress": Temp_Water_Stress,
            "month_sin": month_sin, "month_cos": month_cos,
            "soil_water": soil_water, "soil_temp": soil_temp,
            "crop_season_interaction": crop_season_interaction,
            "Input_Score": Input_Score
        }
        
        # Create feature array in correct order
        features = np.array([[feature_dict.get(f, 0) for f in self.features]], dtype=float)
        
        return features
    
    def predict(self, state, crop, month, nitrogen, phosphorus, potassium,
                temperature, water_availability, season=None) -> Dict:
        """
        Predict yield based on input parameters
        
        Returns dict with 'predicted_yield' and other metadata
        """
        if self.model is None:
            return {"error": "Model not loaded", "predicted_yield": None}
        
        # Get season from month if not provided
        if season is None:
            if isinstance(month, str):
                month_num = MONTH_TO_NUM.get(month, 6)
            else:
                month_num = month
            season = self._get_season_from_month(month_num)
        
        # Engineer features
        features = self._engineer_features(
            state, crop, season, "Alluvial", "Canal",
            nitrogen, phosphorus, potassium, temperature, 6.5, water_availability
        )
        
        # Scale features
        try:
            features_scaled = self.scaler.transform(features)
        except:
            features_scaled = features
        
        # Get prediction
        try:
            predicted_yield = self.model.predict(features_scaled)[0]
            predicted_yield = max(0, predicted_yield)
            
            return {
                "predicted_yield": round(float(predicted_yield), 2),
                "unit": "quintals per hectare",
                "state": state,
                "crop": crop,
                "season": season,
                "confidence": self.model_label
            }
        except Exception as e:
            return {"error": str(e), "predicted_yield": None}


# Singleton instances
_crop_recommender = None
_yield_predictor = None


def get_crop_recommender() -> CropRecommender:
    """Get singleton crop recommender instance"""
    global _crop_recommender
    if _crop_recommender is None:
        _crop_recommender = CropRecommender()
    return _crop_recommender


def get_yield_predictor() -> YieldPredictor:
    """Get singleton yield predictor instance"""
    global _yield_predictor
    if _yield_predictor is None:
        _yield_predictor = YieldPredictor()
    return _yield_predictor


def recommend_crops(state, month, nitrogen, phosphorus, potassium,
                    temperature, rainfall, ph=6.5, soil_type="Alluvial",
                    irrigation_method="Canal", top_k=5) -> List[Dict]:
    """Convenience function for crop recommendation"""
    recommender = get_crop_recommender()
    return recommender.recommend(
        state, month, nitrogen, phosphorus, potassium,
        temperature, rainfall, ph, soil_type, irrigation_method, top_k
    )


def predict_yield(state, crop, month, nitrogen, phosphorus, potassium,
                   temperature, water_availability, season=None) -> Dict:
    """Convenience function for yield prediction"""
    predictor = get_yield_predictor()
    return predictor.predict(
        state, crop, month, nitrogen, phosphorus, potassium,
        temperature, water_availability, season
    )

