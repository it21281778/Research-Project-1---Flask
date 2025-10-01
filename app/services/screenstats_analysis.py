import os
import joblib
import logging
import numpy as np

class ScreenStats:
    def __init__(self, model_filename="rf_model.joblib"):
        """
        Initializes the ScreenStats class by loading the trained Random Forest model.
        """
        self.model = None
        self.model_filename = model_filename
        self.mental_health_labels = {0: "Better", 1: "Good", 2: "Fair", 3: "Poor"}
        self._load_model()

    def _load_model(self):
        """
        Private method to load the trained model.
        """
        try:
            # Define model path
            model_path = os.path.join(os.path.dirname(__file__), "../models", self.model_filename)

            # Logging model loading
            logging.info(f"Loading model from {model_path}")
            
            # Load the trained model
            self.model = joblib.load(model_path)
            
            # Log success
            logging.info("Model loaded successfully")

        except FileNotFoundError:
            logging.error(f"Model file not found at {model_path}")
            raise FileNotFoundError(f"Model file not found at {model_path}")
        except Exception as e:
            logging.error(f"Error loading model: {e}")
            raise RuntimeError(f"Error loading model: {e}")

    def predict(self, features):
        """
        Predicts the mental health status based on the input features.

        Args:
            features (list or np.ndarray): Input features for the model.

        Returns:
            dict: A dictionary containing the prediction result or an error message.
        """
        try:
            # Validate input
            if not isinstance(features, (list, np.ndarray)):
                raise ValueError("Features must be a list or numpy array")

            # Ensure input is in the correct format
            input_data = np.array(features).reshape(1, -1)

            # Make a prediction
            prediction = self.model.predict(input_data)[0]

            # Map prediction to human-readable categories
            result = self.mental_health_labels.get(prediction, "Unknown")

            return {"mental_health_status": result}

        except ValueError as ve:
            logging.error(f"Input validation error: {ve}")
            return {"error": f"Input validation error: {ve}"}
        except Exception as e:
            logging.error(f"Prediction error: {e}")
            return {"error": "Failed to make a prediction"}
