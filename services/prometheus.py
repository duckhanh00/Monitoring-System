# Set the python path
import inspect
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))))

import socket
import time

from prometheus.collectors import Gauge
import psutil
from config.influxdb import InfluxDB
PORT_NUMBER = 4444

from models.ram import RamModel, RamFields

def gather_data(registry):
    influxdb = InfluxDB()
    

    """Gathers the metrics"""

    # Get the host name of the machine
    host = socket.gethostname()
    local_ip = socket. gethostbyname(host)

    # Create our collectors
    ram_metric = Gauge("memory_usage_bytes", "Memory usage in bytes.",
                       {'host': host})
    cpu_metric = Gauge("cpu_usage_percent", "CPU usage percent.",
                       {'host': host})

    # register the metric collectors
    registry.register(ram_metric)
    registry.register(cpu_metric)

    # Start gathering metrics every second
    # while True:
    time.sleep(1)

    # Add ram metrics
    ram = psutil.virtual_memory()
    swap = psutil.swap_memory()

    ram_node = RamModel(host=host, ip=local_ip)
    ram_node.fields = RamFields(total=ram.total, available=ram.available, percent=ram.percent, cached=ram.cached)
    print(ram_node.toJSON())

    ram_metric.set({'type': "virtual", }, ram.used)
    ram_metric.set({'type': "virtual", 'status': "cached"}, ram.cached)
    ram_metric.set({'type': "swap"}, swap.used)

    print(ram, swap, psutil.cpu_percent(interval=1, percpu=True))
    # Add cpu metrics
    for c, p in enumerate(psutil.cpu_percent(interval=1, percpu=True)):
        print("cpu", c, p)
        cpu_metric.set({'core': c}, p)