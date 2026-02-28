import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score
import xgboost as xgb
import joblib
from feature_engineering import engineer_features

def train():

    df = pd.read_csv("data/synthetic_transactions.csv")
    df = engineer_features(df)

    # Label logic
    df["impulse_label"] = (
        (df["emotional_volatility"] > 2.5) |
        (df["night_flag"] == 1) |
        (df["micro_impulse"] == 1)
    ).astype(int)

    features = [
        "amount",
        "night_flag",
        "weekend_ratio",
        "micro_impulse",
        "emotional_volatility"
    ]

    X = df[features]
    y = df["impulse_label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = xgb.XGBClassifier(
        n_estimators=200,
        max_depth=6,
        learning_rate=0.05,
        eval_metric="logloss"
    )

    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    probs = model.predict_proba(X_test)[:, 1]

    print(classification_report(y_test, preds))
    print("ROC AUC:", roc_auc_score(y_test, probs))

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/impulse_model.pkl")

    return model, X


if __name__ == "__main__":
    train()