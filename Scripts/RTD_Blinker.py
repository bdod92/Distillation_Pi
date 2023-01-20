# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple demo of the MAX31865 thermocouple amplifier.
# Will print the temperature every second.
import time
import board
import digitalio
import adafruit_max31865

######### Resistance Temperature Detector (RTD) Initialization Section ########
# Create sensor object, communicating over the board's default SPI bus
spi = board.SPI()
cs = digitalio.DigitalInOut(board.D5)  # Chip select of the MAX31865 board.
#sensor = adafruit_max31865.MAX31865(spi, cs)
# Note you can optionally provide the thermocouple RTD nominal, the reference
# resistance, and the number of wires for the sensor (2 the default, 3, or 4)
# with keyword args:
sensor = adafruit_max31865.MAX31865(spi, cs, rtd_nominal=100, ref_resistor=431.0, wires=3)

######## LED Change Detecting Signaling Initialization Section #######
led = digitalio.DigitalInOut(board.D18)
led.direction = digitalio.Direction.OUTPUT


####### Loop to take INPUT from RTD and send OUTPUT to LED ######

while True:
    # Read temperature.
    temp = sensor.temperature
    res = sensor.resistance
    tgt_temp = 30 #Set this to process spec
    
    if temp > tgt_temp:
        led.value = True
        # Print the value.
        print("Above 30: {0:0.3f}C".format(temp))
        # print("Resistance: {0:0.3f}Ohm".format(res))
        # Delay for a second.
        time.sleep(1.0)
    elif temp <= tgt_temp:
        led.value = False
        # Print the value.
        print("Beloww 30: {0:0.3f}C".format(temp))
        # print("Resistance: {0:0.3f}Ohm".format(res))
        # Delay for a second.
        time.sleep(1.0)
    else:
        print("Error")
        time.sleep(1.0)
