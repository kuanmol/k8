from flask import Flask, request
import os

app = Flask(__name__)
LOG_FILE = '/logs/app.log'
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

@app.route('/')
def home():
    message = "Hello from Flask App!"
    with open(LOG_FILE, 'a') as f:
        f.write(f"{LOG_LEVEL}: {message}\n")
    return message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
