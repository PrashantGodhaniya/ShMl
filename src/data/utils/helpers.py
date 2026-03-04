import os
import pandas as pd


def create_directory(path):
    """
    Create directory if it does not exist.
    """
    os.makedirs(path, exist_ok=True)


def load_csv(path):
    """
    Load CSV safely.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    return pd.read_csv(path)


def save_csv(df, path):
    """
    Save dataframe to CSV.
    """
    directory = os.path.dirname(path)
    os.makedirs(directory, exist_ok=True)

    df.to_csv(path, index=False)


def get_common_columns(df1, df2):
    """
    Return common columns between two datasets.
    """
    return df1.columns.intersection(df2.columns)