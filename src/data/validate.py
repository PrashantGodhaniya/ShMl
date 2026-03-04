import pandas as pd

from src.data.utils.config import RAW_DATA_PATH
from src.data.utils.helpers import load_csv
from src.data.utils.logger import get_logger


logger = get_logger()


def check_missing_values(df):
    """
    Check dataset for missing values.
    """

    missing = df.isnull().sum()

    if missing.sum() > 0:
        logger.warning(f"Missing values detected:\n{missing}")
    else:
        logger.info("No missing values detected.")


def check_duplicates(df):
    """
    Check for duplicate rows.
    """

    duplicates = df.duplicated().sum()

    if duplicates > 0:
        logger.warning(f"{duplicates} duplicate rows found.")
    else:
        logger.info("No duplicate rows found.")


def validate_target_column(df):
    """
    Ensure churn column contains valid values.
    """

    if "Churn" not in df.columns:
        raise ValueError("Target column 'Churn' is missing.")

    unique_values = df["Churn"].unique()

    logger.info(f"Target column values: {unique_values}")


def validate_schema(df):
    """
    Basic schema validation.
    """

    expected_columns = [
        "customerID",
        "gender",
        "SeniorCitizen",
        "Partner",
        "Dependents",
        "tenure",
        "PhoneService",
        "MultipleLines",
        "InternetService",
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies",
        "Contract",
        "PaperlessBilling",
        "PaymentMethod",
        "MonthlyCharges",
        "TotalCharges",
        "Churn"
    ]

    missing_cols = set(expected_columns) - set(df.columns)

    if missing_cols:
        logger.error(f"Missing columns: {missing_cols}")
        raise ValueError("Dataset schema mismatch")

    logger.info("Schema validation passed.")


def validate_data():

    logger.info("Starting data validation...")

    df = load_csv(RAW_DATA_PATH)

    validate_schema(df)

    check_missing_values(df)

    check_duplicates(df)

    validate_target_column(df)

    logger.info("Data validation completed successfully.")


def main():

    validate_data()


if __name__ == "__main__":
    main()