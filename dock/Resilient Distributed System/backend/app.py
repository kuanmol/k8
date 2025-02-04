from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Hello from backend!", "container_id": socket.gethostname()}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
