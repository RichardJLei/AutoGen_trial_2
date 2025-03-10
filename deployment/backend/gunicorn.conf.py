"""
Gunicorn configuration for the AutoGen Planner backend.
"""

import multiprocessing

# Bind to 0.0.0.0:8000
bind = "0.0.0.0:8000"

# Number of worker processes
workers = multiprocessing.cpu_count() * 2 + 1

# Worker class
worker_class = "uvicorn.workers.UvicornWorker"

# Timeout
timeout = 120

# Access log
accesslog = "-"

# Error log
errorlog = "-"

# Log level
loglevel = "info"

# Preload the application
preload_app = True

# Maximum number of requests a worker will process before restarting
max_requests = 1000
max_requests_jitter = 50 