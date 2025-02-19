FROM python:3.9
RUN apt-get update && apt-get install -y curl
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
