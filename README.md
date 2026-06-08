# Fraud Detection for E-commerce and Banking Transactions

## Project Overview

This project builds an end-to-end fraud detection system for e-commerce and bank credit card transactions. The goal is to identify fraudulent transactions using machine learning while minimizing false positives and false negatives.

The system handles:

* E-commerce behavioral data with user/device/IP features
* Bank credit card data with anonymized PCA features

## Key Objectives

* Detect fraudulent transactions in imbalanced datasets
* Engineer behavioral, temporal, and geolocation-based features
* Train and compare multiple machine learning models
* Interpret model predictions using SHAP explainability

## Project Structure

fraud-detection/
├── notebooks/
├── data/
├── models/
├── src/
├── requirements.txt
└── README.md

## Workflow

1. Data Cleaning and EDA
2. IP-to-Country Geolocation Mapping
3. Feature Engineering
4. Handling Class Imbalance (SMOTE)
5. Model Training (Logistic Regression, Random Forest)
6. Model Evaluation (F1, AUC-PR, Confusion Matrix)
7. Model Explainability (SHAP)

## Models Used

* Logistic Regression (baseline)
* Random Forest (final model)

## Key Features

* time_since_signup
* device_transaction_count
* user_transaction_count
* ip_transaction_count
* hour_of_day
* day_of_week

## Evaluation Metrics

* Precision
* Recall
* F1 Score
* AUC-PR (primary metric)

## Results Summary

Random Forest outperformed Logistic Regression in balancing fraud detection and reducing false positives.

## Requirements

Install dependencies using:

```
pip install -r requirements.txt
```

## Author

Fraud Detection Project – Week 5–6 ML Challenge
