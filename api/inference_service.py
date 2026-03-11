import joblib
import pandas as pd
from datetime import datetime
import os
from src.data.monitoring.logging_system import log_prediction_event

MODEL_PATH = "models/churn_model.pkl"
LOG_PATH = "logs/prediction_logs.csv"

model = joblib.load(MODEL_PATH)


def preprocess_input(data):

    df = pd.DataFrame([data])

    # convert categorical columns
    categorical_cols = df.select_dtypes(include="object").columns

    df = pd.get_dummies(df, columns=categorical_cols)

    return df


def log_prediction(prediction, probability):

    os.makedirs("logs", exist_ok=True)

    log_data = {
        "timestamp": datetime.now(),
        "prediction": prediction,
        "probability": probability
    }

    log_df = pd.DataFrame([log_data])

    if os.path.exists(LOG_PATH):
        log_df.to_csv(LOG_PATH, mode="a", header=False, index=False)
    else:
        log_df.to_csv(LOG_PATH, index=False)


def predict_single(data):

    df = preprocess_input(data)

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    log_prediction(prediction, probability)
    log_prediction_event(f"Prediction generated: {prediction}, probability: {probability}")

    return {
        "prediction": int(prediction),
        "churn": "Yes" if prediction == 1 else "No",
        "probability": float(probability)
    }