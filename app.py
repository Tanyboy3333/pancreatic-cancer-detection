from flask import Flask, request, render_template, jsonify
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import io

app = Flask(__name__)

# ✅ Suppress TensorFlow logs & optimize CPU usage
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"  # Reduce TensorFlow log spam
os.environ["TF_INTER_OP_PARALLELISM_THREADS"] = "1"
os.environ["TF_INTRA_OP_PARALLELISM_THREADS"] = "1"

# ✅ Define allowed image extensions
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "tiff"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_image(image):
    """Preprocess image for the model"""
    image = image.resize((128, 128))  # Resize to model input size
    image = np.array(image) / 255.0  # Normalize
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# ✅ Load model lazily to reduce memory usage
def get_model():
    global model
    if "model" not in globals():
        model = load_model("cancer_model.h5")  # Load model only when needed
    return model

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return jsonify({"error": "No file part"}), 400

        file = request.files["file"]

        if file.filename == "":
            return jsonify({"error": "No selected file"}), 400

        if file and allowed_file(file.filename):
            try:
                image = Image.open(io.BytesIO(file.read())).convert("RGB")
                processed_image = preprocess_image(image)

                model = get_model()  # ✅ Load model only when needed
                prediction = model.predict(processed_image)
                result = "Cancerous" if prediction[0][0] > 0.5 else "Non-Cancerous"

                return jsonify({"prediction": result}), 200

            except Exception as e:
                return jsonify({"error": str(e)}), 500

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
