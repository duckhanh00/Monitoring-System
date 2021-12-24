import threading
from prometheus.registry import Registry
from services.prometheus import gather_data
from prometheus.exporter import PrometheusMetricHandler
from http.server import HTTPServer

PORT_NUMBER = 4444

# Create the registry
registry = Registry()

# Create the thread that gathers the data while we serve it
thread = threading.Thread(target=gather_data, args=(registry, ))
thread.start()

# Set a server to export (expose to prometheus) the data (in a thread)
try:
    # We make this to set the registry in the handler
    def handler(*args, **kwargs):
        PrometheusMetricHandler(registry, *args, **kwargs)

    server = HTTPServer(('', PORT_NUMBER), handler)
    server.serve_forever()

except KeyboardInterrupt:
    server.socket.close()
    thread.join()