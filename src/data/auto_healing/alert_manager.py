from src.data.monitoring.logging_system import get_monitor_logger

logger = get_monitor_logger()


def send_drift_alert(message):
    """
    Trigger alert when data drift is detected.
    """

    alert_message = f"ALERT: DATA DRIFT DETECTED → {message}"

    print(alert_message)

    logger.warning(alert_message)


def send_retraining_alert(message):
    """
    Trigger alert when model retraining starts.
    """

    alert_message = f"ALERT: MODEL RETRAINING TRIGGERED → {message}"

    print(alert_message)

    logger.warning(alert_message)


def send_failure_alert(message):
    """
    Trigger alert when pipeline fails.
    """

    alert_message = f"ALERT: PIPELINE FAILURE → {message}"

    print(alert_message)

    logger.error(alert_message)


def main():

    # test alerts

    send_drift_alert("Drift detected in telecom churn dataset")

    send_retraining_alert("Retraining started due to performance drop")

    send_failure_alert("Model pipeline failed during evaluation")


if __name__ == "__main__":
    main()