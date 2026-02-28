import os
from generate_data import generate_transactions
from train_model import train
from explain_model import explain

if __name__ == "__main__":

    print("Generating Dataset...")
    os.makedirs("data", exist_ok=True)
    df = generate_transactions()
    df.to_csv("data/synthetic_transactions.csv", index=False)

    print("Training Model...")
    train()

    print("Generating SHAP Explainability...")
    explain()

    print("Pipeline Completed Successfully.")