import pandas as pd
import numpy as np
import os

# -----------------------------
# Load Original Dataset
# -----------------------------
DATA_PATH = "data/raw/teleco_churn.csv"
OUTPUT_PATH = "data/drifted_data/churn_drifted.csv"

df = pd.read_csv(DATA_PATH)
drifted_df = df.copy()

# Create output directory if not exists
os.makedirs("data/drifted_data", exist_ok=True)


# -----------------------------
# 1. NUMERICAL DRIFT
# -----------------------------
# Simulate price increase
drifted_df["MonthlyCharges"] = (
    drifted_df["MonthlyCharges"] +
    np.random.normal(15, 5, len(df))
)

# Reduce tenure slightly (new customers trend)
drifted_df["tenure"] = (
    drifted_df["tenure"] *
    np.random.uniform(0.6, 1.0, len(df))
).astype(int)


# -----------------------------
# 2. CATEGORICAL DISTRIBUTION SHIFT
# -----------------------------
# More customers switching to month-to-month contract
mask = np.random.rand(len(df)) < 0.3
drifted_df.loc[mask, "Contract"] = "Month-to-month"

# Increase Fiber optic internet usage
mask2 = np.random.rand(len(df)) < 0.25
drifted_df.loc[mask2, "InternetService"] = "Fiber optic"


# -----------------------------
# 3. NOISE INJECTION
# -----------------------------
# Add noise to total charges
drifted_df["TotalCharges"] = pd.to_numeric(
    drifted_df["TotalCharges"], errors="coerce"
)

drifted_df["TotalCharges"] = (
    drifted_df["TotalCharges"] +
    np.random.normal(50, 20, len(df))
)


# -----------------------------
# 4. MISSING VALUE SIMULATION
# -----------------------------
# Random missing values (real-world issue)
missing_mask = np.random.rand(len(df)) < 0.05
drifted_df.loc[missing_mask, "TotalCharges"] = np.nan


# -----------------------------
# 5. SAVE DRIFTED DATASET
# -----------------------------
drifted_df.to_csv(OUTPUT_PATH, index=False)

print("Drifted dataset generated successfully!")
print("Saved at:", OUTPUT_PATH)
