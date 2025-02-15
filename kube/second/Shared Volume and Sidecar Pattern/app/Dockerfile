FROM python:3.9-slim

WORKDIR /app

COPY main.py .
RUN pip install Flask

EXPOSE 5000

CMD ["python", "main.py"]
