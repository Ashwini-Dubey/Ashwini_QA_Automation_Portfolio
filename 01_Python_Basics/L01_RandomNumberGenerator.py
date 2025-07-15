"""
This script demonstrates the use of the 'random' module in Python to generate different types of random numbers.

Functions Used:
- random.randint(a, b): Returns a random integer N such that a <= N <= b.
- random.random(): Returns a random float number between 0.0 and 1.0.
- random.uniform(a, b): Returns a random float N such that a <= N <= b.

Output:
- A random integer between 1 and 100.
- A random float between 0.0 and 1.0.
- A random float between 1 and 10.
"""

import random

random_integer = random.randint(1,100)
print(random_integer)

random_float_0_to_1 = random.random()
print(random_float_0_to_1)

random_uniform = random.uniform(1,10)
print(random_uniform)

# Coin Flip Simulator
#
# This script uses Python's random module to simulate a coin toss.
# It randomly prints either "Heads" or "Tails" each time it is run.

coin_toss = random.randint(0,100)
if coin_toss == 0:
    print("Heads")
else:
    print("Tails")