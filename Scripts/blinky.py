import time
import board
import digitalio

print("Hello static blinky")

led = digitalio.DigitalInOut(board.D18) # create LED digital in/out instance at D18
led.direction = digitalio.Direction.OUTPUT #specify that the direction is out

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)