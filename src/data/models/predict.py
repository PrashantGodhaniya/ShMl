import pandas as pd
import joblib
import os
from src.data.monitoring.logging_system import log_prediction_event

MODEL_PATH = "models/churn_model.pkl"
DATA_PATH = "data/processed/processed_churn.csv"


def load_model():
    """
    Load the trained churn model
    """
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("Trained model not found. Run train.py first.")

    model = joblib.load(MODEL_PATH)
    return model


def load_data():
    """
    Load processed dataset
    """
    df = pd.read_csv(DATA_PATH)
    return df


def make_predictions(model, df):
    """
    Generate churn predictions
    """

    X = df.drop("Churn", axis=1)

    predictions = model.predict(X)
    log_prediction_event("Prediction generated for telecom customer")q
    probabilities = model.predict_proba(X)[:, 1]

    results = df.copy()
    results["predicted_churn"] = predictions
    results["churn_probability"] = probabilities

    return results


def main():

    print("Loading model...")
    model = load_model()

    print("Loading processed data...")
    df = load_data()

    print("Generating predictions...")
    results = make_predictions(model, df)

    print(results[["predicted_churn", "churn_probability"]].head())


if __name__ == "__main__":
    main()