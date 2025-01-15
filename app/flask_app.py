from flask import Flask, jsonify, request  # type: ignore
from app.model import load_model, predict
import os

# Initialize the Flask app
app = Flask(__name__)

# Load the model once when the app starts
MODEL_PATH = "./app/model/model.pkl"

def initialize_model():
    """Load the trained model."""
    if not os.path.exists(MODEL_PATH):
        raise Exception(f"Model file not found at {MODEL_PATH}")
    return load_model(MODEL_PATH)

model = initialize_model()  # Initialize the model at the start

@app.route("/")
def home():
    """Root endpoint to verify the server is running."""
    return "ML Model API is running!"

@app.route("/predict", methods=["POST"])
def make_prediction():
    """API endpoint to make predictions."""
    try:
        # Extract input data from the POST request
        data = request.get_json()  # Example: {'input': [0.5, 1.2, 0.3, 0.7, 1.1]}
        input_data = data["input"]  # Extract the input data (ensure it's a list or array)

        # Make prediction using the model
        prediction = predict(model, input_data)

        # Return the prediction as JSON response
        return jsonify({"prediction": prediction.tolist()})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)  # Run the Flask app (Flask's dev server, for testing)