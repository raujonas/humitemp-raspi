import time
import Adafruit_DHT

pin = 4
sensor = Adafruit_DHT.DHT22

while True:
  humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
  if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
    time.sleep(15)
  else:
    print('Failed to get reading. Try again!')
    sys.exit(1) 
