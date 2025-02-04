import redis
import psycopg2
import time
import os

redis_host = os.getenv('REDIS_HOST', 'localhost')
postgres_host = os.getenv('POSTGRES_HOST', 'localhost')
postgres_user = os.getenv('POSTGRES_USER', 'admin')
postgres_password = os.getenv('POSTGRES_PASSWORD', 'admin')
postgres_db = os.getenv('POSTGRES_DB', 'tasks')

r = redis.Redis(host=redis_host, port=6379, decode_responses=True)
conn = psycopg2.connect(
    host=postgres_host,
    database=postgres_db,
    user=postgres_user,
    password=postgres_password
)
cur = conn.cursor()

while True:
    task = r.brpop('tasks')
    if task:
        task_data = task[1]
        print(f"Processing task: {task_data}")
        cur.execute("INSERT INTO task_log (task) VALUES (%s)", (task_data,))
        conn.commit()
    time.sleep(1)
