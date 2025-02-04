from flask import Flask, request, jsonify
import redis
import os

app = Flask(__name__)
redis_host = os.getenv('REDIS_HOST', 'localhost')
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.route('/task', methods=['POST'])
def add_task():
    task = request.json.get('task')
    if task:
        r.lpush('tasks', task)
        return jsonify({'message': 'Task added'}), 201
    return jsonify({'error': 'No task provided'}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
