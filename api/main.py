from fastapi import FastAPI
from api.schemas import CustomerRequest

import pandas as pd
import joblib

from src.prediction.churn_predictor import (
    predict_churn_probability
)

from src.risk.risk_engine import (
    assign_risk
)

from src.segmentation.customer_segmentation import (
    get_customer_segment
)

from src.recommendations.recommendation_engine import (
    get_recommendation
)

app = FastAPI(
    title="Customer Intelligence Platform"
)

churn_model = joblib.load(
    "models/churn_model.pkl"
)

kmeans_model = joblib.load(
    "models/kmeans_model.pkl"
)

segment_scaler = joblib.load(
    "models/segment_scaler.pkl"
)


@app.get("/")
def home():

    return {
        "message":
        "Customer Intelligence & Retention Platform API"
    }


@app.post("/predict")
def predict(
    customer: CustomerRequest
):

    customer_dict = (
        customer.model_dump()
    )

    input_df = pd.DataFrame(
        [customer_dict]
    )

    churn_probability = (
        predict_churn_probability(
            input_df,
            churn_model
        )
    )

    risk_level = assign_risk(
        churn_probability
    )

    customer_segment = (
        get_customer_segment(
            input_df,
            segment_scaler,
            kmeans_model
        )
    )

    recommendation = (
        get_recommendation(
            customer_segment,
            risk_level
        )
    )

    return {

        "churn_probability":
            round(
                churn_probability,
                4
            ),

        "risk_level":
            risk_level,

        "customer_segment":
            customer_segment,

        "recommendation":
            recommendation
    }