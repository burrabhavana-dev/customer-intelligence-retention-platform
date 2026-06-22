import streamlit as st
import requests

st.title("Customer Intelligence & Retention Platform")

st.subheader("Customer Information")

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

senior = st.selectbox(
    "Senior Citizen",
    [0, 1]
)

partner = st.selectbox(
    "Partner",
    ["Yes", "No"]
)

dependents = st.selectbox(
    "Dependents",
    ["Yes", "No"]
)

tenure = st.number_input(
    "Tenure",
    min_value=0
)

phone_service = st.selectbox(
    "Phone Service",
    ["Yes", "No"]
)

multiple_lines = st.selectbox(
    "Multiple Lines",
    ["Yes", "No", "No phone service"]
)

internet_service = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

online_security = st.selectbox(
    "Online Security",
    ["Yes", "No"]
)

online_backup = st.selectbox(
    "Online Backup",
    ["Yes", "No"]
)

device_protection = st.selectbox(
    "Device Protection",
    ["Yes", "No"]
)

tech_support = st.selectbox(
    "Tech Support",
    ["Yes", "No"]
)

streaming_tv = st.selectbox(
    "Streaming TV",
    ["Yes", "No"]
)

streaming_movies = st.selectbox(
    "Streaming Movies",
    ["Yes", "No"]
)

contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

paperless = st.selectbox(
    "Paperless Billing",
    ["Yes", "No"]
)

payment_method = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0
)

total_charges = st.number_input(
    "Total Charges",
    min_value=0.0
)

revenue_score = st.number_input(
    "Revenue Score",
    min_value=0.0
)

avg_monthly_spend = st.number_input(
    "Average Monthly Spend",
    min_value=0.0
)

tenure_group = st.selectbox(
    "Tenure Group",
    [
        "New",
        "Established",
        "Loyal"
    ]
)

if st.button("Predict"):

    payload = {
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,
        "RevenueScore": revenue_score,
        "AvgMonthlySpend": avg_monthly_spend,
        "TenureGroup": tenure_group
    }

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=payload
    )

    result = response.json()

    st.success("Prediction Complete")

    st.metric(
        "Churn Probability",
        result["churn_probability"]
    )

    st.metric(
        "Risk Level",
        result["risk_level"]
    )

    st.metric(
        "Customer Segment",
        result["customer_segment"]
    )

    st.write(
        "Recommendation:"
    )

    st.info(
        result["recommendation"]
    )