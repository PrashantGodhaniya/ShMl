import os

# Project Root
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))

# Data paths
RAW_DATA_PATH = os.path.join(ROOT_DIR, "data/raw/teleco_churn.csv")
PROCESSED_DATA_PATH = os.path.join(ROOT_DIR, "data/processed/processed_churn.csv")
DRIFT_DATA_PATH = os.path.join(ROOT_DIR, "data/drifted_data/churn_drifted.csv")

# Model paths
MODEL_DIR = os.path.join(ROOT_DIR, "models")
MODEL_PATH = os.path.join(MODEL_DIR, "churn_model.pkl")

# Logs
LOG_DIR = os.path.join(ROOT_DIR, "logs")

# Reports
REPORT_DIR = os.path.join(ROOT_DIR, "reports")

# MLflow
MLFLOW_TRACKING_URI = os.path.join(ROOT_DIR, "mlruns")
MLFLOW_EXPERIMENT = "telecom_churn_prediction"