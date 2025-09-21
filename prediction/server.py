from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load model
model = joblib.load("../train/forex_model.pkl")

# Init app
app = FastAPI()

@app.get("/predict")
def predict(ret_1: float, ret_3: float, ret_6: float, vol_roll: float, ma_diff: float):
    row = np.array([[ret_1, ret_3, ret_6, vol_roll, ma_diff]])
    proba = model.predict_proba(row)[0]
    probability = float(proba[1] if proba[1] > 0.5 else proba[0])
    return {
        "prediction": "buy" if proba[1] > 0.5 else "sell",
        "probability": probability
    }