from flask import Blueprint, request, jsonify
from app.services.screenstats_analysis import ScreenStats

screenstats_blueprint = Blueprint('screenstats', __name__)

# Initialize ScreenStats Service
screen_stats_analyzer = ScreenStats()

@screenstats_blueprint.route('/predict', methods=['POST'])
def predict_screenstats():
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

    # Make prediction
    prediction = screen_stats_analyzer.predict([age, gender, screen_time, social_media, gaming])

    # Ensure the response is a dictionary (JSON serializable)
    if isinstance(prediction, set):
        prediction = list(prediction)  # Convert set to list if necessary
    elif not isinstance(prediction, dict):
        prediction = {"prediction": str(prediction)}  # Convert to a JSON object

    return jsonify(prediction)
