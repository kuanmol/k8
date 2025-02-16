FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend code
COPY app.py /app/

# Expose the port
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
