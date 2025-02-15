import time

LOG_FILE = '/logs/app.log'
PROCESSED_FILE = '/logs/processed.log'

def process_logs():
    with open(LOG_FILE, 'r') as infile, open(PROCESSED_FILE, 'a') as outfile:
        for line in infile:
            outfile.write(f"[PROCESSED] {time.ctime()}: {line}")

if __name__ == '__main__':
    while True:
        process_logs()
        time.sleep(5)
