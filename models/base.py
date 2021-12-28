import json

class BaseModel:
    def __init__(self, host, ip):
        self.tags = Tags(host, ip)
        self.measurement = None
        self.time = None
        self.fields = None

    def class_to_json(self):
        return {
            'measurement': self.measurement,
            'time': self.time,
            'tags': self.tags.__dict__,
            'fields': self.fields.__dict__
        }   

class Tags:
    def __init__(self, host, ip):
        self.host = host
        self.ip = ip

class CPUFields:
    def __init__(self, percent):
        self.cpu_percent = percent

class ProcessFields:
    def __init__(self, number_of_process):
        self.number_of_process = number_of_process

class RamFields:
    def __init__(self, total, available, percent, cached):
        self.total = total
        self.available = available
        self.percent = percent
        self.cached = cached

class DiskFields:
    def set_mount_point(self, mount_point, total, percent):
        self.__dict__[mount_point + "_total"] = total
        self.__dict__[mount_point + "_percent"] = percent