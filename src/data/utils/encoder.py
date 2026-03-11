# src/data/utils/encoder.py

ENCODERS = {

    "gender": {"Male": 1, "Female": 0},

    "Partner": {"Yes": 1, "No": 0},
    "Dependents": {"Yes": 1, "No": 0},

    "PhoneService": {"Yes": 1, "No": 0},

    "MultipleLines": {
        "No": 0,
        "Yes": 1,
        "No phone service": 0
    },

    "InternetService": {
        "No": 0,
        "DSL": 1,
        "Fiber optic": 2
    },

    "OnlineSecurity": {
        "No": 0,
        "Yes": 1,
        "No internet service": 0
    },

    "OnlineBackup": {
        "No": 0,
        "Yes": 1,
        "No internet service": 0
    },

    "DeviceProtection": {
        "No": 0,
        "Yes": 1,
        "No internet service": 0
    },

    "TechSupport": {
        "No": 0,
        "Yes": 1,
        "No internet service": 0
    },

    "StreamingTV": {
        "No": 0,
        "Yes": 1,
        "No internet service": 0
    },

    "StreamingMovies": {
        "No": 0,
        "Yes": 1,
        "No internet service": 0
    },

    "Contract": {
        "Month-to-month": 0,
        "One year": 1,
        "Two year": 2
    },

    "PaperlessBilling": {"No": 0, "Yes": 1},

    "PaymentMethod": {
        "Electronic check": 0,
        "Mailed check": 1,
        "Bank transfer (automatic)": 2,
        "Credit card (automatic)": 3
    },

    "Churn": {"No": 0, "Yes": 1}
}


def encode_input(data):
    """
    Encodes categorical values using predefined mappings
    """

    for col, mapping in ENCODERS.items():

        if col in data:

            value = data[col]

            if isinstance(value, str) and value in mapping:

                data[col] = mapping[value]

    return data