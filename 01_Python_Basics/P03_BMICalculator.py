"""
BMI Calculator

This script prompts the user for their body weight (in kilograms) and height (in metres),
calculates the Body Mass Index (BMI) using the formula  BMI = weight / height², rounds the
result to the nearest whole number, and displays it.

Inputs
------
weight : float
    User’s body weight in kilograms.
height : float
    User’s height in metres.

Output
------
A single line printed to the console showing the computed BMI, rounded to the nearest integer.

Author : Ashwini Dubey
Date   : July 2025
"""

print("Welcome to the BMI Calculator.")
weight = float(input("What is your body weight?\n"))
height = float(input("What is your height?\n"))
bmi = round(weight / (height ** 2))
print(f"Your BMI (Body Mass Index) is : {bmi}")