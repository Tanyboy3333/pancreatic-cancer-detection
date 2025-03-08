# ✅ Use the official Python 3.10 image (matches CI/CD workflow)
FROM python:3.10

# ✅ Set the working directory inside the container
WORKDIR /app

# ✅ Copy the project files to the container
COPY . /app

# ✅ Install TensorFlow Nightly first (matches CI/CD workflow)
RUN pip install --upgrade tf-nightly

# ✅ Install all dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# ✅ Expose the dynamic Render port (use $PORT instead of 10000)
EXPOSE 5000

# ✅ Start the Flask application using Gunicorn with 1 worker (to prevent memory issues)
CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:5000", "app:app"]
