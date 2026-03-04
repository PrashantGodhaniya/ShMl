import logging
import os

from src.data.utils.config import ROOT_DIR


LOG_DIR = os.path.join(ROOT_DIR, "logs")
LOG_FILE = os.path.join(LOG_DIR, "monitoring.log")


def get_monitor_logger():

    os.makedirs(LOG_DIR, exist_ok=True)

    logger = logging.getLogger("monitoring_logger")

    logger.setLevel(logging.INFO)

    if not logger.handlers:

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler = logging.FileHandler(LOG_FILE)
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

    return logger


def log_prediction_event(message):

    logger = get_monitor_logger()

    logger.info(f"PREDICTION_EVENT: {message}")


def log_drift_event(message):

    logger = get_monitor_logger()

    logger.warning(f"DRIFT_ALERT: {message}")


def log_retraining_event(message):

    logger = get_monitor_logger()

    logger.info(f"RETRAINING_TRIGGERED: {message}")