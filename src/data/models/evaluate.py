import pandas as pd
import joblib
import os
import json

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    roc_curve
)

DATA_PATH = "data/processed/processed_churn.csv"
MODEL_PATH = "models/churn_model.pkl"

REPORT_DIR = "reports"


def load_data():

    df = pd.read_csv(DATA_PATH)

    X = df.drop("Churn", axis=1)
    y = df["Churn"]

    return X, y


def load_model():

    model = joblib.load(MODEL_PATH)

    return model


def evaluate_model(model, X, y):

    predictions = model.predict(X)
    probabilities = model.predict_proba(X)[:, 1]

    metrics = {

        "accuracy": accuracy_score(y, predictions),
        "precision": precision_score(y, predictions),
        "recall": recall_score(y, predictions),
        "f1_score": f1_score(y, predictions),
        "roc_auc": roc_auc_score(y, probabilities)

    }

    return metrics, predictions, probabilities


def save_metrics(metrics):

    os.makedirs(REPORT_DIR, exist_ok=True)

    path = os.path.join(REPORT_DIR, "evaluation_metrics.json")

    with open(path, "w") as f:

        json.dump(metrics, f, indent=4)

    print(f"Metrics saved at {path}")


def plot_confusion_matrix(y, predictions):

    cm = confusion_matrix(y, predictions)

    plt.figure(figsize=(6,5))

    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")

    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")

    path = os.path.join(REPORT_DIR, "confusion_matrix.png")

    plt.savefig(path)

    print(f"Confusion matrix saved at {path}")


def plot_roc_curve(y, probabilities):

    fpr, tpr, _ = roc_curve(y, probabilities)

    plt.figure(figsize=(6,5))

    plt.plot(fpr, tpr)

    plt.plot([0,1],[0,1],'--')

    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")

    plt.title("ROC Curve")

    path = os.path.join(REPORT_DIR, "roc_curve.png")

    plt.savefig(path)

    print(f"ROC curve saved at {path}")


def main():

    print("Loading data...")
    X, y = load_data()

    print("Loading model...")
    model = load_model()

    print("Evaluating model...")
    metrics, predictions, probabilities = evaluate_model(model, X, y)

    print("\nEvaluation Metrics:")

    for k, v in metrics.items():

        print(f"{k}: {v:.4f}")

    save_metrics(metrics)

    plot_confusion_matrix(y, predictions)

    plot_roc_curve(y, probabilities)


if __name__ == "__main__":
    main()