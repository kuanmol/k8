from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def home():
    if random.random() > 0.7:  # Simulate failure randomly
        raise Exception("Simulated Failure")
    return "Hello, Docker World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
