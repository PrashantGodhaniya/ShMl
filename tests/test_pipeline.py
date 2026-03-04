import pandas as pd
from src.data.utils.config import RAW_DATA_PATH


def test_data_exists():
    """
    Check if raw dataset exists.
    """

    df = pd.read_csv(RAW_DATA_PATH)

    assert df is not None
    assert df.shape[0] > 0


def test_target_column():
    """
    Ensure churn column exists.
    """

    df = pd.read_csv(RAW_DATA_PATH)

    assert "Churn" in df.columns