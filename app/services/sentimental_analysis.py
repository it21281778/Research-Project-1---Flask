import os
import joblib
import logging
from typing import Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SentimentalAnalysis:
    def __init__(self):
        """
        Initialize the SentimentalAnalysis class by loading the model and setting up the reverse mapping.
        """
        self.model = self._load_model()
        self.reverse_mapping = self._initialize_reverse_mapping()

    def _load_model(self) -> joblib:
        """
        Load the machine learning model from the specified path.

        Returns:
            The loaded model.
        """
        try:
            model_path = os.path.join(os.path.dirname(__file__), "../models/Logistic_Regression.joblib")
            logging.info(f"Loading model from {model_path}")
            model = joblib.load(model_path)
            logging.info("Model loaded successfully")
            return model
        except FileNotFoundError:
            logging.error(f"Model file not found at {model_path}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error while loading the model: {e}")
            raise

    def _initialize_reverse_mapping(self) -> dict:
        """
        Initialize the reverse mapping for prediction labels.

        Returns:
            A dictionary mapping prediction labels to their corresponding categories.
        """
        reverse_mapping = {
            0: 'Anxiety',
            1: 'Normal',
            2: 'Depression',
            3: 'Suicidal',
            4: 'Stress',
            5: 'Bipolar',
            6: 'Personality disorder'
        }
        logging.info("Reverse mapping initialized")
        return reverse_mapping

    def predict(self, text: str) -> Optional[str]:
        """
        Predict the category of the given text using the loaded model.

        Args:
            text: The input text for prediction.

        Returns:
            The predicted category as a string, or an error message if prediction fails.
        """
        if not text:
            logging.warning("Empty text received for prediction")
            return "Input text is empty"

        logging.info(f"Received text for prediction: {text}")
        try:
            prediction = self.model.predict([text])
            result = self.reverse_mapping.get(prediction[0], "Unknown")
            logging.info(f"Prediction result: {result}")
            return result
        except Exception as e:
            logging.error(f"Error during prediction: {e}")
            return f"Prediction error: {e}"
