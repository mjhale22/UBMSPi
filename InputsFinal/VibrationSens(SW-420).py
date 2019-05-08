# Import Raspberry Pi GPIO info as GPIO and Import time functionality
import RPi.GPIO as GPIO
import time

# Set variable of gpio as pin 21
gpio = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio, GPIO.IN)

def callback(gpio):
        if GPIO.input(gpio):
                print ("Vibration Detect!")
        else:
                print ("Vibration Detect!")

GPIO.add_event_detect(gpio, GPIO.BOTH, bouncetime=300)  
GPIO.add_event_callback(gpio, callback)  

# Creates an infinite loop
while True:
        time.sleep(1)
