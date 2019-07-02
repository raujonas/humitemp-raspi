import time
import Adafruit_DHT
import json
import os
import sys
import requests
import datetime

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.virtual import viewport, sevensegment

pin = 4
sensor = Adafruit_DHT.DHT22

def date(seg):
  now = datetime.datetime.now()
  seg.text = now.strftime("%y-%m-%d")

def clock(seg):
  interval = 0.5
  for i in range(int(5/interval)):
    now = datetime.datetime.now()
    seg.text = now.strftime("%H-%M-%S")

    if i % 2 == 0:
      seg.text = now.strftime("%H-%M-%S")
    else:
      seg.text = now.strftime("%H %M %S")
    time.sleep(interval)

def humiTemp(seg):
  humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

  if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
#    seg.text = ('{0:0.1f} CEL'.format(temperature))
#    time.sleep(5)
#    seg.text = ('{0:0.1f} PER'.format(humidity))
    seg.text = ('{0:0.1f}  {1:0.1f}'.format(temperature, humidity))

def main():
  serial = spi(port=0, device=0, gpio=noop())
  device = max7219(serial, cascaded=1)
  seg = sevensegment(device)
	
  while True:
#    date(seg)
#    time.sleep(3)
#    clock(seg)
    humiTemp(seg)
    time.sleep(15)

if __name__ == '__main__':
  main()
