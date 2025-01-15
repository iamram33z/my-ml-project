# test_model.py
import pytest  # type: ignore
import numpy as np
from app.model import create_model, train_model


def test_create_model():
    model = create_model()
    assert model is not None


def test_train_model():
    # Create some dummy data
    X = np.random.rand(100, 5)
    y = np.random.randint(2, size=100)
    model = train_model(X, y)
    assert model is not None
    assert hasattr(model, "predict")
