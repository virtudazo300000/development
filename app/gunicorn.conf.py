bind = '0.0.0.0:8100'
threads = 2

timeout = 120  # Increase timeout to 120 seconds
workers = 3    # Number of worker processes
worker_class = 'sync'
keepalive = 2
worker_connections = 1000
