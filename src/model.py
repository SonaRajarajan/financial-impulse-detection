import numpy as np

def compute_weighted_risk(features):

    weights = {
        "DLI": 0.15,
        "EVSS": 0.20,
        "PDI": 0.15,
        "MICRO_CLUSTER": 0.10,
        "NIGHT_FLAG": 0.10,
        "WEEKEND_RATIO": 0.10
    }

    score = 0
    for k in weights:
        score += features[k] * weights[k]

    score = min(score * 20, 100)  # scale to 100
    return round(score, 2)