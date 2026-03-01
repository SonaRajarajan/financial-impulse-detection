def generate_nudges(features):

    nudges = []

    if features["NIGHT_FLAG"]:
        nudges.append("You tend to spend after midnight. Consider a 12AM spending lock.")

    if features["MICRO_CLUSTER"] > 5:
        nudges.append("Frequent small purchases are accumulating significantly.")

    if features["PDI"] > 2:
        nudges.append("High spending immediately after salary credit detected.")

    if features["EVSS"] > 2:
        nudges.append("Your spending deviates strongly from your normal pattern.")

    return nudges