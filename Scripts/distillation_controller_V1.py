# Title: Distillation_Controller_V1
# Author: Brayden Dodson
# Equipment: Raspberry Pi 4B+, PT100 RTD, MAX31865 Amplifier, 1/2" SS Motorized Ball Valve
# Equipment Cont: 12V Relay, 12V Power Supply, Jumper Wires, and a Distillation Rig


# This program is intended to control a distillation operation
# such that a target temperature at the head (top of the still
# before the condenser), can be maintained. The temperature of
# the vapor at this point is monitored by a pt100 RTD sensor
# and then used to actuate a ball valve that regulates flow to
# a dephlegmator. The ball valve flow will not be linear, so
# "magic numbers" are likely used for V1 of this program.

##### Import Dependencies ######
from time import sleep
import board # Pin selection with be BCM (Broadcom) instead of board pin #s
import digitalio # Controls the IO for the board
import adafruit_max31865 # Breakout board that amplifies the signal from the RTD

######### Resistance Temperature Detector (RTD) Initialization Section ########

spi = board.SPI() # Create sensor object, communicating over the board's default SPI bus
cs = digitalio.DigitalInOut(board.D5)  # Chip select of the MAX31865 board.

# Note you can optionally provide the thermocouple RTD nominal resistance (PT resistance), the reference
# resistance of the MAX31865 board, and the number of wires for the sensor (2 the default, 3, or 4).
sensor = adafruit_max31865.MAX31865(spi, cs, rtd_nominal=100, ref_resistor=431.0, wires=3)

######## LED Change Detecting Signaling Initialization Section #######
led = digitalio.DigitalInOut(board.D14) # Select D18 as the LED signal output pin
led.direction = digitalio.Direction.OUTPUT # Initialize the pin in the program as an OUTPUT pin

####### Ball Valve Relay Initialization Section #####
ball_relay_open = digitalio.DigitalInOut(board.D15) # Assign open relay chip select to BCM GPIO_14
ball_relay_open.direction = digitalio.Direction.OUTPUT
ball_relay_open.value = True

####### Ball Valve Relay Initialization Section #####
ball_relay_close = digitalio.DigitalInOut(board.D18) # Assign close relay chip select to BCM GPIO_15
ball_relay_close.direction = digitalio.Direction.OUTPUT
ball_relay_open.value = True

###### Open Valve ########
def open_valve():
    ball_relay_open.value = True
    ball_relay_close.value = False
    
###### Close Valve #######
def close_valve():
    ball_relay_open.value = False
    ball_relay_close.value = True
    
###### Pause Valve #######
def pause_valve():
    ball_relay_open.value = True
    ball_relay_close.value = True
    
    
###### Loop to take INPUT from RTD and send OUTPUT to LED ######

while True:
    temp = sensor.temperature # create a temperature object
    res = sensor.resistance # create a resistance object
    
    tgt_temp = 29.00 #Set this to process spec
    ctrl_limit = 1 # Control Limit range (deg C)
    
    ucl = tgt_temp + ctrl_limit
    lcl = tgt_temp - ctrl_limit
    
    print("Current Temp: {0:0.3f}C.".format(temp))
    # print("Resistance: {0:0.3f}Ohm".format(res)) #print the resistance for information purposes
    
    if temp >= (ucl):
        led.value = True
        open_valve()
        # Print the value.
        print("Reducing temperature now.\n")
        
    elif temp <= lcl:
        led.value = True
        close_valve()
        # Print the value.
        print("Increasing temperature now.\n")
        #ball_relay.value = False
    else:
        led.value = False
        pause_valve()
        print("Temperature is within control limits\n")
    
    ### Likely a place for a PID variable later and can be included in the elif blocks ######
    sleep(2) # Let the valve actuate for 2 seconds (either direction or paused).
    pause_valve() #Always disengage the relay after valve actuation
    
    for i in range(0,5):
        print(i)
        sleep(1) #Wait i seconds before retesting. Let the system equilibrate to whatever change 
    led.value = False
