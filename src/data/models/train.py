import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

from src.data.utils.config import PROCESSED_DATA_PATH, MODEL_PATH
from src.data.utils.logger import get_logger
from src.data.utils.config_loader import load_config

# MLflow
from mlops.mlflow_setup import setup_mlflow
from mlops.experiment_tracking import log_training


logger = get_logger()


def train_model():

    logger.info("Loading processed dataset...")

    df = pd.read_csv(PROCESSED_DATA_PATH)

    # Load model configuration
    config = load_config("configs/model_config.yaml")

    n_estimators = config["parameters"]["n_estimators"]
    max_depth = config["parameters"]["max_depth"]
    min_samples_split = config["parameters"]["min_samples_split"]
    random_state = config["parameters"]["random_state"]

    logger.info("Splitting dataset...")

    X = df.drop("Churn", axis=1)
    y = df["Churn"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=random_state
    )

    logger.info("Training RandomForest model...")

    model = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        min_samples_split=min_samples_split,
        random_state=random_state
    )

    model.fit(X_train, y_train)

    logger.info("Evaluating model...")

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    report = classification_report(y_test, y_pred)

    logger.info(f"\nAccuracy: {accuracy}")
    logger.info(f"\nClassification Report:\n{report}")

    # Save model
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)

    joblib.dump(model, MODEL_PATH)

    logger.info(f"Model saved at {MODEL_PATH}")

    # MLflow tracking
    setup_mlflow()

    metrics = {
        "accuracy": accuracy
    }

    log_training(metrics)


def main():

    train_model()


if __name__ == "__main__":
    main()