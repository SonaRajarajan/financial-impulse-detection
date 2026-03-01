import pandas as pd
import numpy as np
from datetime import timedelta

def calculate_dli(df):
    df = df.sort_values("timestamp")
    df["within_2hr"] = (
        df["timestamp"].diff() <= timedelta(hours=2)
    )
    return int(df["within_2hr"].rolling(3).sum().max() >= 3)


def calculate_evss(df):
    weekly_mean = df["amount"].mean()
    std = df["amount"].std() + 1
    current = df["amount"].iloc[-1]
    return abs(current - weekly_mean) / std


def calculate_pdi(df):
    salary_day = df[df["timestamp"].dt.day == 1]
    if salary_day.empty:
        return 0
    first_48 = df[df["timestamp"] <= salary_day["timestamp"].iloc[0] + timedelta(days=2)]
    return first_48["amount"].sum() / (df["amount"].mean() + 1)


def calculate_micro_cluster(df):
    small_tx = df[df["amount"] < 300]
    return len(small_tx)


def calculate_night_flag(df):
    night_tx = df[df["timestamp"].dt.hour.between(1,4)]
    return int(len(night_tx) > 0)


def calculate_weekend_ratio(df):
    weekend = df[df["timestamp"].dt.weekday >= 5]["amount"].sum()
    weekday = df[df["timestamp"].dt.weekday < 5]["amount"].sum()
    return weekend / (weekday + 1)