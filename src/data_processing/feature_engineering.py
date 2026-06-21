def create_tenure_group(df):
    
    bins = [0, 12, 24, 48, 72]

    labels = [
        "New",
        "Growing",
        "Established",
        "Loyal"
    ]

    df["TenureGroup"] = pd.cut(
        df["tenure"],
        bins=bins,
        labels=labels
    )

    return df
def create_revenue_score(df):

    df["RevenueScore"] = (
        df["MonthlyCharges"] * df["tenure"]
    )

    return df
def create_avg_monthly_spend(df):

    df["AvgMonthlySpend"] = (
        df["TotalCharges"] /
        (df["tenure"] + 1)
    )

    return df