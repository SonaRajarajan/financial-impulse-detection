import pandas as pd
from feature_engineering import *

def compute_behavioural_features(df):

    features = {
        "DLI": calculate_dli(df),
        "EVSS": calculate_evss(df),
        "PDI": calculate_pdi(df),
        "MICRO_CLUSTER": calculate_micro_cluster(df),
        "NIGHT_FLAG": calculate_night_flag(df),
        "WEEKEND_RATIO": calculate_weekend_ratio(df),
    }

    return features