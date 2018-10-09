##  Lab 4 Weather Report
##      CIS 1051
##          February 16, 2018
##  David Zheng

import datetime as dt
import os

location = input('Where are you?\n')
fahrenheit = round(float(input('What is the temperature in Fahrenheit?\n')), 1)
celcius = round((float(fahrenheit)-32)*(5/9), 1)
wind = round(float(input('What is the wind speed in mph?\n')), 1)
precip = input('Is it \"raining\", \"snowing\", or \"none?\"\n')
now = dt.datetime.today()
date_formatted = now.strftime(' %b %d %Y ')
dd = dt.datetime(2018,3,20) - now
hours = round(dd.days*24 + (dd.seconds)/(60*60), 1)
msg = "Location: %s \nDate: %s \nHours Till Spring: %.1f \nTemperature(Fahrenheit): %0.1f \nTemperature(Celcius): %.1f \nWind Speed(mph): %.1f \nPrecipitation: %s" %(location, date_formatted, hours, fahrenheit, celcius, wind, precip)

print(msg)

if fahrenheit < 50.0 :
    windchill = round(float(35.74 + 0.6125 * fahrenheit - 35.75*(wind**0.16) + 0.4275*fahrenheit*(wind**0.16)), 1)
    if windchill < 40.0 :
        if precip == "none" :
            print("Windchill: %.1f \nWARNING: Windchill is less than 40!" %windchill)
        elif precip == "raining" :
            print("Windchill: %.1f \nWARNING: Windchill is less than 40!\nRemember to bring an umbrella!" %windchill)
        elif precip == "snowing" :
            print("Windchill: %.1f \nWARNING: Windchill is less than 40!\nRemember to dress warmly!" %windchill)
    else :
        if precip == "raining" :
            print("Windchill: %.1f \nRemember to bring an umbrella!" %windchill)
        elif precip == "snowing" :
            print("Windchill: %.1f \nRemember to dress warmly!" %windchill)
        elif precip == "none" :
            print("Windchill: %.1f" %windchill)
else :
    if precip == "raining" :
        print("Remember to bring an umbrella!")
    elif precip == "snowing" :
        print("Remember to dress warmly!")
