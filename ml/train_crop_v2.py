"""Fast Crop Recommendation Model Training - Optimized Version"""
import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import xgboost as xgb
import warnings
warnings.filterwarnings('ignore')

print("=" * 60)
print("Fast Crop Recommendation Model Training (v2)")
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

for col in ['N', 'P', 'K', 'pH', 'water_requirement']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df['temperature_c'] = df['temperature_c'].apply(convert_num)
df = df.dropna()

print(f"   Samples: {len(df)}, Crops: {df['crop'].nunique()}, States: {df['state'].nunique()}")

# Encode categoricals
print("\n[2/5] Encoding features...")
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

# Feature engineering
print("\n[3/5] Feature engineering...")

month_map = {"Kharif": 7, "Rabi": 11, "Zaid": 3, "Whole Year": 6}
df["month_num"] = df["season"].map(month_map)

df["NPK_total"] = df["N"] + df["P"] + df["K"]
df["N_ratio"] = df["N"] / (df["P"] + 1)
df["P_ratio"] = df["P"] / (df["K"] + 1)
df["temp_water"] = df["temperature_c"] * df["water_requirement"] / 1000
df["ph_deviation"] = abs(df["pH"] - 6.5)
df["month_sin"] = np.sin(2 * np.pi * df["month_num"] / 12)
df["month_cos"] = np.cos(2 * np.pi * df["month_num"] / 12)

features = [
    "N", "P", "K", "temperature_c", "pH", "water_requirement",
    "state_e", "season_e", "soil_e", "irrig_e",
    "NPK_total", "N_ratio", "P_ratio", "temp_water",
    "ph_deviation", "month_sin", "month_cos", "month_num"
]

print(f"   Features: {len(features)}")

X = df[features]
y = df["crop_e"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
print(f"   Train: {len(X_train)}, Test: {len(X_test)}")

print("\n[4/5] Training XGBoost...")
model = xgb.XGBClassifier(
    n_estimators=80,
    max_depth=8,
    learning_rate=0.15,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42,
    n_jobs=-1,
    use_label_encoder=False,
    eval_metric='mlogloss'
)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"   Accuracy: {acc:.4f}")

print("\n[5/5] Saving models...")
joblib.dump(model, "ml/models/crop_model_xgb_v2.pkl")
joblib.dump(state_enc, "ml/models/crop_state_encoder_v2.pkl")
joblib.dump(season_enc, "ml/models/crop_season_encoder_v2.pkl")
joblib.dump(soil_enc, "ml/models/crop_soil_encoder_v2.pkl")
joblib.dump(irrig_enc, "ml/models/crop_irrigation_encoder_v2.pkl")
joblib.dump(crop_enc, "ml/models/crop_encoder_v2.pkl")
joblib.dump(features, "ml/models/crop_features_v2.pkl")

print(f"\nDone! Crops: {len(crop_enc.classes_)}, States: {len(state_enc.classes_)}")
print(f"Accuracy: {acc:.4f}")

