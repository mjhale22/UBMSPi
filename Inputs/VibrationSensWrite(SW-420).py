from gpiozero import MotionSensor, LED
from signal import pause

vib = MotionSensor(21)
led = LED(16)

vib.when_motion = print("Motion Detected")
vib.when_no_motion = print("No Motion")

pause()
