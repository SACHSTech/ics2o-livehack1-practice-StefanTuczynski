"""
Name: minutes_days.py
Purpose: Convert a set amount of minutes into days.

Author: Stefan Tuczynski

Date: 03/12/2020
"""

#takes minutes given from user
print("--- Welcome to the online minutes to days converter ---")
minutes = int(input("Amount of minutes: "))

#processing data given from user 
days = (minutes / 1440)

#outputting amount of days
print(minutes,"minutes equals:",days,"days")
print("--- Thank you for using the online minutes to days converter! ---")

