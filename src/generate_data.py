import numpy as np
import pandas as pd
import random
from datetime import datetime, timedelta
import os

np.random.seed(42)

NUM_USERS = 1000
MONTHS = 6
START_DATE = datetime(2024, 1, 1)

categories = [
    "Groceries", "Bills", "Food_Delivery", "Fashion",
    "Electronics", "Gaming", "Subscriptions", "Travel"
]

def generate_transactions():
    transactions = []

    for user in range(NUM_USERS):
        salary = np.random.randint(20000, 80000)
        base_daily_spend = salary / 30 * np.random.uniform(0.2, 0.4)

        for day in range(30 * MONTHS):
            date = START_DATE + timedelta(days=day)

            num_tx = np.random.poisson(1.5)

            for _ in range(num_tx):
                category = random.choice(categories)
                amount = np.random.normal(base_daily_spend, 200)

                # Impulse injection
                if category in ["Fashion", "Gaming", "Electronics"]:
                    if np.random.rand() < 0.2:
                        amount *= np.random.uniform(2, 4)

                hour = np.random.randint(0, 24)

                # Late night impulse
                if 1 <= hour <= 4 and np.random.rand() < 0.3:
                    amount *= 1.8

                transactions.append([
                    user,
                    date + timedelta(hours=hour),
                    category,
                    abs(amount)
                ])

    df = pd.DataFrame(transactions,
                      columns=["user_id", "timestamp", "category", "amount"])

    return df


if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    df = generate_transactions()
    df.to_csv("data/synthetic_transactions.csv", index=False)
    print("Dataset Generated.")