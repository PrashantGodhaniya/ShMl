import joblib
import pandas as pd
from datetime import datetime
import os

from src.data.monitoring.logging_system import log_prediction_event
from src.data.utils.encoder import encode_input

MODEL_PATH = "models/churn_model.pkl"
SCALER_PATH = "artifacts/scaler.pkl"
FEATURE_COLUMNS_PATH = "artifacts/feature_columns.pkl"
LOG_PATH = "logs/prediction_logs.csv"

# Load model and preprocessing artifacts
model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)
feature_columns = joblib.load(FEATURE_COLUMNS_PATH)


def preprocess_input(data):

    # convert categorical inputs like "Male", "Yes"
    data = encode_input(data)

    df = pd.DataFrame([data])

    # Ensure correct feature order used during training
    df = df.reindex(columns=feature_columns, fill_value=0)

    # Scale numeric features
    df[df.columns] = scaler.transform(df)

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

    # existing preprocessing pipeline
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