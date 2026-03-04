import mlflow


def setup_mlflow():
    """
    Configure MLflow tracking.
    """

    mlflow.set_tracking_uri("file:./mlruns")

    mlflow.set_experiment("telecom_churn_prediction")

    print("MLflow experiment initialized.")