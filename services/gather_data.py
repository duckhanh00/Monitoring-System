# Set the python path
import inspect
import os
import sys
from datetime import datetime
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))))
import socket
import psutil

from config.influxdb import InfluxDB

from services.statistic_service import StatisticService

def gather_data(registry):
    # Get the host name of the machine
    host = socket.gethostname()
    local_ip = socket.gethostbyname(host)

    # Connect InfluxDB
    influxdb = InfluxDB()

    """Gathers the metrics"""
    statistic_service = StatisticService(host=host, ip=local_ip)

    # Start gathering metrics every second
    while True:
        json_body = []
        current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
        print(current_time)
        # Add ram metrics
        swap = psutil.swap_memory()
        
        # Statistic ram
        ram_node = statistic_service.statistic_ram(current_time, "ram")
        json_body.append(ram_node.class_to_json())

        # Statistic cpu
        cpu_node = statistic_service.statistic_cpu(current_time, "cpu")
        json_body.append(cpu_node.class_to_json())

        # Statistic process
        process_node = statistic_service.statistic_process(current_time, "process")
        json_body.append(process_node.class_to_json())

        # Statistic process
        disk_node = statistic_service.statistic_disk(current_time, "disk")
        json_body.append(disk_node.class_to_json())

        influxdb.client.write_points(json_body)
    