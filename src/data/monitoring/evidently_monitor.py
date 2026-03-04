import pandas as pd
import os

from evidently.report import Report
from evidently.metric_preset import DataDriftPreset


REFERENCE_DATA = "data/processed/processed_churn.csv"
CURRENT_DATA = "data/drifted_data/churn_drifted.csv"

REPORT_PATH = "reports/evidently_drift_report.html"


def preprocess(df):

    # Remove ID column if exists
    if "customerID" in df.columns:
        df = df.drop(columns=["customerID"])

    # Convert Yes/No columns to numeric
    df = df.replace({"Yes": 1, "No": 0})

    # Convert categorical columns using one-hot encoding
    df = pd.get_dummies(df)

    return df


def load_datasets():

    reference = pd.read_csv(REFERENCE_DATA)
    current = pd.read_csv(CURRENT_DATA)

    reference = preprocess(reference)
    current = preprocess(current)

    # Ensure same columns
    common_cols = reference.columns.intersection(current.columns)

    reference = reference[common_cols]
    current = current[common_cols]

    return reference, current


def generate_report(reference, current):

    report = Report(metrics=[DataDriftPreset()])

    report.run(
        reference_data=reference,
        current_data=current
    )

    os.makedirs("reports", exist_ok=True)

    report.save_html(REPORT_PATH)

    print("Drift report generated at:", REPORT_PATH)


def main():

    reference, current = load_datasets()

    generate_report(reference, current)


if __name__ == "__main__":
    main()