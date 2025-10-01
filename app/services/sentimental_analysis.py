import os
import joblib
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SentimentalAnalysis:
    def __init__(self):
        try:
            model_path = os.path.join(os.path.dirname(__file__), "../models/Logistic_Regression.joblib")
            logging.info(f"Loading model from {model_path}")
            self.model = joblib.load(model_path)
            logging.info("Model loaded successfully")
        except Exception as e:
            logging.error(f"Error loading model: {e}")
            raise e

        self.reverse_mapping = {
            0: 'Anxiety',
            1: 'Normal',
            2: 'Depression',
            3: 'Suicidal',
            4: 'Stress',
            5: 'Bipolar',
            6: 'Personality disorder'
        }
        logging.info("Reverse mapping initialized")

    def predict(self, text):
        logging.info(f"Received text for prediction: {text}")
        try:
            prediction = self.model.predict([text])
            result = self.reverse_mapping.get(prediction[0], "Unknown")
            logging.info(f"Prediction result: {result}")
            return result
        except Exception as e:
            logging.error(f"Error during prediction: {e}")
            return str(e)
