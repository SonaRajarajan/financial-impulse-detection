from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import pandas as pd
from sklearn.ensemble import IsolationForest

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- SCHEMA ----------------

class Expense(BaseModel):
    amount: float
    timestamp: str
    category: str

class AnalyzeRequest(BaseModel):
    expenses: List[Expense]
    period: str


# ---------------- ANALYZE ----------------

@app.post("/analyze")
def analyze(data: AnalyzeRequest):

    if len(data.expenses) < 3:
        return {"error": "Add at least 3 expenses"}

    # Create dataframe
    df = pd.DataFrame([{
        "amount": e.amount,
        "timestamp": pd.to_datetime(e.timestamp, dayfirst=True),
        "category": e.category
    } for e in data.expenses])

    df["hour"] = df["timestamp"].dt.hour
    df["day"] = df["timestamp"].dt.day
    df["weekday"] = df["timestamp"].dt.weekday

    mean_spend = df["amount"].mean()
    std_spend = df["amount"].std()

    # ---------------- BEHAVIOURAL SIGNALS ----------------

    df["is_night"] = (df["hour"] >= 21) | (df["hour"] <= 5)

    # 🔥 Improved Weekend Behaviour Logic
    df["is_weekend_pattern"] = (
        (df["weekday"] >= 5) |  # Saturday/Sunday
        ((df["weekday"] == 4) & (df["hour"] >= 18))  # Friday evening after 6PM
    )

    df["is_end_month"] = df["day"] > 25

    night_ratio = df["is_night"].mean()
    weekend_ratio = df["is_weekend_pattern"].mean()
    end_month_ratio = df["is_end_month"].mean()
    frequency_spike = len(df)

    # ---------------- ML IMPULSE ENGINE ----------------

    iso = IsolationForest(random_state=42)
    iso.fit(df[["amount"]])

    anomaly_scores = abs(iso.decision_function(df[["amount"]]))
    anomaly_score = anomaly_scores.mean()

    volatility_score = std_spend / (mean_spend + 1)
    frequency_score = len(df) / 10

    raw_score = (
        anomaly_score * 0.3 +
        volatility_score * 0.3 +
        frequency_score * 0.2 +
        night_ratio * 0.1 +
        weekend_ratio * 0.1
    )

    impulse_score = round(min(100, raw_score * 100), 2)

    # ---------------- SEVERITY ----------------

    if impulse_score > 70:
        severity = "High"
        banner_color = "red"
    elif impulse_score > 40:
        severity = "Medium"
        banner_color = "yellow"
    else:
        severity = "Low"
        banner_color = "green"

    # ---------------- BEHAVIOUR CLASSIFICATION ----------------

    if impulse_score > 70:
        detected_behavior = "High Impulse Financial Behaviour"
    elif std_spend > mean_spend * 0.8:
        detected_behavior = "High Volatility Spending Pattern"
    elif end_month_ratio > 0.6:
        detected_behavior = "End-of-Month Concentrated Spending"
    elif night_ratio > 0.4:
        detected_behavior = "Late-Night Emotional Spending"
    elif weekend_ratio > 0.4:
        detected_behavior = "Weekend-Oriented Spending Behaviour"
    else:
        detected_behavior = "Stable & Controlled Financial Behaviour"

    # ---------------- CONFIDENCE ----------------

    confidence = round(
        min(100, (
            anomaly_score * 50 +
            volatility_score * 30 +
            max(night_ratio, weekend_ratio, end_month_ratio) * 20
        ) * 100), 2
    )

    # ---------------- ML EXPLAINABILITY ----------------

    explainability = [
        f"Anomaly intensity score: {round(anomaly_score,3)}",
        f"Volatility contribution: {round(volatility_score,3)}",
        f"Frequency factor: {round(frequency_score,3)}",
        f"Night ratio contribution: {round(night_ratio,3)}",
        f"Weekend pattern contribution: {round(weekend_ratio,3)}"
    ]

    # ---------------- EXECUTIVE SUMMARY ----------------

    executive_summary = (
        f"The behavioural analysis indicates a {severity.lower()} risk pattern "
        f"classified as '{detected_behavior}'. "
        f"Spending volatility and behavioural timing patterns significantly influenced "
        f"the impulse risk score of {impulse_score}%. "
        f"The model confidence level for this assessment is {confidence}%."
    )

    # ---------------- ANALYSIS ----------------

    analysis = [
        f"Average transaction value: {round(mean_spend,2)}",
        f"Spending volatility: {round(std_spend,2)}",
        f"Transactions recorded: {frequency_spike}",
        f"{round(night_ratio*100,1)}% late-night spending",
        f"{round(weekend_ratio*100,1)}% weekend-oriented spending",
        f"{round(end_month_ratio*100,1)}% month-end concentration"
    ]

    # ---------------- SUGGESTIONS ----------------

    suggestions = []

    if severity == "High":
        suggestions.append("Implement strict behavioural spending controls.")
        suggestions.append("Enable automated transaction alerts.")

    if volatility_score > 0.5:
        suggestions.append("Adopt structured weekly budgeting.")

    if night_ratio > 0.4:
        suggestions.append("Avoid financial decisions after 9 PM.")

    if weekend_ratio > 0.4:
        suggestions.append("Predefine discretionary weekend budgets.")

    if end_month_ratio > 0.6:
        suggestions.append("Distribute expenses evenly across the month.")

    if not suggestions:
        suggestions.append("Maintain current disciplined financial behaviour.")

    features = {
        "mean_spend": round(mean_spend, 2),
        "std_spend": round(std_spend, 2),
        "night_ratio": round(night_ratio, 2),
        "weekend_ratio": round(weekend_ratio, 2),
        "end_month_ratio": round(end_month_ratio, 2),
        "frequency_spike": frequency_spike
    }

    return {
        "impulse_risk_score": impulse_score,
        "severity": severity,
        "confidence": confidence,
        "banner_color": banner_color,
        "detected_behavior": detected_behavior,
        "executive_summary": executive_summary,
        "explainability": explainability,
        "features": features,
        "analysis": analysis,
        "suggestions": suggestions
    }