import pandas as pd
import os
from scipy.stats import ks_2samp
from src.data.monitoring.logging_system import log_drift_event
from src.data.auto_healing.alert_manager import send_drift_alert


REFERENCE_DATA = "data/processed/processed_churn.csv"
CURRENT_DATA = "data/drifted_data/churn_drifted.csv"

DRIFT_THRESHOLD = 0.05


def load_datasets():

    reference = pd.read_csv(REFERENCE_DATA)
    current = pd.read_csv(CURRENT_DATA)

    return reference, current


def detect_drift(reference, current):

    drift_report = {}

    numeric_columns = reference.select_dtypes(include=["int64", "float64"]).columns

    for column in numeric_columns:

        ref_col = pd.to_numeric(reference[column], errors="coerce")
        cur_col = pd.to_numeric(current[column], errors="coerce")

        ref_col = ref_col.dropna()
        cur_col = cur_col.dropna()

        stat, p_value = ks_2samp(ref_col, cur_col)

        drift_report[column] = {
            "p_value": float(p_value),
            "drift_detected": p_value < DRIFT_THRESHOLD
        }

    return drift_report


def print_report(report):

    print("\nDrift Detection Report\n")

    drift_found = False

    for feature, result in report.items():

        print(f"{feature}: p_value={result['p_value']:.4f} drift={result['drift_detected']}")

        if result["drift_detected"]:
            drift_found = True

    if drift_found:
        print("\n⚠ Data Drift Detected!")
        log_drift_event("Data drift detected in telecom churn dataset")
        send_drift_alert("Data drift detected in telecom churn dataset")
    else:
        print("\nNo significant drift detected.")


def main():

    reference, current = load_datasets()

    report = detect_drift(reference, current)

    print_report(report)


if __name__ == "__main__":
    main()