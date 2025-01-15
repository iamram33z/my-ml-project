# model.py
import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression
import os

MODEL_PATH = "./app/model/model.pkl"  # Path for model storage


def create_model():
    """Create a logistic regression model"""
    model = LogisticRegression(max_iter=1000)
    return model


def save_model(model, filename=MODEL_PATH):
    """Save the trained model to a file"""
    with open(filename, "wb") as f:
        pickle.dump(model, f)


def load_model(filename=MODEL_PATH):
    """Load a saved model from a file"""
    if os.path.exists(filename):
        with open(filename, "rb") as f:
            model = pickle.load(f)
        return model
    else:
        raise FileNotFoundError(f"Model file {filename} not found!")


def train_model(X, y):
    """Train a new model"""
    model = create_model()
    model.fit(X, y)
    save_model(model)
    return model


def predict(model, input_data):
    """Make a prediction using the trained model"""
    input_data = np.array(input_data).reshape(1, -1)  # Reshape for a single sample
    prediction = model.predict(input_data)
    return prediction
