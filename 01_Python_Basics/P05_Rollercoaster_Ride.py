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
    pic_consent = input("Do you want the pictures too?\n")

    if age < 12:

        if pic_consent == "Yes" :
            print("You have to pay $8 for the ride")
        else:
            print("You have to pay $5 for the ride.")

    elif age > 18:

        if pic_consent == "Yes" :
            print("You have to pay $15 for the ride")
        else:
            print("You have to pay $12 for the ride.")

    else:
        if pic_consent == "Yes" :
            print("You have to pay $10 for the ride")
        else:
            print("You have to pay $7 for the ride.")

else:
    print("You can't ride the rollercoaster!")