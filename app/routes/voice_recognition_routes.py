from flask import Blueprint, request, jsonify
import os
from werkzeug.utils import secure_filename
from app.services.voice_emotion_recognition import predict_emotion  

voice_bp = Blueprint("voice", __name__)

UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@voice_bp.route("/predict-emotion", methods=["POST"])
def predict_emotion_route():
    print("📥 Received request at /predict-emotion")

    # ✅ Debug: Check incoming request headers and content type
    print("🔍 Headers:", request.headers)
    print("🔍 Content-Type:", request.content_type)

    if "file" not in request.files:
        print("❌ No file found in request")
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        print("❌ Empty file uploaded")
        return jsonify({"error": "Empty file uploaded"}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    print(f"📂 Saving file to {file_path}")
    file.save(file_path)

    # ✅ Process Audio and Predict Emotion
    predicted_emotion = predict_emotion(file_path)
    print(f"🎙️ Predicted Emotion: {predicted_emotion}")

    return jsonify({"emotion": predicted_emotion})
