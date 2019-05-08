#!/usr/bin/python
import RPi.GPIO as GPIO
import time

#GPIO SETUP
channel = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
        if GPIO.input(channel):
                print "Vibration Detect!"
        else:
                print "Vibration Detect!"

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  
GPIO.add_event_callback(channel, callback)  
# infinite loop
while True:
        time.sleep(1)
