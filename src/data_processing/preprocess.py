import pandas as pd


def load_data(path):
    return pd.read_csv(path)


def clean_total_charges(df):

    df["TotalCharges"] = df["TotalCharges"].replace(" ", pd.NA)

    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"],
        errors="coerce"
    )

    return df


def handle_missing_values(df):

    df["TotalCharges"] = df["TotalCharges"].fillna(
        df["TotalCharges"].median()
    )

    return df


def drop_unnecessary_columns(df):

    return df.drop(
        columns=["customerID"]
    )
if __name__ == "__main__":

    df = load_data(
        "data/WA_Fn-UseC_-Telco-Customer-Churn.csv"
    )

    print(df.head())