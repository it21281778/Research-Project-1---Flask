import pickle
import os

# Define the path to the model file
model_path = os.path.join(os.path.dirname(__file__), 'thinkingpattern.pkl')

# Load the model
def load_model(path):
    with open(path, 'rb') as file:
        model = pickle.load(file)
    return model

# Use the model for prediction
def analyze_thinking_pattern(input_data):
    model = load_model(model_path)
    prediction = model.predict([input_data])  # Assuming input_data is a single feature vector
    return prediction

