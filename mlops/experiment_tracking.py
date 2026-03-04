import mlflow


def log_training(metrics):
    """
    Log training metrics to MLflow.
    """

    with mlflow.start_run():

        for key, value in metrics.items():
            mlflow.log_metric(key, value)

        print("Training metrics logged to MLflow.")