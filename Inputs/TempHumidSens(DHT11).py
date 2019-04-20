#PRIOR TO RUNNING, TYPE FOLLOWNING INTO TERMINAL:
#   git clone https://github.com/adafruit/Adafruit_Python_DHT.git
#   sudo pip3 install Adafruit_DHT
#   cd Adafruit_Python_DHT
#   sudo apt-get update

#Import Adafruit_DHT Sensor Library to use script associated with sensor
import Adafruit_DHT

# Set variable of sensor to (sensor being used) DHT11 : Options are DHT11, DHT22 or AM2302
sensor=Adafruit_DHT.DHT11
 
# Set variable of gpio as (pin) 21
gpio=21

#Set temperatureF to convert temperature (celsius) to fahrenheit
temperatureF=(temperature*(9/5)+32)

humidity, temperature = Adafruit_DHT.read(sensor, gpio)
 
if humidity is not None and temperature is not None:
  print('Temp={0:0.1f}*F  Humidity={1:0.1f}%'.format(temperatureF, humidity))
else:
  print('Failed to get reading. Try again!')
