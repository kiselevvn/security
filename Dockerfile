FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# CMD ["gunicorn", "--workers", "3", "--timeout", "600", "--chdir", "./backend", "main.wsgi:application", "-b", "0.0.0.0:8000",]