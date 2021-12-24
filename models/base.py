class BaseModel:
    def __init__(self, host, ip):
        self.tags = Tags(host, ip)

class Tags:
    def __init__(self, host, ip):
        self.host = host
        self.ip = ip