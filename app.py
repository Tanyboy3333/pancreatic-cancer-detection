import os
from flask import Flask, request, jsonify, render_template
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), 'cancer_model.h5')
model = load_model(model_path)  # Load the correct .h5 file

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = [float(x) for x in request.form.values()]
        final_features = np.array([data])

        prediction = model.predict(final_features)
        predicted_class = int(np.argmax(prediction, axis=1)[0])

        return jsonify({'prediction': predicted_class})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
