# Use Python 3.8 image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the app source code into the container
COPY app/app.py /app/

# Install dependencies
RUN pip install flask

# Expose the port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
