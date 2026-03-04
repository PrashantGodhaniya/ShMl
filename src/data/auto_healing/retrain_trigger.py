import subprocess
import json
import os
from src.data.monitoring.logging_system import log_retraining_event
from src.data.auto_healing.alert_manager import send_retraining_alert


DRIFT_SCRIPT = "src/data/monitoring/drift_detection.py"
TRAIN_SCRIPT = "src/data/models/train.py"
EVALUATE_SCRIPT = "src/data/models/evaluate.py"

REPORT_PATH = "reports/evaluation_metrics.json"
BEST_MODEL_METRIC = "roc_auc"


def run_script(script_path):

    result = subprocess.run(
        ["python", script_path],
        capture_output=True,
        text=True
    )

    print(result.stdout)

    return result.stdout


def drift_detected(output):

    return "Drift Detected" in output


def load_metrics():

    if not os.path.exists(REPORT_PATH):
        return None

    with open(REPORT_PATH) as f:
        metrics = json.load(f)

    return metrics


def main():

    print("\nChecking for data drift...\n")

    drift_output = run_script(DRIFT_SCRIPT)

    if drift_detected(drift_output):

        print("\n⚠ Drift detected. Retraining model...\n")
        
        send_retraining_alert("Model retraining started due to drift")

        run_script(TRAIN_SCRIPT)

        print("\nEvaluating new model...\n")

        run_script(EVALUATE_SCRIPT)

        metrics = load_metrics()

        if metrics:

            print("\nNew Model Performance:")

            for k, v in metrics.items():
                print(f"{k}: {v:.4f}")

            print("\nModel retraining complete.")

            log_retraining_event("Model retraining triggered due to performance drop")

    else:

        print("\nNo drift detected. Model remains unchanged.")


if __name__ == "__main__":
    main()