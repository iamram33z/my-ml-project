# predict.py
import numpy as np
from model import load_model, predict

# Dummy input data for prediction
input_data = [0.5, 1.2, 0.3, 0.7, 1.1]

# Load the trained model
model = load_model()

# Make a prediction
prediction = predict(model, input_data)
print(f"Prediction: {prediction}")
