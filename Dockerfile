# syntax=docker/dockerfile:1.7
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# Exponer 8080 (convención Cloud Run)
ENV PORT=8080
EXPOSE 8080

# Arrancar servidor HTTP (JSON-RPC)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
