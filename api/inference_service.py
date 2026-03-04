import joblib
import pandas as pd

MODEL_PATH = "models/churn_model.pkl"

model = joblib.load(MODEL_PATH)


def predict_single(customer):

    df = pd.DataFrame([customer])

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    return {
        "prediction": int(prediction),
        "churn_probability": float(probability)
    }


def predict_batch(customers):

    df = pd.DataFrame(customers)

    predictions = model.predict(df)
    probabilities = model.predict_proba(df)[:, 1]

    results = []

    for pred, prob in zip(predictions, probabilities):

        results.append({
            "prediction": int(pred),
            "churn_probability": float(prob)
        })

    return results