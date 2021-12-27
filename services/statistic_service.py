import psutil
from models.base import BaseModel, RamFields, ProcessFields, CPUFields, DiskFields

class StatisticService:
    def __init__(self, host, ip):
        self.node = BaseModel(host=host, ip=ip)

    def set_time_and_measurement(self, time, measurement):
        self.node.time = time
        self.node.measurement = measurement

    def statistic_ram(self, time, measurement):
        self.set_time_and_measurement(time=time, measurement=measurement)

        ram = psutil.virtual_memory()
        self.node.fields = RamFields(total=ram.total, available=ram.available, percent=ram.percent, cached=ram.cached)

        return self.node

    def statistic_cpu(self, time, measurement):
        self.set_time_and_measurement(time=time, measurement=measurement)
        
        cpu_percent = psutil.cpu_percent(interval=1) 
        self.node.fields = CPUFields(percent=cpu_percent)

        return self.node

    def statistic_process(self, time, measurement):
        self.set_time_and_measurement(time=time, measurement=measurement)

        pids = psutil.pids()
        self.node.fields = ProcessFields(number_of_process=len(pids))

        return self.node

    def statistic_disk(self, time, measurement):
        self.set_time_and_measurement(time=time, measurement=measurement)

        disk_used = 0
        disk_total = 0
        for i in psutil.disk_partitions():
            disk_usage = psutil.disk_usage(i.mountpoint)
            disk_used += disk_used + disk_usage.used 
            disk_total += disk_total + disk_usage.total 

        disk_percent = disk_used / disk_total * 100
        self.node.fields = DiskFields(percent=disk_percent)

        return self.node
