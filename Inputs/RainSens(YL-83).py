#!/usr/bin/env python

from time import sleep
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)
state = GPIO.input(21)

if (state == 0):
    print "Water detected!"
else:
    print "Water not detected"
