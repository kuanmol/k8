from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db_config = {
    'host': 'mysql-service',  # Using the service name for internal Kubernetes communication
    'user': 'root',
    'password': 'rootpassword',
    'database': 'mydatabase'
}

# Route to fetch data
@app.route('/data', methods=['GET'])
def get_data():
    # Connect to MySQL
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Query the database
    cursor.execute("SELECT 'Hello from backend!' AS message")
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return jsonify({"message": result[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
