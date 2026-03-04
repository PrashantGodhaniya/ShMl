import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
import os


# -------------------------
# CONFIG PATHS
# -------------------------
RAW_DATA_PATH = "data/raw/teleco_churn.csv"
PROCESSED_DATA_PATH = "data/processed/processed_churn.csv"


# -------------------------
# LOAD DATA
# -------------------------
def load_data():
    df = pd.read_csv(RAW_DATA_PATH)
    return df


# -------------------------
# CLEAN DATA
# -------------------------
def clean_data(df):
    # Remove customerID (not useful for ML)
    if "customerID" in df.columns:
        df.drop("customerID", axis=1, inplace=True)

    # Convert TotalCharges to numeric
    if "TotalCharges" in df.columns:
        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    # Fill missing numeric values
    df.fillna(df.median(numeric_only=True), inplace=True)

    # Fill categorical missing values
    for col in df.select_dtypes(include="object"):
        df[col].fillna(df[col].mode()[0], inplace=True)

    return df


# -------------------------
# ENCODE CATEGORICAL DATA
# -------------------------
def encode_data(df):
    le = LabelEncoder()

    for col in df.select_dtypes(include="object"):
        df[col] = le.fit_transform(df[col])

    return df


# -------------------------
# SCALE NUMERIC FEATURES
# -------------------------
def scale_data(df):
    scaler = StandardScaler()

    # Select numeric columns
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

    # Remove target column from scaling
    if "Churn" in numeric_cols:
        numeric_cols = numeric_cols.drop("Churn")

    # Scale features
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    return df


# -------------------------
# SAVE DATA
# -------------------------
def save_data(df):
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv(PROCESSED_DATA_PATH, index=False)
    print(f"Processed data saved at: {PROCESSED_DATA_PATH}")


# -------------------------
# MAIN PIPELINE
# -------------------------
def main():
    df = load_data()
    df = clean_data(df)
    df = encode_data(df)
    df = scale_data(df)
    save_data(df)


if __name__ == "__main__":
    main() 