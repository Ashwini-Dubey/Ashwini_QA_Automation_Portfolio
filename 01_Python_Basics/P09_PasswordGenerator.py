import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
pw_letters = int(input("How many letter would like in your password?\n"))
pw_symbols = int(input("How many symbols would you like?\n"))
pw_numbers = int(input("How many numbers would you like?\n"))

#Easy Version
pass_gen_easy = ""

for char in range(0,pw_letters):
    pass_gen_easy+=random.choice(letters)

for num in range(0,pw_numbers):
    pass_gen_easy+=random.choice(numbers)

for sym in range(0,pw_symbols):
    pass_gen_easy+=random.choice(symbols)

print(pass_gen_easy)
