
from flask import Flask
import redis

app = Flask(__name__)

# Connect to Redis using the container's name as the hostname
r = redis.StrictRedis(host='redis', port=6379, db=0, decode_responses=True)

@app.route('/')
def hello_world():
    # Set and get data from Redis
    r.set('foo', 'bar')
    return f"Hello, Docker! Foo is {r.get('foo')}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
