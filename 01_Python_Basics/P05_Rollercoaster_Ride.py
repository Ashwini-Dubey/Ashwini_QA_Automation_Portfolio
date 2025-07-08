"""
Rollercoaster Ticketing Script
------------------------------
A small console program that determines whether a user can ride a
roller‑coaster and, if so, how much they must pay for a ticket.

Concepts Used:
1. If-else statements
2. Nested If-else statements.

"""

print("Welcome to the Rollercoaster!")
height = int(input("What is your height (in cm)?\n"))

if height > 120:
    print("You can ride the rollercoaster!")

    age = int(input("What is your age?\n"))

    if age < 12:
        print("You have to pay $5 for the ride")

    elif age > 18:
        print("You have to pay $12 for the ride.")

    else:
        print("You have to pay $7 for the ride.")
else:
    print("You can't ride the rollercoaster!")