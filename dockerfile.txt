# Use an official Python runtime
FROM python:3.8

# Set working directory
WORKDIR /app

# Copy the project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 10000 (Render uses dynamic ports)
EXPOSE 10000

# Start the Flask application using Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:10000", "app:app"]
