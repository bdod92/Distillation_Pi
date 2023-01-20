import time
import board
import digitalio

print("Hello static blinky")

led = digitalio.DigitalInOut(board.D18) # create LED digital in/out instance at D18
led.direction = digitalio.Direction.OUTPUT #specify that the direction is out

button = digitalio.DigitalInOut(board.D4) #create the button instance at D4 and save
button.direction = digitalio.Direction.INPUT #specify that the button information direction is an input
button.pull = digitalio.Pull.UP #pull the button state into the up position

while True: 
    led.value = not button.value #while the button state is not the same as led state, perform action??
    time.sleep(0.5) # for some reason, the light turns on when the button is pressued
    print("led: " + str(led.value)) # the button is in the DOWN state I assume when pressed
    print("button: " + str(button.value))
    