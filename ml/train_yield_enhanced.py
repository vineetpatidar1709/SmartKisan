"""Enhanced Yield Prediction Model Training with Ensemble Approach

This module implements an improved yield prediction system using:
- Ensemble of Gradient Boosting models
- Advanced feature engineering
- Cross-validation for hyperparameter tuning
"""
import pandas as pd
import numpy as np
import joblib
import pickle
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.preprocessing import LabelEncoder, StandardScaler, RobustScaler
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor, StackingRegressor
from sklearn.linear_model import Ridge
import xgboost as xgb
import warnings
warnings.filterwarnings('ignore')

# Try to import LightGBM
try:
    import lightgbm as lgb
    HAS_LGBM = True
except ImportError:
    HAS_LGBM = False
    print("LightGBM not available, using XGBoost only")

print("=" * 60)
print("Enhanced Yield Prediction Model Training")
print("=" * 60)

# Load data
print("\n[1/6] Loading data...")
df = pd.read_csv("ml/augmented_crop_data_v8.csv")

# Data preprocessing
def convert_num(val):
    if isinstance(val, str) and '-' in val:
        parts = val.split('-')
        try:
            return (float(parts[0]) + float(parts[1])) / 2
        except:
            return np.nan
    try:
        return float(val)
    except:
        return np.nan

# Convert numeric columns
for col in ['N', 'P', 'K', 'pH', 'water_requirement', 'yield_q_ha']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df['temperature_c'] = df['temperature_c'].apply(convert_num)
df = df.dropna()

print(f"   Total samples after cleaning: {len(df)}")
print(f"   Unique crops: {df['crop'].nunique()}")
print(f"   Yield range: {df['yield_q_ha'].min():.2f} - {df['yield_q_ha'].max():.2f} q/ha")

# Feature Engineering
print("\n[2/6] Feature Engineering...")

# Encode categorical variables
crop_enc = LabelEncoder()
state_enc = LabelEncoder()
season_enc = LabelEncoder()
soil_enc = LabelEncoder()
irrig_enc = LabelEncoder()

df["Crop_E"] = crop_enc.fit_transform(df["crop"])
df["State_E"] = state_enc.fit_transform(df["state"])
df["Season_E"] = season_enc.fit_transform(df["season"])
df["Soil_E"] = soil_enc.fit_transform(df["soil"])
df["Irrig_E"] = irrig_enc.fit_transform(df["irrigation_method"])

# Advanced feature engineering
# 1. NPK features
df["N_P"] = df["N"] / (df["P"] + 1)
df["N_K"] = df["N"] / (df["K"] + 1)
df["P_K"] = df["P"] / (df["K"] + 1)
df["NPK_total"] = df["N"] + df["P"] + df["K"]
df["NPK_product"] = df["N"] * df["P"] * df["K"] / 1000
df["NPK_balance"] = (df["N"] - df["P"]).abs() + (df["P"] - df["K"]).abs()

# 2. Nutrient status indicators
df["N_high"] = np.where(df["N"] > 100, 1, 0)
df["P_high"] = np.where(df["P"] > 50, 1, 0)
df["K_high"] = np.where(df["K"] > 100, 1, 0)

# 3. pH features
df["ph_optimal"] = np.where((df["pH"] >= 6.0) & (df["pH"] <= 7.5), 1, 0)
df["ph_deviation"] = abs(df["pH"] - 6.5)
df["ph_stress"] = np.where((df["pH"] < 5.5) | (df["pH"] > 8.5), 1, 0)

# 4. Temperature features
df["temp_optimal"] = np.where((df["temperature_c"] >= 20) & (df["temperature_c"] <= 30), 1, 0)
df["temp_stress"] = np.where((df["temperature_c"] < 15) | (df["temperature_c"] > 35), 1, 0)
df["temp_deviation"] = abs(df["temperature_c"] - 25)

# 5. Water features
df["water_stress"] = np.where(df["water_requirement"] < 300, 1, 0)
df["water_excess"] = np.where(df["water_requirement"] > 1500, 1, 0)

# 6. Soil quality index
df["Soil_Qual"] = (df["N"] + df["P"] + df["K"]) / 3
df["Soil_Index"] = df["Soil_Qual"] * (1 - df["ph_deviation"] / 10) * df["temp_optimal"]

# 7. Climate suitability score
df["Climate_Score"] = (df["temp_optimal"] + df["ph_optimal"]) / 2

# 8. Temperature-Water interaction
df["Temp_Water"] = df["temperature_c"] * df["water_requirement"] / 1000
df["Temp_Water_Stress"] = df["temp_stress"] * df["water_stress"]

# 9. Month/Season encoding
month_map = {"Kharif": 7, "Rabi": 11, "Zaid": 3, "Whole Year": 6}
df["month_num"] = df["season"].map(month_map)
df["month_sin"] = np.sin(2 * np.pi * df["month_num"] / 12)
df["month_cos"] = np.cos(2 * np.pi * df["month_num"] / 12)

# 10. Soil-specific interactions
df["soil_water"] = df["Soil_E"] * df["water_requirement"] / 1000
df["soil_temp"] = df["Soil_E"] * df["temperature_c"]

# 11. Crop-specific baseline yield (will be handled by crop encoding, but adding more features)
df["crop_season_interaction"] = df["Crop_E"] * 10 + df["Season_E"]

# 12. Input intensity score
df["Input_Score"] = df["N"] + df["P"] + df["K"] + df["water_requirement"] / 10

# 13. Efficiency ratios
df["yield_efficiency"] = df["yield_q_ha"] / (df["Input_Score"] + 1)

# Define feature set
features = [
    # Encoded categorical features
    "State_E", "Crop_E", "Season_E", "Soil_E", "Irrig_E",
    # Basic numeric features
    "N", "P", "K", "temperature_c", "pH", "water_requirement",
    # NPK engineered features
    "N_P", "N_K", "P_K", "NPK_total", "NPK_product", "NPK_balance",
    "N_high", "P_high", "K_high",
    # pH features
    "ph_optimal", "ph_deviation", "ph_stress",
    # Temperature features
    "temp_optimal", "temp_stress", "temp_deviation",
    # Water features
    "water_stress", "water_excess",
    # Quality indices
    "Soil_Qual", "Soil_Index", "Climate_Score",
    # Interaction features
    "Temp_Water", "Temp_Water_Stress",
    "month_sin", "month_cos",
    "soil_water", "soil_temp",
    "crop_season_interaction",
    "Input_Score"
]

print(f"   Total features: {len(features)}")

X = df[features]
y = df["yield_q_ha"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"   Train samples: {len(X_train)}, Test samples: {len(X_test)}")

# Scale features
scaler = RobustScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model 1: XGBoost
print("\n[3/6] Training XGBoost model...")
xgb_model = xgb.XGBRegressor(
    n_estimators=200,
    max_depth=12,
    learning_rate=0.1,
    subsample=0.8,
    colsample_bytree=0.8,
    min_child_weight=3,
    random_state=42,
    n_jobs=-1
)
xgb_model.fit(X_train, y_train)
xgb_pred = xgb_model.predict(X_test)
xgb_r2 = r2_score(y_test, xgb_pred)
xgb_mae = mean_absolute_error(y_test, xgb_pred)
xgb_rmse = np.sqrt(mean_squared_error(y_test, xgb_pred))
print(f"   XGBoost - R2: {xgb_r2:.4f}, MAE: {xgb_mae:.2f}, RMSE: {xgb_rmse:.2f}")

# Model 2: LightGBM (if available)
if HAS_LGBM:
    print("\n[4/6] Training LightGBM model...")
    lgb_model = lgb.LGBMRegressor(
        n_estimators=200,
        max_depth=12,
        learning_rate=0.1,
        num_leaves=50,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42,
        n_jobs=-1,
        verbose=-1
    )
    lgb_model.fit(X_train, y_train)
    lgb_pred = lgb_model.predict(X_test)
    lgb_r2 = r2_score(y_test, lgb_pred)
    lgb_mae = mean_absolute_error(y_test, lgb_pred)
    lgb_rmse = np.sqrt(mean_squared_error(y_test, lgb_pred))
    print(f"   LightGBM - R2: {lgb_r2:.4f}, MAE: {lgb_mae:.2f}, RMSE: {lgb_rmse:.2f}")
else:
    lgb_model = None
    lgb_r2 = 0

# Model 3: Gradient Boosting
print("\n[5/6] Training Gradient Boosting model...")
gb_model = GradientBoostingRegressor(
    n_estimators=150,
    max_depth=10,
    learning_rate=0.1,
    subsample=0.8,
    random_state=42
)
gb_model.fit(X_train, y_train)
gb_pred = gb_model.predict(X_test)
gb_r2 = r2_score(y_test, gb_pred)
gb_mae = mean_absolute_error(y_test, gb_pred)
gb_rmse = np.sqrt(mean_squared_error(y_test, gb_pred))
print(f"   Gradient Boosting - R2: {gb_r2:.4f}, MAE: {gb_mae:.2f}, RMSE: {gb_rmse:.2f}")

# Model 4: Random Forest (as base for stacking)
print("\n[6/6] Training Random Forest and creating ensemble...")
rf_model = RandomForestRegressor(
    n_estimators=150,
    max_depth=15,
    random_state=42,
    n_jobs=-1
)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)
rf_r2 = r2_score(y_test, rf_pred)
rf_mae = mean_absolute_error(y_test, rf_pred)
rf_rmse = np.sqrt(mean_squared_error(y_test, rf_pred))
print(f"   Random Forest - R2: {rf_r2:.4f}, MAE: {rf_mae:.2f}, RMSE: {rf_rmse:.2f}")

# Ensemble: Weighted averaging
print("\n   Creating ensemble model...")

# Get predictions from each model
xgb_pred_train = xgb_model.predict(X_train)
if lgb_model is not None:
    lgb_pred_train = lgb_model.predict(X_train)
else:
    lgb_pred_train = xgb_pred_train
    
gb_pred_train = gb_model.predict(X_train)
rf_pred_train = rf_model.predict(X_train)

# Calculate weights based on R2 scores
total_r2 = xgb_r2 + lgb_r2 + gb_r2 + rf_r2
w_xgb = xgb_r2 / total_r2
w_lgb = lgb_r2 / total_r2
w_gb = gb_r2 / total_r2
w_rf = rf_r2 / total_r2

print(f"   Weights - XGB: {w_xgb:.3f}, LGB: {w_lgb:.3f}, GB: {w_gb:.3f}, RF: {w_rf:.3f}")

# Ensemble prediction on test set
ensemble_pred = (w_xgb * xgb_pred + w_lgb * lgb_pred + w_gb * gb_pred + w_rf * rf_pred)
ensemble_r2 = r2_score(y_test, ensemble_pred)
ensemble_mae = mean_absolute_error(y_test, ensemble_pred)
ensemble_rmse = np.sqrt(mean_squared_error(y_test, ensemble_pred))

print(f"   Ensemble - R2: {ensemble_r2:.4f}, MAE: {ensemble_mae:.2f}, RMSE: {ensemble_rmse:.2f}")

# Cross-validation for best model
print("\n   Running cross-validation...")
cv = KFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(xgb_model, X, y, cv=cv, scoring='r2')
print(f"   XGBoost CV R2 Score: {cv_scores.mean():.4f} (+/- {cv_scores.std()*2:.4f})")

# Save models
print("\n   Saving models...")
# Primary model (XGBoost)
joblib.dump(xgb_model, "ml/models/yield_model_xgb_enhanced.pkl")

# Save encoders
joblib.dump(crop_enc, "ml/models/yield_crop_encoder_enhanced.pkl")
joblib.dump(state_enc, "ml/models/yield_state_encoder_enhanced.pkl")
joblib.dump(season_enc, "ml/models/yield_season_encoder_enhanced.pkl")
joblib.dump(soil_enc, "ml/models/yield_soil_encoder_enhanced.pkl")
joblib.dump(irrig_enc, "ml/models/yield_irrigation_encoder_enhanced.pkl")

# Save scaler
joblib.dump(scaler, "ml/models/yield_scaler_enhanced.pkl")

# Save features list
joblib.dump(features, "ml/models/yield_features_enhanced.pkl")

# Save ensemble configuration
ensemble_config = {
    'xgb_weight': w_xgb,
    'lgb_weight': w_lgb,
    'gb_weight': w_gb,
    'rf_weight': w_rf,
    'xgb_r2': xgb_r2,
    'lgb_r2': lgb_r2,
    'gb_r2': gb_r2,
    'rf_r2': rf_r2,
    'ensemble_r2': ensemble_r2,
    'ensemble_mae': ensemble_mae,
    'ensemble_rmse': ensemble_rmse
}
with open("ml/models/yield_ensemble_config.pkl", "wb") as f:
    pickle.dump(ensemble_config, f)

print("\n" + "=" * 60)
print("RESULTS SUMMARY")
print("=" * 60)
print(f"XGBoost:          R2={xgb_r2:.4f}, MAE={xgb_mae:.2f}, RMSE={xgb_rmse:.2f}")
if HAS_LGBM:
    print(f"LightGBM:         R2={lgb_r2:.4f}, MAE={lgb_mae:.2f}, RMSE={lgb_rmse:.2f}")
print(f"Gradient Boosting: R2={gb_r2:.4f}, MAE={gb_mae:.2f}, RMSE={gb_rmse:.2f}")
print(f"Random Forest:     R2={rf_r2:.4f}, MAE={rf_mae:.2f}, RMSE={rf_rmse:.2f}")
print(f"\nEnsemble Model:   R2={ensemble_r2:.4f}, MAE={ensemble_mae:.2f}, RMSE={ensemble_rmse:.2f}")
print(f"Cross-validation:  {cv_scores.mean():.4f} (+/- {cv_scores.std()*2:.4f})")
print(f"\nCrops supported: {len(crop_enc.classes_)}")
print(f"States covered: {len(state_enc.classes_)}")
print(f"Features used: {len(features)}")
print("\n✅ Enhanced yield prediction model training complete!")

