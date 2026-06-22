def assign_risk(probability):

    if probability >= 0.75:
        return "High"

    elif probability >= 0.50:
        return "Medium"

    return "Low"