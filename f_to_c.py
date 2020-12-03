"""
Name: f_to_c.py
Purpose: To convert a set amount of degrees farienheight to a
set amount of degrees celcius.

Author: Stefan Tuczynski

Date: 03/12/2020
"""

#Asks user for the amount of degrees farienheight
print("--- Welcome to the online farienheight to celcius converter ---")
f = float(input("Degrees Farienheight: "))

#Tells user the amount of degrees celcius after conversion
print(f , "degrees farienheight equals", float((f - 32) * (5/9) ), "degrees celcius.")
print("--- Thank you for using the online farienheight to celcius conveter! ---")