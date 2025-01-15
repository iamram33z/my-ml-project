# train.py
import numpy as np
from model import train_model

# Dummy dataset (features: X, labels: y)
X = np.random.rand(100, 5)
y = np.random.randint(2, size=100)

# Train the model
train_model(X, y)
print("Model trained and saved!")
