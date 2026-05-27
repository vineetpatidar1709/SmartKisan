"""Yield Prediction Model Training"""
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error
import warnings
warnings.filterwarnings('ignore')

print("Training Yield Model...")
df = pd.read_csv("ml/augmented_crop_data_v8.csv")

def convert_num(val):
    if isinstance(val, str) and '-' in val:
        parts = val.split('-')
        try: return (float(parts[0]) + float(parts[1])) / 2
        except: return np.nan
    try: return float(val)
    except: return np.nan

for col in ['N', 'P', 'K', 'pH', 'water_requirement', 'yield_q_ha']:
    df[col] = pd.to_numeric(df[col], errors='coerce')
df['temperature_c'] = df['temperature_c'].apply(convert_num)
df = df.dropna()

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

df["N_P"] = df["N"] / (df["P"] + 1)
df["N_K"] = df["N"] / (df["K"] + 1)
df["Temp_Water"] = df["temperature_c"] * df["water_requirement"] / 100
df["Soil_Qual"] = (df["N"] + df["P"] + df["K"]) / 3

features = ["State_E", "Crop_E", "Season_E", "Soil_E", "Irrig_E", "N", "P", "K", "temperature_c", "pH", "water_requirement", "N_P", "N_K", "Temp_Water", "Soil_Qual"]
X = df[features]
y = df["yield_q_ha"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
print(f"Train: {len(X_train)}, Test: {len(X_test)}")

model = RandomForestRegressor(n_estimators=120, max_depth=15, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(f"R2: {r2_score(y_test, y_pred):.4f}, MAE: {mean_absolute_error(y_test, y_pred):.4f}")

with open("ml/models/yield_model.pkl", "wb") as f:
    pickle.dump(model, f)
with open("ml/models/yield_scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)
with open("ml/models/yield_crop_encoder.pkl", "wb") as f:
    pickle.dump(crop_enc, f)
with open("ml/models/yield_state_encoder.pkl", "wb") as f:
    pickle.dump(state_enc, f)
with open("ml/models/yield_season_encoder.pkl", "wb") as f:
    pickle.dump(season_enc, f)
with open("ml/models/yield_soil_encoder.pkl", "wb") as f:
    pickle.dump(soil_enc, f)
with open("ml/models/yield_irrigation_encoder.pkl", "wb") as f:
    pickle.dump(irrig_enc, f)
with open("ml/models/yield_features.pkl", "wb") as f:
    pickle.dump(features, f)

print(f"Done! Crops: {len(crop_enc.classes_)}, States: {len(state_enc.classes_)}")

