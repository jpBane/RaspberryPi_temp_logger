import os
import time
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

try:
 f = open("/home/pi/temp_humidity_logger/temp_humidity.csv", "a+")
 if os.stat("/home/pi/temp_humidity_logger/temp_humidty.csv").st_size == 0:
  f.write("Timestamp,Temperature_C,Humidity_pct\r\r")
  
except:
 pass
 
while True:
 humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
 if humidity is not None and temperature is not None:
  f.write("{0},{1:0.1f},{2:0.1f}\r\n".format(time.strftime("%Y-%m-%d %H:%M:%S"), temperature, humidity))
 else:
  print("Failed to retrieve data from humidity sensor")
 
 time.sleep(60)
