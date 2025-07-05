#!/usr/bin/env python3
"""
Band Name Generator

This simple script generates a band name by combining the name of a city the user grew up in
with the name of their pet. It’s an introductory Python project for practicing input/output
operations and string manipulation.

Concepts Used:
1. Print Statement.
2. Variables & Usage

Author: Ashwini Dubey
Date: July 2025
"""

print("Welcome to the Brand Name Generator.")
user_city = input("What is the name of the city you have grew up in?\n")
user_pet_name = input("What is the name of your pet?\n")
band_name = user_city + " " + user_pet_name
print("Your band name could be ",band_name)
print("Thank you for using the Band Name Generator.")