# Import required functions from packages
from influxdb import InfluxDBClient
import time
import Adafruit_DHT 

# Define the variables
client = InfluxDBClient(host='localhost', port=8086)
client.switch_database('temp_logger_db')

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

# ...

while True:
 if humidity is not None and temperature is not None:
  json_body = [
    {
        "measurement": "temp_humidity",
        "tags": {
            "location": "Keller"
        },
        "fields": {
            "temperature": round(temperature, ndigits = 1),
            "humidity": round(humidity, ndigits = 1)            
        }
    }
  ]
 else:
  print("Failed to retrieve data from humidity sensor")

 client.write_points(json_body, time_precision='s')

 time.sleep(60)
