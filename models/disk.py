from models.base import BaseModel

class DiskModel(BaseModel):
    def __init__(self, host, ip):
        super().__init__(host, ip)
        self.measurement = "disk"
        self.time = None
        self.fields = None

class DiskFields:
    def __init__(self, total, used, free, percent):
        self.total = total
        self.used = used
        self.free = free
        self.percent = percent
