#!/usr/bin/env python3

"""
Tip Calculator

This script calculates how much each person should pay when a bill is split among multiple people,
including a specified tip amount. It prompts the user for the total bill, tip amount, and number
of people splitting the bill, then outputs the per-person amount with two decimal precision.

Author: Ashwini Dubey
Date: July 2025
"""

print("Welcome to the Tip Calculator.")
bill_amount = float(input("What was the total bill?\nINR "))
tip_amount = float(input("How much tip would you like to give?\nINR "))
people_split = int(input("How many people to split the bill?\n"))
per_person_pay = round(((bill_amount + tip_amount)/people_split),2)
print("Each person should pay : INR", per_person_pay)
