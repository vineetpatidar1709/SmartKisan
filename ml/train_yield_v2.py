"""Fast Yield Prediction Model Training - Optimized Version"""
import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score, mean_absolute_error
import xgboost as xgb
import warnings
warnings.filterwarnings('ignore')

print("=" * 60)
print("Fast Yield Prediction Model Training (v2)")
print("=" * 60)

# Load data
print("\n[1/5] Loading data...")
df = pd.read_csv("ml/augmented_crop_data_v8.csv")

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

for col in ['N', 'P', 'K', 'pH', 'water_requirement', 'yield_q_ha']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df['temperature_c'] = df['temperature_c'].apply(convert_num)
df = df.dropna()

print(f"   Samples: {len(df)}, Crops: {df['crop'].nunique()}")

# Encode categoricals
print("\n[2/5] Encoding features...")
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

# Feature engineering
print("\n[3/5] Feature engineering...")

month_map = {"Kharif": 7, "Rabi": 11, "Zaid": 3, "Whole Year": 6}
df["month_num"] = df["season"].map(month_map)

df["N_P"] = df["N"] / (df["P"] + 1)
df["N_K"] = df["N"] / (df["K"] + 1)
df["Temp_Water"] = df["temperature_c"] * df["water_requirement"] / 100
df["Soil_Qual"] = (df["N"] + df["P"] + df["K"]) / 3

df["month_sin"] = np.sin(2 * np.pi * df["month_num"] / 12)
df["month_cos"] = np.cos(2 * np.pi * df["month_num"] / 12)

features = [
    "State_E", "Crop_E", "Season_E", "Soil_E", "Irrig_E",
    "N", "P", "K", "temperature_c", "pH", "water_requirement",
    "month_num", "N_P", "N_K", "Temp_Water", "Soil_Qual",
    "month_sin", "month_cos"
]

print(f"   Features: {len(features)}")

X = df[features]
y = df["yield_q_ha"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"   Train: {len(X_train)}, Test: {len(X_test)}")

print("\n[4/5] Training XGBoost...")
model = xgb.XGBRegressor(
    n_estimators=100,
    max_depth=12,
    learning_rate=0.1,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42,
    n_jobs=-1
)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
print(f"   R2: {r2:.4f}, MAE: {mae:.2f}")

print("\n[5/5] Saving models...")
joblib.dump(model, "ml/models/yield_model_xgb_v2.pkl")
joblib.dump(crop_enc, "ml/models/yield_crop_encoder_v2.pkl")
joblib.dump(state_enc, "ml/models/yield_state_encoder_v2.pkl")
joblib.dump(season_enc, "ml/models/yield_season_encoder_v2.pkl")
joblib.dump(soil_enc, "ml/models/yield_soil_encoder_v2.pkl")
joblib.dump(irrig_enc, "ml/models/yield_irrigation_encoder_v2.pkl")
joblib.dump(features, "ml/models/yield_features_v2.pkl")

print(f"\nDone! Crops: {len(crop_enc.classes_)}, States: {len(state_enc.classes_)}")
print(f"R2: {r2:.4f}, MAE: {mae:.2f}")

