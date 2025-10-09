from flask import Blueprint, request, jsonify
from app.services.screenstats_analysis import ScreenStats

# Define a blueprint for screenstats routes
screenstats_blueprint = Blueprint('screenstats', __name__)

# Initialize ScreenStats Service
screen_stats_analyzer = ScreenStats()

@screenstats_blueprint.route('/predict', methods=['POST'])
def predict_screenstats():
    """
    Endpoint to predict screen statistics based on input data.

    Expects a JSON payload with the following fields:
    - age: int
    - gender: str
    - screen_time: float
    - social_media: float
    - gaming: float

    Returns:
        JSON response with the prediction or an error message.
    """
    data = request.json

    # Extract input values from JSON
    age = data.get("age")
    gender = data.get("gender")
    screen_time = data.get("screen_time")
    social_media = data.get("social_media")
    gaming = data.get("gaming")

    # Validate required fields
    if None in [age, gender, screen_time, social_media, gaming]:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        # Make prediction
        prediction = screen_stats_analyzer.predict([age, gender, screen_time, social_media, gaming])

        # Ensure the response is a dictionary (JSON serializable)
        if isinstance(prediction, set):
            prediction = list(prediction)  # Convert set to list if necessary
        elif not isinstance(prediction, dict):
            prediction = {"prediction": str(prediction)}  # Convert to a JSON object

        return jsonify(prediction)
    except Exception as e:
        # Handle unexpected errors during prediction
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
