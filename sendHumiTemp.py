import time
import Adafruit_DHT
import json
import os
import sys
import requests
from datetime import datetime

pin = 4
sensor = Adafruit_DHT.DHT22
hostname = sys.argv[1]
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

response = os.system("ping -c 1 " + hostname)

if response == 0:
  print hostname, 'is up!'
else:
  print hostname, 'is down!'

while True:
  humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
  now = datetime.now().isoformat()

  if humidity is not None and temperature is not None:
    data = {}
    data["temp"] = round(temperature, 2)
    data["humi"] = round(humidity, 2)
    data["time"] = now
    json_data = json.dumps(data)

    r = requests.post('http://' + hostname + ':8080/humitemp/latest', data=json_data, headers=headers)
    print r.content

    time.sleep(60)
  else:
    print('Failed to get reading. Try again!')
#    sys.exit(1) 
    time.sleep(5)
