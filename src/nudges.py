def generate_nudge(row):

    if row["night_flag"] == 1:
        return "You tend to spend late at night. Consider a midnight spending cap."

    if row["micro_impulse"] == 1:
        return "Frequent small purchases are adding up. Try a weekly micro-spend limit."

    if row["emotional_volatility"] > 3:
        return "This purchase deviates significantly from your normal spending."

    return "Your spending pattern looks stable."