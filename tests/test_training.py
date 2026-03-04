import os
from src.data.utils.config import MODEL_PATH


def test_model_exists():
    """
    Check if trained model file exists.
    """

    assert os.path.exists(MODEL_PATH)