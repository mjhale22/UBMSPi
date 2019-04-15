from gpiozero import MotionSensor, LED 
from signal import pause

vib = MotionSensor(21)
led = LED(16)

vib.when_motion = led.on
vib.when_no_motion = led.off

pause()
