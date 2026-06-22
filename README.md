# Customer Intelligence & Retention Platform

## Overview

Customer Intelligence & Retention Platform is an end-to-end AI-powered application designed to help businesses identify customer churn risk, segment customers based on value and behavior, and generate actionable retention recommendations.

The platform combines machine learning, customer segmentation, explainable AI, REST APIs, and an interactive dashboard to support proactive customer retention strategies.

---

## Business Problem

Customer churn directly impacts revenue and customer lifetime value.

Traditional churn prediction systems only indicate whether a customer is likely to leave.

This platform goes beyond prediction by:

* Predicting churn probability
* Classifying customer risk levels
* Segmenting customers into business-relevant groups
* Generating personalized retention recommendations
* Providing explainable AI insights

---

## Features

### Churn Prediction Engine

* Logistic Regression based churn prediction
* Probability-based risk assessment
* Model benchmarking using Random Forest and XGBoost

### Customer Segmentation Engine

* K-Means clustering
* Premium Customers
* Loyal Customers
* Growing Customers
* At-Risk High-Value Customers

### Risk Classification

* High Risk
* Medium Risk
* Low Risk

### Retention Recommendation Engine

* Personalized customer retention actions
* Segment-aware recommendations
* Risk-based intervention strategies

### Explainable AI

* SHAP feature importance
* Customer-level prediction explanations

### FastAPI Backend

* REST API endpoints
* Pydantic validation
* Real-time predictions

### Streamlit Dashboard

* Interactive customer input form
* Real-time predictions
* Business-friendly visual interface

---

## Technology Stack

* Python
* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* SHAP
* FastAPI
* Streamlit
* Joblib

---

## Model Performance

| Model               | Accuracy | ROC-AUC |
| ------------------- | -------- | ------- |
| Logistic Regression | 80.48%   | 84.64%  |
| Random Forest       | 80.06%   | 83.98%  |
| XGBoost             | 79.13%   | 83.87%  |

Logistic Regression was selected as the production model based on overall performance and interpretability.

---

## Project Architecture

Customer Data → Feature Engineering → Churn Prediction → Risk Classification → Customer Segmentation → Recommendation Engine → FastAPI → Streamlit Dashboard

---

## Future Enhancements

* Customer Lifetime Value Prediction
* RAG-powered Customer Support Insights
* Real-time Event Streaming
* Docker Deployment
* Cloud Deployment (AWS/Azure)
