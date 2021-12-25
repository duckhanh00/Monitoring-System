from models.base import BaseModel
import json

class RamModel(BaseModel):
    def __init__(self, host, ip):
        super().__init__(host, ip)
        self.measurement = "ram"
        self.time = None
        self.fields = None


class RamFields:
    def __init__(self, total, available, percent, cached):
        self.total = total
        self.available = available
        self.percent = percent
        self.cached = cached

    


