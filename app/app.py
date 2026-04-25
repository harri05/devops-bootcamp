from flask import Flask, jsonify
import os
import socket
import redis
import time

app = Flask(__name__)

# Connect to Redis — host comes from environment variable
# Defaults to "localhost" for local dev, overridden in Docker/K8s
REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = int(os.environ.get("REDIS_PORT", 6379))
APP_ENV    = os.environ.get("APP_ENV", "development")
APP_START  = time.time()

# Initialize Redis connection
try:
    cache = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
    cache.ping()
    redis_connected = True
except Exception:
    redis_connected = False

def increment_requests():
    if redis_connected:
        return cache.incr("requests_total")
    return -1

@app.route("/")
def home():
    count = increment_requests()
    return jsonify({
        "message": "Welcome to DevOps Bootcamp API",
        "version": "2.0.0",
        "host": socket.gethostname(),
        "request_number": count
    })

@app.route("/health")
def health():
    redis_status = "connected" if redis_connected else "disconnected"
    return jsonify({
        "status": "healthy",
        "version": "2.0.0",
        "redis": redis_status
    })

@app.route("/info")
def info():
    return jsonify({
        "app": "devops-bootcamp",
        "environment": APP_ENV,
        "stack": ["Python", "Flask", "Docker", "Redis", "Kubernetes"]
    })

@app.route("/metrics-preview")
def metrics():
    uptime = int(time.time() - APP_START)
    total  = cache.get("requests_total") if redis_connected else "N/A"
    return jsonify({
        "requests_total": total,
        "uptime_seconds": uptime,
        "environment": APP_ENV,
        "redis_connected": redis_connected
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
this is broken python
