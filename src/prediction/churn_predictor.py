def predict_churn_probability(
    input_df,
    churn_model
):

    probability = float(
        churn_model.predict_proba(
            input_df
        )[0][1]
    )

    return probability