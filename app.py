from flask import Flask, request, jsonify, render_template
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = load_model('model.h5')  # Load .h5 file

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract input features from form or API request
    data = [float(x) for x in request.form.values()]
    final_features = np.array([data])

    # Make prediction
    prediction = model.predict(final_features)
    
    # Assuming binary classification, return 0 or 1
    predicted_class = int(np.argmax(prediction, axis=1)[0])

    return jsonify({'prediction': predicted_class})

if __name__ == "__main__":
    app.run(debug=True)
