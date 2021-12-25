from influxdb import InfluxDBClient
from config.constants import InfluxDBConstant

class InfluxDB:
    def __init__(self):
        self.client = InfluxDBClient(
            host=InfluxDBConstant.HOST, 
            port=InfluxDBConstant.PORT, 
            username=InfluxDBConstant.USERNAME, 
            password=InfluxDBConstant.PASSWORD,
        )

        self.getDatabase(InfluxDBConstant.DATABASE_MONITORING)

    def getDatabase(self, database_name):
        dbs = self.client.get_list_database()
        db_names = [] 
        for db in dbs:
            db_names.append(db['name'])

        if database_name not in db_names:
            self.client.create_database(database_name)
            self.client.switch_database(database_name)
        else:
            self.client.switch_database(database_name)
    
