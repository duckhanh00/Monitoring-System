import json

class BaseModel:
    def __init__(self, host, ip):
        self.tags = Tags(host, ip)

    def class_to_json(self):
        return {
            'measurement': self.measurement,
            'time': self.time,
            'tags': self.tags.__dict__,
            'fields': self.fields.__dict__
        }   
    def disk(self):
        return {
            'measurement': self.measurement,
            'time': self.time,
            'tags': self.tags.__dict__,
            'fields': self.fields
        } 
class Tags:
    def __init__(self, host, ip):
        self.host = host
        self.ip = ip