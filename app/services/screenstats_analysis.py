import os
import joblib
import logging
import numpy as np

class ScreenStats:
    def __init__(self):
        """
        Initializes the ScreenStats class by loading the trained Random Forest model.
        """
        try:
            # Define model path
            model_path = os.path.join(os.path.dirname(__file__), "../models/rf_model.joblib")

            # Logging model loading
            logging.info(f"Loading model from {model_path}")
            
            # Load the trained model
            self.model = joblib.load(model_path)
            
            # Log success
            logging.info("Model loaded successfully")

        except Exception as e:
            logging.error(f"Error loading model: {e}")
            raise e

    def predict(self, features):
        try:
            # Ensure input is in the correct format
            input_data = np.array(features).reshape(1, -1)

            # Make a prediction
            prediction = self.model.predict(input_data)[0]

            # Map prediction to human-readable categories
            mental_health_labels = {0: "Better", 1: "Good", 2: "Fair", 3: "Poor"}
            result = mental_health_labels.get(prediction, "Unknown")

            return {"mental_health_status": result}

        except Exception as e:
            logging.error(f"Prediction error: {e}")
            return {"error": "Failed to make a prediction"}
