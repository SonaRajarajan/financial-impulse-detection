import pandas as pd
import numpy as np

def engineer_features(df):

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["hour"] = df["timestamp"].dt.hour
    df["weekday"] = df["timestamp"].dt.weekday
    df["weekend"] = df["weekday"] >= 5

    # Night impulse
    df["night_flag"] = df["hour"].apply(lambda x: 1 if 1 <= x <= 4 else 0)

    # Micro impulse (< 300)
    df["micro_impulse"] = df["amount"].apply(lambda x: 1 if x < 300 else 0)

    # Emotional volatility
    user_mean = df.groupby("user_id")["amount"].transform("mean")
    user_std = df.groupby("user_id")["amount"].transform("std")

    df["emotional_volatility"] = abs(df["amount"] - user_mean) / (user_std + 1)

    # Weekend ratio per user
    weekend_spend = df[df["weekend"] == True].groupby("user_id")["amount"].sum()
    weekday_spend = df[df["weekend"] == False].groupby("user_id")["amount"].sum()

    ratio = (weekend_spend / (weekday_spend + 1)).reset_index()
    ratio.columns = ["user_id", "weekend_ratio"]

    df = df.merge(ratio, on="user_id", how="left")

    return df