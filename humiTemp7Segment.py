import time
import Adafruit_DHT
import json
import os
import sys
import requests
import datetime

pin = 4
sensor = Adafruit_DHT.DHT22

while True:
  humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
  now = datetime.datetime.now().isoformat()

  if humidity is not None and temperature is not None:
    print('Time={2} Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity, now))

    time.sleep(15)
  else:
    print('Failed to get reading. Try again!')
    sys.exit(1) 
