from flask import Blueprint, request, jsonify
from app.services.thinking_analysis import analyze_thinking_pattern

thinking_blueprint = Blueprint('thinking', __name__)

@thinking_blueprint.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    input_data = data.get('input_data', [])
    prediction = analyze_thinking_pattern(input_data)
    return jsonify({"prediction": prediction})

