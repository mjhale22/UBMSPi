#Wiring diagram and tutorial can be found at: https://tutorials-raspberrypi.com/measuring-soil-moisture-with-raspberry-pi/

#In order to be able to address the MCP3008, SPI must be activated. TYPE THE FOLLOWING INTO TERMINAL:
#   sudo raspi-config
#   Select “8 Advanced Options” -> “A6 SPI” -> “Yes”.

#PRIOR TO RUNNING, TYPE FOLLOWNING INTO TERMINAL:
#   sudo apt-get install git python-dev
#   git clone https://github.com/doceme/py-spidev.git
#   cd py-spidev
#   sudo python setup.py install

#!/usr/bin/python
 
import spidev
import os
import time
 
delay = 0.2
 
spi = spidev.SpiDev()
spi.open(0,0)
 
def readChannel(channel):
  val = spi.xfer2([1,(8+channel)<<4,0])
  data = ((val[1]&3) << 8) + val[2]
  return data
 
if __name__ == "__main__":
  try:
    while True:
      val = readChannel(0)
      if (val != 0):
        print(val)
      time.sleep(delay)
      
  except KeyboardInterrupt:
    print "Cancel."
