from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})
# MongoDB connection
client = MongoClient('mongodb://mongo-service:27017/')
db = client['mydatabase']
collection = db['data']

@app.route('/api/data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'POST':
        data = request.json.get('data')
        collection.insert_one({'data': data})
        return jsonify({'message': 'Data saved!'}), 201
    else:
        data = list(collection.find({}, {'_id': 0}))
        return jsonify(data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
