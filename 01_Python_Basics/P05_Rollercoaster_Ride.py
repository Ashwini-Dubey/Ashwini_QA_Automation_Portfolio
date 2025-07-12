"""
Rollercoaster Ride Eligibility and Pricing System

This program checks if a user is eligible to ride a rollercoaster based on their height.
If eligible, it then determines the ride cost based on the user's age and whether they want photos.

Logic:
- Minimum height to ride is 121 cm.
- Ticket pricing is age-based:
    - Under 12 years:
        - $5 (ride only)
        - $8 (with photos)
    - 13 to 18 years:
        - $7 (ride only)
        - $10 (with photos)
    - Above 18 years:
        - $12 (ride only)
        - $15 (with photos)
- If height is 120 cm or less, the user is not allowed to ride.

Inputs:
- height (in cm)
- age (in years)
- photo consent (Yes/No)

Output:
- Eligibility message
- Ride price based on age and photo option
"""


print("Welcome to the Rollercoaster!")
height = int(input("What is your height (in cm)?\n"))

if height > 120:
    print("You can ride the rollercoaster!")

    age = int(input("What is your age?\n"))
    pic_consent = input("Do you want the pictures too?\n")

    if age >= 45 and age <= 55:
            print("Your ride is free.")

    elif age < 12:

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