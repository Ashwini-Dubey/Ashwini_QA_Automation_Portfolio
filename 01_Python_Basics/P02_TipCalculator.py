#!/usr/bin/env python3

print("Welcome to the Tip Calculator.")
bill_amount = float(input("What was the total bill?\n"))
tip_amount = float(input("How much tip would you like to give?\n"))
people_split = int(input("How many people to split the bill?\n"))
per_person_pay = round(((bill_amount + tip_amount)/people_split),2)
print("Each person should pay :", per_person_pay)
