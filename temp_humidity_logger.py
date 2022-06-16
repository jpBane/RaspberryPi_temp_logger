# Import the required functions from packages
import os
import time
import Adafruit_DHT

# Define the variables
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

# Define the CSV file to log the data.
try:
 f = open("/home/pi/temp_humidity_logger/temp_humidity.csv", "a+")
 if os.stat("/home/pi/temp_humidity_logger/temp_humidity.csv").st_size == 0:
  f.write("Timestamp,Temperature_C,Humidity_pct\r\n")
  
except:
 pass

# Write the data to the CSV file
humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
if humidity is not None and temperature is not None:
 f.write("{0},{1:0.1f},{2:0.1f}\r\n".format(time.strftime("%Y-%m-%d %H:%M:%S"), temperature, humidity))
 f.flush()
else:
 print("Failed to retrieve data from humidity sensor")
