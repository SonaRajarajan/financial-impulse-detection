import pandas as pd
import numpy as np

def compute_features(expenses, period="weekly"):

    if not expenses:
        return 0, "No Data", {}, ["Add expenses to analyze behaviour"]

    df = pd.DataFrame(expenses)

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["amount"] = df["amount"].astype(float)
    df = df.sort_values("timestamp")

    # ----------------------------
    # Dopamine Loop Index
    # ----------------------------
    df["time_diff"] = df["timestamp"].diff().dt.total_seconds() / 3600
    quick_spikes = df[df["time_diff"] <= 2]
    dli = min(len(quick_spikes) / 3, 1)

    # ----------------------------
    # Emotional Volatility
    # ----------------------------
    mean = df["amount"].mean()
    std = df["amount"].std() + 1e-6
    evss = abs(df["amount"].iloc[-1] - mean) / std

    # ----------------------------
    # End-of-month surge
    # ----------------------------
    df["day"] = df["timestamp"].dt.day
    end_month = df[df["day"] >= 25]["amount"].sum()
    monthly_avg = df["amount"].sum() / 30
    pdi = end_month / (monthly_avg + 1e-6)

    # ----------------------------
    # Micro impulse
    # ----------------------------
    micro = len(df[df["amount"] < 300]) / 5

    # ----------------------------
    # Weekend spike
    # ----------------------------
    df["weekday"] = df["timestamp"].dt.weekday
    weekend = df[df["weekday"] >= 5]["amount"].sum()
    weekday = df[df["weekday"] < 5]["amount"].sum()
    weekend_ratio = weekend / (weekday + 1e-6)

    # ----------------------------
    # Night spending
    # ----------------------------
    df["hour"] = df["timestamp"].dt.hour
    night = len(df[(df["hour"] >= 1) & (df["hour"] <= 4)]) / 3

    # ----------------------------
    # Risk prediction
    # ----------------------------
    multiplier = 1
    if period == "daily":
        multiplier = 1.5
    elif period == "monthly":
        multiplier = 0.8

    risk_score = min(
        100,
        round(multiplier * (
            20*dli +
            20*evss +
            15*pdi +
            10*micro +
            15*weekend_ratio +
            20*night
        ), 2)
    )

    profile = "Controlled Planner"
    if risk_score > 70:
        profile = "High Impulse Spender"
    elif weekend_ratio > 1.5:
        profile = "Social Influence Buyer"
    elif night > 0.5:
        profile = "Late Night Impulser"

    nudges = []

    if dli > 0.5:
        nudges.append("Frequent rapid purchases detected.")
    if night > 0.5:
        nudges.append("Late-night purchases increase impulse risk.")
    if pdi > 1.5:
        nudges.append("End-of-month surge detected.")
    if not nudges:
        nudges.append("Spending pattern appears stable.")

    features = {
        "DLI": round(dli,2),
        "EVSS": round(evss,2),
        "PDI": round(pdi,2),
        "MICRO": round(micro,2),
        "WEEKEND": round(weekend_ratio,2),
        "NIGHT": round(night,2),
    }

    return risk_score, profile, features, nudges