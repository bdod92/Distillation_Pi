#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [15, 18, 24]

# loop through pins and set mode and state to 'low'

for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH) #relays connect to NC (normally closed) turn on when in the low state
    
sleep(60)


# time to sleep between operations in the main loop

# SleepTimeL = 2
# 
# # main loop
# 
# try:
#     for i in pinList:
#         GPIO.output(i, GPIO.HIGH)
#         print (i)
#         sleep(3)
#     
#     GPIO.cleanup()
#     print ("Good bye!")
# 
# # End program cleanly with keyboard
# except KeyboardInterrupt:
#   print ("  Quit")
# 
#   # Reset GPIO settings
# GPIO.cleanup()


# find more information on this script at
# http://youtu.be/oaf_zQcrg7g