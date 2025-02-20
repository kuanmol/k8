from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

db_config = {
    'host': 'db',
    'user': 'root',
    'password': 'password',
    'database': 'mydatabase'
}

def get_db_connection():
    """Establish and return a MySQL database connection."""
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500

@app.route('/users', methods=['GET'])
def get_users():
    """Fetch all users from the database."""
    conn = get_db_connection()
    if isinstance(conn, tuple):  # If connection failed
        return conn
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    """Add a new user."""
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

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    """Update user information."""
    data = request.get_json()
    conn = get_db_connection()
    if isinstance(conn, tuple):
        return conn
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET name = %s, email = %s WHERE id = %s', (data['name'], data['email'], id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'User updated successfully'})

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    """Delete a user by ID."""
    conn = get_db_connection()
    if isinstance(conn, tuple):
        return conn
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = %s', (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'User deleted successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
