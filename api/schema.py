from pydantic import BaseModel
from typing import List


class CustomerData(BaseModel):

    gender: float
    SeniorCitizen: float
    Partner: float
    Dependents: float
    tenure: float
    PhoneService: float
    MultipleLines: float
    InternetService: float
    OnlineSecurity: float
    OnlineBackup: float
    DeviceProtection: float
    TechSupport: float
    StreamingTV: float
    StreamingMovies: float
    Contract: float
    PaperlessBilling: float
    PaymentMethod: float
    MonthlyCharges: float
    TotalCharges: float


class BatchCustomerData(BaseModel):

    customers: List[CustomerData]