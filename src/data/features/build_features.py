import pandas as pd

from src.data.utils.config import PROCESSED_DATA_PATH
from src.data.utils.helpers import load_csv, save_csv
from src.data.utils.logger import get_logger


logger = get_logger()


def clean_total_charges(df):
    """
    Convert TotalCharges column to numeric.
    """

    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    df["TotalCharges"].fillna(df["TotalCharges"].median(), inplace=True)

    return df


def encode_binary_columns(df):
    """
    Convert Yes/No columns to 1/0.
    """

    binary_cols = df.select_dtypes(include="object").columns

    for col in binary_cols:

        if set(df[col].unique()) == {"Yes", "No"}:

            df[col] = df[col].map({"Yes": 1, "No": 0})

    return df


def one_hot_encode(df):
    """
    One-hot encode remaining categorical variables.
    """

    df = pd.get_dummies(df, drop_first=True)

    return df


def build_features():

    logger.info("Starting feature engineering...")

    df = load_csv(PROCESSED_DATA_PATH)

    logger.info("Cleaning TotalCharges column...")
    df = clean_total_charges(df)

    logger.info("Encoding binary categorical variables...")
    df = encode_binary_columns(df)

    logger.info("Applying one-hot encoding...")
    df = one_hot_encode(df)

    logger.info(f"Feature engineering complete. Dataset shape: {df.shape}")

    save_csv(df, PROCESSED_DATA_PATH)

    logger.info("Processed dataset saved.")


def main():

    build_features()


if __name__ == "__main__":
    main()