"""
model.py
--------
Linear regression training and prediction for oil reserve volume estimation.

Linear regression is appropriate here because the target (product volume)
has a roughly continuous distribution and the relationship with geological
features is expected to be approximately linear.
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler


FEATURE_COLUMNS = ["f0", "f1", "f2"]
TARGET_COLUMN = "product"


def prepare_data(df: pd.DataFrame, test_size: float = 0.25, random_state: int = 42) -> tuple:
    """Split a region DataFrame into train/validation sets.

    Args:
        df: Region DataFrame with feature and target columns.
        test_size: Proportion reserved for validation. Defaults to 0.25.
        random_state: Random seed for reproducibility. Defaults to 42.

    Returns:
        Tuple of (X_train, X_val, y_train, y_val).
    """
    X = df[FEATURE_COLUMNS]
    y = df[TARGET_COLUMN]
    return train_test_split(X, y, test_size=test_size, random_state=random_state)


def train(X_train, y_train) -> LinearRegression:
    """Train a Linear Regression model on the provided training data.

    Args:
        X_train: Training feature matrix.
        y_train: Training target vector.

    Returns:
        Fitted LinearRegression model.
    """
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model


def evaluate(model: LinearRegression, X_val, y_val) -> dict:
    """Evaluate a trained model on the validation set.

    Args:
        model: Fitted LinearRegression model.
        X_val: Validation feature matrix.
        y_val: True validation target values.

    Returns:
        Dict with predictions array, rmse, and mean_predicted_volume.
    """
    predictions = model.predict(X_val)
    rmse = np.sqrt(mean_squared_error(y_val, predictions))

    return {
        "predictions": predictions,
        "rmse": round(rmse, 4),
        "mean_predicted_volume": round(predictions.mean(), 4),
    }
