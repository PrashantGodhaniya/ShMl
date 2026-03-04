from fastapi import FastAPI
from api.schema import CustomerData, BatchCustomerData
from api.inference_service import predict_single, predict_batch


app = FastAPI(
    title="Customer Churn Prediction API",
    description="Self-Healing MLOps Churn Prediction System",
    version="1.0"
)


@app.get("/")
def health_check():

    return {"status": "API running"}


@app.post("/predict")
def predict(customer: CustomerData):

    result = predict_single(customer.dict())

    return result


@app.post("/predict-batch")
def predict_bulk(data: BatchCustomerData):

    customers = [c.dict() for c in data.customers]

    results = predict_batch(customers)

    return {"predictions": results}