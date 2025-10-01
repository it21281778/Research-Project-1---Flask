import os
import librosa
import numpy as np
import tensorflow as tf # type: ignore
import joblib

# ✅ Load Pre-trained LSTM Model & Label Encoder
MODEL_PATH = os.path.join(os.path.dirname(__file__), "../models/speech_emotion_model_lstm.keras")
ENCODER_PATH = os.path.join(os.path.dirname(__file__), "../models/emotion_encoder.pkl")

print(f"📥 Loading Model from: {MODEL_PATH}")
model = tf.keras.models.load_model(MODEL_PATH)
print("✅ Model Loaded Successfully")

print(f"📥 Loading Encoder from: {ENCODER_PATH}")
encoder = joblib.load(ENCODER_PATH)
print("✅ Encoder Loaded Successfully")

# ✅ Preprocess audio file into (1, 300, 40) shape
def extract_audio_features(file_path, expected_timesteps=300, n_mfcc=40):
    try:
        y, sr = librosa.load(file_path, sr=22050, duration=5.0)
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc).T  # shape: (time, 40)

        print(f"🔍 Extracted MFCC shape: {mfcc.shape}")

        # Pad or truncate
        if mfcc.shape[0] < expected_timesteps:
            pad_width = expected_timesteps - mfcc.shape[0]
            mfcc = np.pad(mfcc, ((0, pad_width), (0, 0)), mode='constant')
        else:
            mfcc = mfcc[:expected_timesteps, :]

        return np.expand_dims(mfcc, axis=0)  # shape: (1, 300, 40)
    except Exception as e:
        print(f"❌ Error extracting MFCCs: {e}")
        return None

# ✅ Predict emotion
def predict_emotion(audio_path):
    features = extract_audio_features(audio_path)
    if features is None:
        return {"error": "Invalid audio file"}

    try:
        prediction = model.predict(features)
        predicted_index = np.argmax(prediction)
        predicted_emotion = encoder.categories_[0][predicted_index]

        print(f"🎙️ Predicted Emotion: {predicted_emotion}")
        return {"emotion": predicted_emotion}
    except Exception as e:
        print(f"❌ Model inference error: {e}")
        return {"error": "Model inference failed"}
