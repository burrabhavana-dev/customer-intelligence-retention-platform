segment_mapping = {
    0: "Loyal Customers",
    1: "Premium Customers",
    2: "Growing Customers",
    3: "At-Risk High-Value Customers"
}


def get_customer_segment(
    input_df,
    scaler,
    kmeans_model
):

    segment_features = input_df[
        [
            "tenure",
            "MonthlyCharges",
            "TotalCharges",
            "RevenueScore"
        ]
    ]

    scaled_features = scaler.transform(
        segment_features
    )

    cluster = int(
        kmeans_model.predict(
            scaled_features
        )[0]
    )

    return segment_mapping[cluster]