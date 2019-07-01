import time
import Adafruit_DHT
import json
import os
import sys
import requests
import datetime

pin = 4
sensor = Adafruit_DHT.DHT22
hostname = sys.argv[1]
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

#response = os.system("ping -c 1 " + hostname)

#if response == 0:
# print hostname, 'is up!'
#else:
# print hostname, 'is down!'

while True:
  humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
  now = datetime.datetime.now().isoformat()

  if humidity is not None and temperature is not None:
#    print('Time={2} Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity, now))

    data = {}
    data["temp"] = round(temperature, 2)
    data["humi"] = round(humidity, 2)
    data["time"] = now
    json_data = json.dumps(data)
    print json_data

    r = requests.put('http://' + hostname + ':8080/humitemp/latest', data=json_data, headers=headers)
#    print r.content

    time.sleep(15)
  else:
    print('Failed to get reading. Try again!')
#    sys.exit(1) 
    time.sleep(5)
