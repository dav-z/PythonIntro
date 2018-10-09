##  Lab 5
##  CIS 1051
##      David Zheng
##      February 23, 2018

import os
import datetime as dt
import math

Ask = True
while Ask:
    destination = str(input("What is your desired destination? Choose from the Following: \n" +
                    "P: Princeton \n" + "N: New York City \n" + "B: Baltimore \n" +
                    "W: Washington \n" + "L: Lancaster \n" + "H: Harrisburg \n"))
    destination = destination[0].upper()
    destinationList = ["P", "N", "B", "W", "L", "H"]
    if destination in destinationList:
        if destination == "P":
            print("Please catch a Northbound train to Princeton.")
            place = 'Princeton'
            direction = 'Northbound'
            miles = 45
            price = 5 + (miles * 0.5)
            stop = '1st'
        elif destination == "N":
            print("Please catch a Northbound train to New York City.")
            place = 'New York City'
            direction = 'Northbound'
            miles = 98
            price = 10 + (miles * 0.5)
            stop = '2nd'
        elif destination == "B":
            print("Please catch a Southbound train to Baltimore.")
            place = 'Baltimore'
            direction = 'Southbound'
            miles = 80
            price = 5 + (miles * 0.5)
            stop = '1st'
        elif destination == "W":
            print("Please take a Southbound train to Washington.")
            place = 'Washington'
            direction = 'Southbound'
            miles = 115
            price = 10 + (miles * 0.5)
            stop = '2nd'
        elif destination == "L":
            print("Please take a Westbound train to Lancaster.")
            place = 'Lancaster'
            direction = 'Westbound'
            miles = 70
            price = 5 + (miles * 0.5)
            stop = '1st'
        elif destination == "H":
            print("Please take a Westbound train to Harrisburg.")
            place = 'Harrisburg'
            direction = 'Westbound'
            miles = 105
            price = 5 + (miles * 0.5)
            stop = '2nd'
        Ask = False
    else:
        print("Please enter a valid destination")
        Ask = True


now = dt.datetime.now()
if (now.hour > 19) or (now.hour < 2.15) or (now.hour < 6) or (now.hour < 6.05) or (now.hour < 6.10):
    price = str(price - (price * 0.1))
else:
    price = str(price)
if not ((now.hour > 3) and (now.hour < 5.3)):
    if direction == "Northbound":
        traintime = now.hour + 1
        if traintime >= 12:
            traintime = traintime - 12
            traintime = str(traintime) + ":00"
            daytimeabb = "PM."
        else:
            traintime = str(now.hour + 1) + ":00"
            daytimeabb = "AM."
    elif direction == "Southbound":
        traintime = now.hour + 1
        if now.minute < 5:
            traintime = now.hour
        if traintime >= 12:
            traintime = traintime - 12
            traintime = str(traintime) + ":05"
            daytimeabb = "PM."
        else:
            traintime = str(now.hour + 1) + ":05"
            daytimeabb = "AM."
    elif direction == "Westbound":
        traintime = now.hour + 1
        if now.minute < 10:
            traintime = now.hour
        if traintime >= 12:
            traintime = traintime - 12
            traintime = str(traintime) + ":10"
            daytimeabb = "PM."
        else:
            traintime = str(now.hour + 1) + ":10"
            daytimeabb = "AM."
    print("Your next train leaves at " + traintime + daytimeabb)
    print(place + " is the " + stop + "stop.")
    print("Your fare is $" + price + ".")

else:
    print("Sorry, please wait until the morning for the next available train.")
