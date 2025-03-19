🔬 Pancreatic Cancer Detection using Deep Learning & MLOps
🚀 Live Demo: https://pancreatic-cancer-detection.onrender.com/

This project implements a Convolutional Neural Network (CNN) model to detect pancreatic cancer from CT scan images. The trained model is deployed using Flask, a CI/CD pipeline (GitHub Actions) automates testing and deployment, and the application is hosted on Render with a user-friendly UI for real-time predictions.


🚀 How It Works:

1️⃣ Model Training & Saving
A CNN model was trained using CT scan images to classify them as cancerous or non-cancerous.
The model was saved in TensorFlow format (cancer_model.h5).


2️⃣ Backend: Flask for Inference
Flask loads the trained model and provides an API for predictions.
Uploaded CT scan images are preprocessed before being passed to the model.


3️⃣ Frontend: User-friendly UI
A simple yet elegant web interface built using HTML, Bootstrap, and JavaScript.
Users upload an image, and the model instantly predicts if it's cancerous.


4️⃣ CI/CD Pipeline: GitHub Actions & Render
GitHub Actions automatically runs unit tests before deployment.
If tests pass, the app is deployed to Render using a webhook.


The app is now publicly accessible via Render.
🛠️ Installation & Running Locally

1️⃣ Clone the Repository



git clone https://github.com/yourusername/Pancreatic-Cancer-Detection.git
cd Pancreatic-Cancer-Detection


2️⃣ Create a Virtual Environment & Install Dependencies


python -m venv venv
source venv/bin/activate   # For Mac/Linux
venv\Scripts\activate      # For Windows

pip install -r requirements.txt


3️⃣ Run the Flask App


python app.py


The app will be available at http://127.0.0.1:5000/.


🛠️ Deployment on Render


1️⃣ Push your code to GitHub


2️⃣ GitHub Actions runs tests and triggers deployment


3️⃣ Render pulls the latest version and redeploys the app


4️⃣ Live at: Pancreatic Cancer Detection

✅ Features

✔ Deep Learning-powered image classification

✔ Flask API for seamless model inference

✔ Interactive web UI for easy image uploads

✔ CI/CD automation with GitHub Actions

✔ Live deployment on Render



📜 License
This project is open-source