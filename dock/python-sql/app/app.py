from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL connection details
DB_CONFIG = {
    'host': 'mysql',
    'user': 'root',
    'password': 'rootpassword',
    'database': 'testdb'
}

# Connect to MySQL database
def get_db_connection():
    conn = mysql.connector.connect(**DB_CONFIG)
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM items')
    items = cursor.fetchall()
    conn.close()
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    item_name = request.form['name']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO items (name) VALUES (%s)', (item_name,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
