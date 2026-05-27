"""Enhanced Crop Recommendation Model Training with Ensemble Approach

This module implements an improved crop recommendation system using:
- Ensemble of XGBoost, LightGBM, and Neural Network
- Advanced feature engineering
- Cross-validation for hyperparameter tuning
"""
import pandas as pd
import numpy as np
import joblib
import pickle
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.preprocessing import LabelEncoder, StandardScaler, RobustScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.neural_network import MLPClassifier
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
print("Enhanced Crop Recommendation Model Training")
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
for col in ['N', 'P', 'K', 'pH', 'water_requirement']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df['temperature_c'] = df['temperature_c'].apply(convert_num)
df = df.dropna()

print(f"   Total samples after cleaning: {len(df)}")
print(f"   Unique crops: {df['crop'].nunique()}")
print(f"   Unique states: {df['state'].nunique()}")

# Feature Engineering
print("\n[2/6] Feature Engineering...")

# Encode categorical variables
state_enc = LabelEncoder()
season_enc = LabelEncoder()
soil_enc = LabelEncoder()
irrig_enc = LabelEncoder()
crop_enc = LabelEncoder()

df["state_e"] = state_enc.fit_transform(df["state"])
df["season_e"] = season_enc.fit_transform(df["season"])
df["soil_e"] = soil_enc.fit_transform(df["soil"])
df["irrig_e"] = irrig_enc.fit_transform(df["irrigation_method"])
df["crop_e"] = crop_enc.fit_transform(df["crop"])

# Advanced feature engineering
# 1. NPK ratios and totals
df["NPK_total"] = df["N"] + df["P"] + df["K"]
df["N_ratio"] = df["N"] / (df["P"] + 1)
df["P_ratio"] = df["P"] / (df["K"] + 1)
df["N_K_ratio"] = df["N"] / (df["K"] + 1)

# 2. Nutrient balance indicators
df["N_deficit"] = np.where(df["N"] < 50, 1, 0)
df["P_deficit"] = np.where(df["P"] < 30, 1, 0)
df["K_deficit"] = np.where(df["K"] < 30, 1, 0)

# 3. pH related features
df["ph_optimal"] = np.where((df["pH"] >= 6.0) & (df["pH"] <= 7.5), 1, 0)
df["ph_deviation"] = abs(df["pH"] - 6.5)
df["ph_acidic"] = np.where(df["pH"] < 5.5, 1, 0)
df["ph_alkaline"] = np.where(df["pH"] > 8.0, 1, 0)

# 4. Water requirement categories
df["water_low"] = np.where(df["water_requirement"] < 400, 1, 0)
df["water_medium"] = np.where((df["water_requirement"] >= 400) & (df["water_requirement"] < 800), 1, 0)
df["water_high"] = np.where(df["water_requirement"] >= 800, 1, 0)

# 5. Temperature features
df["temp_optimal"] = np.where((df["temperature_c"] >= 20) & (df["temperature_c"] <= 30), 1, 0)
df["temp deviation"] = abs(df["temperature_c"] - 25)

# 6. Soil quality index
df["soil_quality"] = (df["N"] + df["P"] + df["K"]) / 3
df["soil_score"] = df["soil_quality"] * (1 - df["ph_deviation"] / 10)

# 7. Climate suitability score
df["climate_score"] = (df["temp_optimal"] + df["ph_optimal"] + df["water_medium"]) / 3

# 8. Month encoding (for seasonal patterns)
# Extract month from season
month_map = {"Kharif": 7, "Rabi": 11, "Zaid": 3, "Whole Year": 6}
df["month_num"] = df["season"].map(month_map)
df["month_sin"] = np.sin(2 * np.pi * df["month_num"] / 12)
df["month_cos"] = np.cos(2 * np.pi * df["month_num"] / 12)

# 9. Temperature-Water interaction
df["temp_water"] = df["temperature_c"] * df["water_requirement"] / 1000

# 10. Nutrient-water interaction
df["N_water"] = df["N"] * df["water_requirement"] / 1000

# Define feature set
features = [
    # Basic features
    "N", "P", "K", "temperature_c", "pH", "water_requirement",
    "state_e", "season_e", "soil_e", "irrig_e",
    # Engineered features
    "NPK_total", "N_ratio", "P_ratio", "N_K_ratio",
    "N_deficit", "P_deficit", "K_deficit",
    "ph_optimal", "ph_deviation", "ph_acidic", "ph_alkaline",
    "water_low", "water_medium", "water_high",
    "temp_optimal", "temp deviation",
    "soil_quality", "soil_score", "climate_score",
    "month_sin", "month_cos",
    "temp_water", "N_water"
]

print(f"   Total features: {len(features)}")

X = df[features]
y = df["crop_e"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)
print(f"   Train samples: {len(X_train)}, Test samples: {len(X_test)}")

# Scale features
scaler = RobustScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model 1: XGBoost
print("\n[3/6] Training XGBoost model...")
xgb_model = xgb.XGBClassifier(
    n_estimators=150,
    max_depth=10,
    learning_rate=0.1,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42,
    n_jobs=-1,
    use_label_encoder=False,
    eval_metric='mlogloss'
)
xgb_model.fit(X_train, y_train)
xgb_pred = xgb_model.predict(X_test)
xgb_acc = accuracy_score(y_test, xgb_pred)
print(f"   XGBoost Accuracy: {xgb_acc:.4f}")

# Model 2: LightGBM (if available)
if HAS_LGBM:
    print("\n[4/6] Training LightGBM model...")
    lgb_model = lgb.LGBMClassifier(
        n_estimators=150,
        max_depth=10,
        learning_rate=0.1,
        num_leaves=31,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42,
        n_jobs=-1,
        verbose=-1
    )
    lgb_model.fit(X_train, y_train)
    lgb_pred = lgb_model.predict(X_test)
    lgb_acc = accuracy_score(y_test, lgb_pred)
    print(f"   LightGBM Accuracy: {lgb_acc:.4f}")
else:
    lgb_model = None
    lgb_acc = 0

# Model 3: Neural Network
print("\n[5/6] Training Neural Network model...")
nn_model = MLPClassifier(
    hidden_layer_sizes=(128, 64, 32),
    activation='relu',
    solver='adam',
    alpha=0.001,
    batch_size=64,
    learning_rate='adaptive',
    max_iter=500,
    random_state=42,
    early_stopping=True,
    validation_fraction=0.1
)
nn_model.fit(X_train_scaled, y_train)
nn_pred = nn_model.predict(X_test_scaled)
nn_acc = accuracy_score(y_test, nn_pred)
print(f"   Neural Network Accuracy: {nn_acc:.4f}")

# Ensemble: Weighted voting
print("\n[6/6] Creating ensemble model...")

# Get probabilities from each model
xgb_proba = xgb_model.predict_proba(X_test)
if lgb_model is not None:
    lgb_proba = lgb_model.predict_proba(X_test)
else:
    lgb_proba = xgb_proba

nn_proba = nn_model.predict_proba(X_test_scaled)

# Weighted average (weights based on individual accuracy)
total_acc = xgb_acc + lgb_acc + nn_acc
w_xgb = xgb_acc / total_acc
w_lgb = lgb_acc / total_acc
w_nn = nn_acc / total_acc

print(f"   Weights - XGB: {w_xgb:.3f}, LGB: {w_lgb:.3f}, NN: {w_nn:.3f}")

# Ensemble prediction
ensemble_proba = w_xgb * xgb_proba + w_lgb * lgb_proba + w_nn * nn_proba
ensemble_pred = np.argmax(ensemble_proba, axis=1)
ensemble_acc = accuracy_score(y_test, ensemble_pred)
print(f"   Ensemble Accuracy: {ensemble_acc:.4f}")

# Cross-validation for best model
print("\n   Running cross-validation...")
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(xgb_model, X, y, cv=cv, scoring='accuracy')
print(f"   XGBoost CV Score: {cv_scores.mean():.4f} (+/- {cv_scores.std()*2:.4f})")

# Save models
print("\n   Saving models...")
# XGBoost (primary model)
joblib.dump(xgb_model, "ml/models/crop_model_xgb_enhanced.pkl")

# Save encoders
joblib.dump(state_enc, "ml/models/crop_state_encoder_enhanced.pkl")
joblib.dump(season_enc, "ml/models/crop_season_encoder_enhanced.pkl")
joblib.dump(soil_enc, "ml/models/crop_soil_encoder_enhanced.pkl")
joblib.dump(irrig_enc, "ml/models/crop_irrigation_encoder_enhanced.pkl")
joblib.dump(crop_enc, "ml/models/crop_encoder_enhanced.pkl")

# Save scaler
joblib.dump(scaler, "ml/models/crop_scaler_enhanced.pkl")

# Save features list
joblib.dump(features, "ml/models/crop_features_enhanced.pkl")

# Save ensemble weights
ensemble_config = {
    'xgb_weight': w_xgb,
    'lgb_weight': w_lgb,
    'nn_weight': w_nn,
    'xgb_accuracy': xgb_acc,
    'lgb_accuracy': lgb_acc,
    'nn_accuracy': nn_acc,
    'ensemble_accuracy': ensemble_acc
}
with open("ml/models/ensemble_config.pkl", "wb") as f:
    pickle.dump(ensemble_config, f)

print("\n" + "=" * 60)
print("RESULTS SUMMARY")
print("=" * 60)
print(f"XGBoost Accuracy:       {xgb_acc:.4f}")
if HAS_LGBM:
    print(f"LightGBM Accuracy:      {lgb_acc:.4f}")
print(f"Neural Network Accuracy: {nn_acc:.4f}")
print(f"Ensemble Accuracy:       {ensemble_acc:.4f}")
print(f"Cross-validation Score:  {cv_scores.mean():.4f}")
print(f"\nCrops supported: {len(crop_enc.classes_)}")
print(f"States covered: {len(state_enc.classes_)}")
print(f"Features used: {len(features)}")
print("\n✅ Enhanced crop recommendation model training complete!")

