"""Crop Recommendation Model Training"""
import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score
import xgboost as xgb
import warnings
warnings.filterwarnings('ignore')

print("Training Crop Model...")
df = pd.read_csv("ml/augmented_crop_data_v8.csv")

def convert_num(val):
    if isinstance(val, str) and '-' in val:
        parts = val.split('-')
        try: return (float(parts[0]) + float(parts[1])) / 2
        except: return np.nan
    try: return float(val)
    except: return np.nan

for col in ['N', 'P', 'K', 'pH', 'water_requirement']:
    df[col] = pd.to_numeric(df[col], errors='coerce')
df['temperature_c'] = df['temperature_c'].apply(convert_num)
df = df.dropna()

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

features = ["N", "P", "K", "temperature_c", "pH", "water_requirement", "state_e", "season_e", "soil_e", "irrig_e"]
X = df[features]
y = df["crop_e"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
print(f"Train: {len(X_train)}, Test: {len(X_test)}")

model = xgb.XGBClassifier(n_estimators=60, max_depth=8, learning_rate=0.15, random_state=42, n_jobs=-1, use_label_encoder=False, eval_metric='mlogloss')
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")

joblib.dump(model, "ml/models/crop_model.pkl")
joblib.dump(state_enc, "ml/models/state_encoder.pkl")
joblib.dump(season_enc, "ml/models/season_encoder.pkl")
joblib.dump(soil_enc, "ml/models/soil_encoder.pkl")
joblib.dump(irrig_enc, "ml/models/irrigation_encoder.pkl")
joblib.dump(crop_enc, "ml/models/crop_encoder.pkl")
joblib.dump(features, "ml/models/feature_columns.pkl")

scaler = StandardScaler()
scaler.fit(X)
joblib.dump(scaler, "ml/models/scaler.pkl")

print(f"Done! Crops: {len(crop_enc.classes_)}, States: {len(state_enc.classes_)}")

