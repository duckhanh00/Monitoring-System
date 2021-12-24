from influxdb import InfluxDBClient
from config.constants import InfluxDBConstant

class InfluxDB:
    def __init__(self):
        self.client = InfluxDBClient(
            host=InfluxDBConstant.HOST, 
            port=InfluxDBConstant.PORT, 
            username=InfluxDBConstant.USERNAME, 
            password=InfluxDBConstant.PASSWORD
        )

        self.getDatabase('monitoring_db')

        json_body = [
            {
                "measurement": "ram",
                "tags": {
                    "host": "Carol",
                    "ip": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
                },
                "time": "2018-03-28T8:01:00Z",
                "fields": {
                    "duration": 127,
                    "percent": 20
                }
            },
            {
                "measurement": "cpu",
                "tags": {
                    "host": "Carol",
                    "ip": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
                },
                "time": "2018-03-29T8:04:00Z",
                "fields": {
                    "duration": 132
                }
            },
            {
                "measurement": "disk",
                "tags": {
                    "host": "Carol",
                    "ip": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
                },
                "time": "2018-03-30T8:02:00Z",
                "fields": {
                    "duration": 129
                }
            }
        ]
        self.client.write_points(json_body)
        result = self.client.query('SELECT "percent", "duration" FROM "monitoring_db"."autogen"."ram"')
        print(result.raw)

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
    
