# Gunicorn configuration file
import multiprocessing

# Use uvicorn worker for FastAPI (ASGI) application
# This is critical for avoiding the 'FastAPI.__call__() missing 1 required positional argument: 'send'' error
worker_class = "uvicorn.workers.UvicornWorker"

# Gunicorn configuration for production
bind = "0.0.0.0:10000"  # Render default port
workers = multiprocessing.cpu_count() * 2 + 1  # Standard worker calculation
timeout = 120  # Increase timeout for long-running requests
keepalive = 5  # Keep connections alive

print(f"Using worker class: {worker_class}")
print(f"Starting {workers} workers")
