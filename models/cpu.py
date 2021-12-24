from models.base import BaseModel

class CPUModel(BaseModel):
    def __init__(self, host, ip) -> None:
        super(host, ip)
        self.measurement = "cpu"
        self.time = None
        self.fields = CPUFields()

class CPUFields:
    def __init__(self) -> None:
        self.cpu_percent = None