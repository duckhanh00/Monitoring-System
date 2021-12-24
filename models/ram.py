from models.base import BaseModel
import json

class RamModel(BaseModel):
    def __init__(self, host, ip):
        super().__init__(host, ip)
        self.measurement = "ram"
        self.time = None
        self.fields = None

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

class RamFields:
    def __init__(self, total, available, percent, cached):
        self.total = total
        self.available = available
        self.percent = percent
        self.cached = cached

