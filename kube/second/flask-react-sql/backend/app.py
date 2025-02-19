from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
import os
import time

app = Flask(__name__)
CORS(app)

# Fetching database credentials from environment variables
db_config = {
    'host': os.environ.get('MYSQL_HOST', 'mysql-service'),
    'user': os.environ.get('MYSQL_USER', 'root'),
    'password': os.environ.get('MYSQL_PASSWORD', 'secretPassword'),
    'database': os.environ.get('MYSQL_DATABASE', 'mydatabase')
}

def get_db_connection():
    """Establish and return a MySQL database connection with retry logic."""
    retries = 5  # Retry up to 5 times if DB is not ready
    for _ in range(retries):
        try:
            conn = mysql.connector.connect(**db_config)
            return conn
        except mysql.connector.Error as err:
            print(f"Database connection error: {err}, retrying...")
            time.sleep(5)  # Wait before retrying
    return jsonify({"error": "Database connection failed after retries"}), 500

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    if isinstance(conn, tuple):
        return conn
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data.get('name') or not data.get('email'):
        return jsonify({'error': 'Missing name or email'}), 400

    conn = get_db_connection()
    if isinstance(conn, tuple):
        return conn
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, email) VALUES (%s, %s)', (data['name'], data['email']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'User added successfully'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
