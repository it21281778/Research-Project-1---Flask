from flask import Blueprint, request, jsonify
from app.services.sentimental_analysis import SentimentalAnalysis

sentimental_blueprint = Blueprint('sentimental', __name__)

# Initialize Sentimental Analysis Service
sentiment_analyzer = SentimentalAnalysis()

@sentimental_blueprint.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get('text', '')
    prediction = sentiment_analyzer.predict(text)
    return jsonify({"prediction": prediction})
