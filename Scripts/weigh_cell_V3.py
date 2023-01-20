#Weigh cell third pass
#This version does not use the tare function because it is more consistent to use the same weight for the jar

#Need to add in a red light / green light for removal and replacement of the jar. Set the time between readings to
# 10 seconds, and the green window to the middle 5 seconds, or whatever is best

#Need to add in RTD temp probe readings, ball valve, servo, distance sensor, and flow meter still

# You can parallel process in python using the threading function (See quora)

import time
import sys
import RPi.GPIO as GPIO
from hx711 import HX711
# from emulated_hx711 import HX711

#start a counter
counter = 0
#start a timer
t0 = time.time()

#weight function returns the current weight
def weight():
    #! /usr/bin/python2

    EMULATE_HX711=False
    referenceUnit = 460.5

    hx = HX711(26, 6)
    hx.set_reading_format("MSB", "MSB")
    hx.set_reference_unit(referenceUnit)
   
    gram = int(hx.get_weight(5))
    return gram
                  

#temp function returns the current temp
def temperature():
    temp = 27
    return temp

#take the tare weight and store it for later use
# tare_weight = weight()
jar_count = 0

while True:
    jar_count += 1
    new_jar=True
    jar_tare_wt = weight()
    start_wt = weight() - jar_tare_wt
    end_wt = weight() - jar_tare_wt
    
    #if the weight decreases by >250g restart the new jar cycle
    while new_jar:
        try:
            #take a starting weight for the cycle
            start_wt = weight() - jar_tare_wt
            elap_time = round(time.time() - t0)

            #Call the record temp function and save into the temp variable
            temp = temperature()
            #call the record weight function and save it into the weight variable
            #send the temp to the temp df with the elapsed time.

            #Record, calculate, and send all of the data for ABV calcs to a df (separate from the temp df)
            if counter == 4: #executes every 60 seconds
                print("execute data transfer")
                #volume = call volume function (return volume)
                #weight = call the weight function (return weight)
                #density = call the density function (pass in volume, weight, temperature and return density adjusted for temp)
                #call the store values function. Send all of the above data to separate, wholistic df. Will combine data later when values can be interpolated.
                counter = 0
            counter += 1

            print("jar_tar weight pre-if: " + str(jar_tare_wt))
            print("start weight pre-if: " + str(start_wt))
            print("end weight pre-if: " + str(end_wt))
            print("tare_check pre-if: " + str(new_jar))
            
            time.sleep(5)
            end_wt = weight() - jar_tare_wt
            
            #this value 250 should be set to the maximum weight difference between jars plus some buffer
            #You could include a an input field and sub in a variable, or just hard code it with some magic numbers
            if (start_wt-250)>(end_wt):
                new_jar = False
                
            print("start weight post -if: " + str(start_wt))
            print("end weight post-if: " + str(end_wt))
            print("tare_check psot-if: " + str(new_jar))
            print(elap_time, jar_count, start_wt, end_wt, temp)
            print("---------------------------------")
            print("")
            
        except (KeyboardInterrupt, SystemExit):
            print('outer loop broken')
            GPIO.cleanup()
            sys.exit()
    print("cycle broken n = " + str(jar_count) + " times")
    print("")