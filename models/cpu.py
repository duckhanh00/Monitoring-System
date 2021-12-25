from models.base import BaseModel

class CPUModel(BaseModel):
    def __init__(self, host, ip):
        super().__init__(host, ip)
        self.measurement = "cpu"
        self.time = None
        self.fields = None

class CPUFields:
    def __init__(self, percent):
        self.cpu_percent = percent