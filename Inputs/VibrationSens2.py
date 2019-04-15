from gpiozero import MotionSensor, LED 
from signal import pause

vib = MotionSensor(4)

vib.when_motion = print("Motion Detected")
vib.when_no_motion = print("No Motion")

pause()
