#Weigh cell first pass
import time
import sys
import RPi.GPIO as GPIO
from hx711 import HX711
# from emulated_hx711 import HX711

#Pin Assigments


#start a counter
counter = 0
#start a timer
t0 = time.time()

#weight function returns the current weight
def weight(tare_check):
    #! /usr/bin/python2

    EMULATE_HX711=False
    referenceUnit = 460.5
#   sys.exit()

    hx = HX711(26, 6)
    hx.set_reading_format("MSB", "MSB")
    hx.set_reference_unit(referenceUnit)
#     hx.reset()

    if tare_check == 1:
        hx.tare()
        print("Tare done! Add weight now...")

    while True:
#         try:
        gram = int(hx.get_weight(5))
        return gram
        
#         except (KeyboardInterrupt, SystemExit):
#             print('no')
#             GPIO.cleanup()
#             sys.exit()
            
            # Prints the weight. Comment if you're debbuging the MSB and LSB issue.
#             gram = int(hx.get_weight(5))
#             print(str(gram) + ' grams')
#             lbs = round(gram/453.592,2)
#             print(str(lbs) + ' lbs')
#             print()            

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
    tare_check = 0
    jar_tare_wt = weight(tare_check)
    end_wt = weight(tare_check)
    tare_check = 0
    print("Start weight: " + str(start_wt))
    print("End weight: " + str(end_wt))
    time.sleep(5)
    
    start_wt = weight(tare_check)
    end_wt = weight(tare_check)
    print("Start weight: " + str(start_wt))
    print("End weight: " + str(end_wt))
    print('_______________')
    time.sleep(5)
    
    #if the weight decreases by >250g restart the new jar cycle
#     while new_jar:
#         try:
#             #take a starting weight for the cycle
#             start_wt = weight(tare_check)
#             elap_time = round(time.time() - t0)
# 
#             #Call the record temp function and save into the temp variable
#             temp = temperature()
#             #call the record weight function and save it into the weight variable
#             #send the temp to the temp df with the elapsed time.
# 
#             #Record, calculate, and send all of the data for ABV calcs to a df (separate from the temp df)
#             if counter == 4: #executes every 60 seconds
#                 print("execute data transfer")
#                 #volume = call volume function (return volume)
#                 #weight = call the weight function (return weight)
#                 #density = call the density function (pass in volume, weight, temperature and return density adjusted for temp)
#                 #call the store values function. Send all of the above data to separate, wholistic df. Will combine data later when values can be interpolated.
#                 counter = 0
#             counter += 1
# 
#             print("start weight pre-if: " + str(start_wt))
#             print("end weight pre-if: " + str(start_wt))
#             print("tare_check pre-if: " + str(tare_check))
#             
#             time.sleep(3)
#             end_wt = weight(tare_check)
#             if (start_wt-250)>(end_wt):
#                 tare_check = 1
#                 new_jar = False
#             else:
#                 tare_check = 0
#             time.sleep(3)
#                 
#             print("start weight post -if: " + str(start_wt))
#             print("end weight post-if: " + str(start_wt))
#             print("tare_check pre-if: " + str(tare_check))
#             print(elap_time, jar_count, start_wt, end_wt, temp)
#             print("---------------------------------")
#             print("")
#             
#         except (KeyboardInterrupt, SystemExit):
#             print('outer loop broken')
#             GPIO.cleanup()
#             sys.exit()
#     print("cycle broken n = " + str(jar_count) + " times")
#     print("")
