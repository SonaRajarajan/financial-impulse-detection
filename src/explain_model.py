import shap
import joblib
import pandas as pd
import matplotlib.pyplot as plt
from feature_engineering import engineer_features

def explain():

    df = pd.read_csv("data/synthetic_transactions.csv")
    df = engineer_features(df)

    features = [
        "amount",
        "night_flag",
        "weekend_ratio",
        "micro_impulse",
        "emotional_volatility"
    ]

    X = df[features]

    model = joblib.load("models/impulse_model.pkl")

    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X)

    # Global summary
    shap.summary_plot(shap_values, X, show=False)
    plt.savefig("models/global_shap_summary.png")
    plt.close()

    # Feature importance
    shap.summary_plot(shap_values, X, plot_type="bar", show=False)
    plt.savefig("models/feature_importance.png")
    plt.close()

    print("SHAP explanations generated.")


if __name__ == "__main__":
    explain()