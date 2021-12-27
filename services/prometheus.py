# Set the python path
import inspect
import os
import sys
from datetime import datetime
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))))

import socket
import time

from prometheus.collectors import Gauge
import psutil
from config.influxdb import InfluxDB

from models.ram import RamModel, RamFields
from models.cpu import CPUModel, CPUFields
from models.disk import DiskModel, DiskFields
def gather_data(registry):
    influxdb = InfluxDB()
    

    """Gathers the metrics"""

    # Get the host name of the machine
    host = socket.gethostname()
    local_ip = socket.gethostbyname(host)

    # Create our collectors
    ram_metric = Gauge("memory_usage_bytes", "Memory usage in bytes.",
                       {'host': host})
    cpu_metric = Gauge("cpu_usage_percent", "CPU usage percent.",
                       {'host': host})
    disk_metric = Gauge("disk_usage_percent", "disk usage percent", 
                        {'host': host})
    # register the metric collectors
    registry.register(ram_metric)
    registry.register(cpu_metric)
    registry.register(disk_metric)

    # Start gathering metrics every second
    while True:
        json_body = []
        current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
        print(current_time)
        # Add ram metrics
        ram = psutil.virtual_memory()
        swap = psutil.swap_memory()
        
        ram_node = RamModel(host=host, ip=local_ip)
        ram_node.time = current_time
        ram_node.fields = RamFields(total=ram.total, available=ram.available, percent=ram.percent, cached=ram.cached)
        json_body.append(ram_node.class_to_json())

        cpu_percent = psutil.cpu_percent(interval=1) 
        cpu_node = CPUModel(host=host, ip=local_ip)
        cpu_node.time = current_time
        cpu_node.fields = CPUFields(percent=cpu_percent)
        json_body.append(cpu_node.class_to_json())

        disks = {}
        for i in psutil.disk_partitions():
            disks[i.mountpoint] = psutil.disk_usage(i.mountpoint).percent
        disk_node = DiskModel(host=host, ip=local_ip)
        disk_node.time = current_time
        disk_node.fields = disks
        json_body.append(disk_node.disk())

        print(json_body)
        influxdb.client.write_points(json_body)
    