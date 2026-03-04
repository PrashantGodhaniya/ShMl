import pandas as pd

from src.data.utils.config import RAW_DATA_PATH
from src.data.utils.helpers import load_csv
from src.data.utils.logger import get_logger


logger = get_logger()


def ingest_data():
    """
    Load raw telecom churn dataset.
    """

    logger.info("Starting data ingestion...")

    try:

        df = load_csv(RAW_DATA_PATH)

        logger.info(f"Dataset loaded successfully with shape: {df.shape}")

        return df

    except Exception as e:

        logger.error(f"Data ingestion failed: {e}")
        raise e


def preview_data(df):
    """
    Display basic dataset information.
    """

    logger.info("Previewing dataset...")

    logger.info(f"Columns: {list(df.columns)}")

    logger.info(f"Dataset shape: {df.shape}")

    logger.info(f"Missing values:\n{df.isnull().sum()}")


def main():

    df = ingest_data()

    preview_data(df)


if __name__ == "__main__":
    main()