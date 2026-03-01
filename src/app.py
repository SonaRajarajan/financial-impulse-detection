from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from behavioural_engine import compute_behavioural_features
from model import compute_weighted_risk
from nudges import generate_nudges

app = FastAPI()

class TransactionInput(BaseModel):
    transactions: list

@app.post("/predict")
def predict(data: TransactionInput):

    df = pd.DataFrame(data.transactions)
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    features = compute_behavioural_features(df)
    risk_score = compute_weighted_risk(features)
    nudges = generate_nudges(features)

    return {
        "risk_score": risk_score,
        "features": features,
        "nudges": nudges
    }