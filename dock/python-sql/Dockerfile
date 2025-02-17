# Use Python 3.9 image as base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt from the 'app' directory to /app in the container
COPY app/requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy the 'app' directory content into the container's /app directory
COPY app/ /app/

# Expose port 5000 (default Flask port)
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]
