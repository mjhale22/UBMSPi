    
#!/usr/bin/python

import RPi.GPIO as GPIO
import time

pin = 8

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN)

def callback(pin):
	if GPIO.input(pin):
		print("DETECTED")
	else:
		print("DOH")


GPIO.add_event_detect(pin, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(pin, callback)

while True:
	time.sleep(1)
