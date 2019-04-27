import time
import Adafruit_DHT
import json
import os
import sys

pin = 4
sensor = Adafruit_DHT.DHT22
hostname = sys.argv[1]
response = os.system("ping -c 1 " + hostname)

if response == 0:
 print hostname, 'is up!'
else:
 print hostname, 'is down!'

while True:
  humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

  if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))

    data = {}
    data["temp"] = round(temperature, 2)
    data["humi"] = round(humidity, 2)
    json_data = json.dumps(data)
    print "JSON: ", json_data

    time.sleep(15)
  else:
    print('Failed to get reading. Try again!')
    sys.exit(1) 
