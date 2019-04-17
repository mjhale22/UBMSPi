import dht11
import RPi.GPIO as GPIO
import time

def dht11_example():
    # Pin 4
    dht11_0 = dht11.DHT11(pin=4)
    result = dht11_0.read()
    print('DHT11')
    print("Temperature: ", result.temperature, "C")
    print("Humidity: ", result.humidity, "%\n")
