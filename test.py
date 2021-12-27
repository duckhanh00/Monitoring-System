from typing import Dict
import psutil
from influxdb import InfluxDBClient
psutil.disk_partitions()
disks = {}
for i in psutil.disk_partitions():
    disks[i.mountpoint] = {'percent':psutil.disk_usage(i.mountpoint).percent,
                            'total':psutil.disk_usage(i.mountpoint).total,
                            'free':psutil.disk_usage(i.mountpoint).free,
                            'used':psutil.disk_usage(i.mountpoint).used}
# print(disks)

pids = psutil.pids()
print(len(pids))