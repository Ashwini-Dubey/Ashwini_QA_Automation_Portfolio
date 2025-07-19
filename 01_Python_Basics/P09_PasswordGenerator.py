import random

# List of all possible characters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ----------------------------------------
# PyPassword Generator
# ----------------------------------------
"""
This script generates two types of passwords:
1. Easy Level Password: Characters are added in a fixed sequence (letters, numbers, symbols).
2. Hard Level Password: Characters are randomly shuffled for higher security.

It asks the user how many letters, symbols, and numbers they want in their password.
"""

print("Welcome to the PyPassword Generator!")

# Take user input for number of letters, symbols, and numbers
pw_letters = int(input("How many letter would like in your password?\n"))
pw_symbols = int(input("How many symbols would you like?\n"))
pw_numbers = int(input("How many numbers would you like?\n"))

# -------------------- Easy Version --------------------
# Characters are not shuffled: letters -> numbers -> symbols
pass_gen_easy = ""

# Add random letters
for char in range(0, pw_letters):
    pass_gen_easy += random.choice(letters)

# Add random numbers
for num in range(0, pw_numbers):
    pass_gen_easy += random.choice(numbers)

# Add random symbols
for sym in range(0, pw_symbols):
    pass_gen_easy += random.choice(symbols)

print("Easy Level Password: ", pass_gen_easy)

# -------------------- Hard Version --------------------
# Characters are shuffled after selection
pass_gen_hard = []

# Add random letters
for char in range(0, pw_letters):
    pass_gen_hard.append(random.choice(letters))

# Add random numbers
for num in range(0, pw_numbers):
    pass_gen_hard.append(random.choice(numbers))

# Add random symbols
for sym in range(0, pw_symbols):
    pass_gen_hard.append(random.choice(symbols))

# Shuffle the entire list to randomize the order
random.shuffle(pass_gen_hard)

# Convert list to string
pass_hard = ""
for char in pass_gen_hard:
    pass_hard += char

print("Hard Level Password: ", pass_hard)
