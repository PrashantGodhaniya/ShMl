from pydantic import BaseModel
from typing import List, Union


class CustomerData(BaseModel):

    gender: Union[str, int]
    SeniorCitizen: int
    Partner: Union[str, int]
    Dependents: Union[str, int]

    tenure: float

    PhoneService: Union[str, int]
    MultipleLines: Union[str, int]

    InternetService: Union[str, int]

    OnlineSecurity: Union[str, int]
    OnlineBackup: Union[str, int]
    DeviceProtection: Union[str, int]
    TechSupport: Union[str, int]

    StreamingTV: Union[str, int]
    StreamingMovies: Union[str, int]

    Contract: Union[str, int]

    PaperlessBilling: Union[str, int]

    PaymentMethod: Union[str, int]

    MonthlyCharges: float
    TotalCharges: float


class BatchCustomerData(BaseModel):

    customers: List[CustomerData]