from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel

app = FastAPI()

model = joblib.load("models/impulse_model.pkl")

class Transaction(BaseModel):
    amount: float
    night_flag: int
    weekend_ratio: float
    micro_impulse: int
    emotional_volatility: float


@app.get("/")
def home():
    return {"message": "Impulse Detection API Running"}


@app.post("/predict")
def predict(tx: Transaction):

    data = pd.DataFrame([[
        tx.amount,
        tx.night_flag,
        tx.weekend_ratio,
        tx.micro_impulse,
        tx.emotional_volatility
    ]], columns=[
        "amount",
        "night_flag",
        "weekend_ratio",
        "micro_impulse",
        "emotional_volatility"
    ])

    prob = model.predict_proba(data)[0][1]
    risk_score = round(prob * 100, 2)

    return {
        "risk_score": risk_score
    }