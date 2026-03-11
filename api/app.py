import os
from fastapi import FastAPI
from api.schema import CustomerData, BatchCustomerData
from api.inference_service import predict_single

app = FastAPI(
    title="Customer Churn Prediction API",
    description="Self-Healing MLOps Churn Prediction System",
    version="1.0"
)


@app.get("/")
def health_check():
    return {"status": "API running"}


# -------- NEW MODEL INFO ENDPOINT --------
@app.get("/model-info")
def model_info():

    return {
        "model_name": "RandomForest Churn Model",
        "version": "1.0",
        "framework": "scikit-learn",
        "features": 19,
        "author": "PrashantGodhaniya"
    }

@app.get("/monitoring")
def monitoring():

    prediction_log_file = "logs/predictions.log"
    drift_log_file = "logs/drift.log"
    retrain_log_file = "logs/retraining.log"

    prediction_logs = 0
    drift_events = 0
    retraining_events = 0

    if os.path.exists(prediction_log_file):
        with open(prediction_log_file) as f:
            prediction_logs = len(f.readlines())

    if os.path.exists(drift_log_file):
        with open(drift_log_file) as f:
            drift_events = len(f.readlines())

    if os.path.exists(retrain_log_file):
        with open(retrain_log_file) as f:
            retraining_events = len(f.readlines())

    return {
        "prediction_logs": prediction_logs,
        "drift_events": drift_events,
        "retraining_events": retraining_events,
        "status": "healthy"
    }

# -------- SINGLE PREDICTION --------
@app.post("/predict")
def predict(customer: CustomerData):

    result = predict_single(customer.dict())

    return result


# -------- BATCH PREDICTION --------
@app.post("/predict-batch")
def predict_bulk(data: BatchCustomerData):

    customers = [c.dict() for c in data.customers]

    results = []

    for customer in customers:
        results.append(predict_single(customer))

    return {"predictions": results}