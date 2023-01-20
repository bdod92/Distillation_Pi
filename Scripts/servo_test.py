#Import libraries
import RPi.GPIO as GPIO
import time

#Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

#Set pin 16 (GPIO 23) as GPIO pin out and servo1 as pin 16 PWM
GPIO.setup(36, GPIO.OUT)
servo1 = GPIO.PWM(36,50) #pin 16, 50 hz

#start PWM, but with value of 0 = pulse off
servo1.start(0)
print("waiting for 2 seconds")
time.sleep(2)

#move the servo
print("rotating 180 degrees in 10 steps")

#define variable duty
duty = 2

#loop duty values from 2 to 12 (0 to 180 degrees)
while duty <= 12:
    servo1.ChangeDutyCycle(duty)
    time.sleep(0.3)
    servo1.ChangeDutyCycle(0)
    time.sleep(0.7) #using 0.7, but could theoretically be less
    duty = duty + 1

#wait some seconds
time.sleep(2)

#turn back to 90 degrees
print("turning back to 90 degrees for 2 seconds")
servo1.ChangeDutyCycle(7)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)
time.sleep(1.5)

#turn abck to 0 deg
print("turning back to 0 degrees")
servo1.ChangeDutyCycle(2)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

#clean up at the end
servo1.stop()
GPIO.cleanup()
print("Goodbye!")