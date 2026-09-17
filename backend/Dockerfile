FROM python:3.12-alpine

WORKDIR /app

RUN pip install --no-cache-dir psycopg2-binary

COPY app.py .

CMD ["python", "app.py"]
