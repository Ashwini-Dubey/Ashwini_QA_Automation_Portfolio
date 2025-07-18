"""
FizzBuzz Program

This script prints numbers from 1 to 100 with the following rules:
- If a number is divisible by both 3 and 5, print "FizzBuzz"
- If a number is divisible by 3 only, print "Fizz"
- If a number is divisible by 5 only, print "Buzz"
- Otherwise, print the number itself

Used commonly as a basic programming exercise to demonstrate control flow and modulo operations.
"""
for number in range(1,101):

    if number%3==0 and number%5==0:
        print("FizzBuzz")

    elif number%3==0:
        print("Fizz")

    elif number%5==0:
        print("Buzz")

    else:
        print(number)
