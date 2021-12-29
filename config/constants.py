import os
from dotenv import load_dotenv
load_dotenv()

class InfluxDBConstant:
    HOST = os.getenv("INFLUX_HOST") or '165.22.52.226'
    PORT = os.getenv("INFLUX_PORT") or '8086'
    USERNAME = os.getenv("INFLUX_USERNAME") or 'admin'
    PASSWORD = os.getenv("INFLUX_PASSWORD") or '123456'
    DATABASE_MONITORING = os.getenv("DATABASE_MONITORING") or 'monitoring_db'

class Constant:
    CAPACITY_THRESHOLD = 53687091200

