from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient
import psycopg2
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# MySQL Configuration
mysql_db = SQLAlchemy(app)

class MySQLUser(mysql_db.Model):
    id = mysql_db.Column(mysql_db.Integer, primary_key=True)
    name = mysql_db.Column(mysql_db.String(100), nullable=False)

# PostgreSQL Configuration
pg_conn = psycopg2.connect(Config.POSTGRES_URI)
pg_cursor = pg_conn.cursor()

# Create PostgreSQL Table
pg_cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name TEXT
    )
""")
pg_conn.commit()

# MongoDB Configuration
mongo_client = MongoClient(Config.MONGO_URI)
mongo_db = mongo_client[Config.MONGO_DB]
mongo_collection = mongo_db["users"]

# ✅ Fix for before_first_request issue
with app.app_context():
    mysql_db.create_all()

@app.route('/')
def index():
    mysql_users = MySQLUser.query.all()
    pg_cursor.execute("SELECT * FROM users")
    pg_users = pg_cursor.fetchall()
    mongo_users = list(mongo_collection.find({}, {"_id": 0}))

    return render_template("index.html", mysql_users=mysql_users, pg_users=pg_users, mongo_users=mongo_users)

@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form['name']

    # Add to MySQL
    new_mysql_user = MySQLUser(name=name)
    mysql_db.session.add(new_mysql_user)
    mysql_db.session.commit()

    # Add to PostgreSQL
    pg_cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
    pg_conn.commit()

    # Add to MongoDB
    mongo_collection.insert_one({"name": name})

    return redirect('/')

@app.route('/delete_user/<int:id>')
def delete_user(id):
    # Delete from MySQL
    user = MySQLUser.query.get(id)
    if user:
        mysql_db.session.delete(user)
        mysql_db.session.commit()

    # Delete from PostgreSQL
    pg_cursor.execute("DELETE FROM users WHERE id = %s", (id,))
    pg_conn.commit()

    # Delete from MongoDB (Assuming name is unique for simplicity)
    mongo_collection.delete_one({"name": user.name})

    return redirect('/')

@app.route('/healthz')
def health_check():
    return "OK", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
