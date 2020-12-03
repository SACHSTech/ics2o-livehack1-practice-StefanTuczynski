"""
Name:   windchill.py
Purpose: to take the tempurature (celcius) and the wind speed (km/h) 

Author: Tuczynski.S

Date:   03/12/2020
"""

#gets information on degrees and windspeed from user 
print("--- Welcome to the online Windchill converter! ---")
temp = float(input("Degrees Celcius: "))
speed = float(input("Wind speed (km/h): "))

#processing the equation
windchill = (13.12 + (temp * 0.6215) - (11.36 * (speed ** 0.16)) + (0.3965 * temp * (speed ** 0.16)))

#outputs information back to user
print("The calculated windchill is:", round(windchill))
print("--- Thank you for using the online Winchill calculator! ---")