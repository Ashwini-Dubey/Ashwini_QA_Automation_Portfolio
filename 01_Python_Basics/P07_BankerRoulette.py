"""
Random Friend Selector

This script selects one name at random from a predefined list of friends
using Python's built-in random module. It demonstrates the use of
random.choice(), which returns a randomly selected element from a non-empty sequence.

Ideal for simple random draws or selections from a list.
"""

import random

friends = ["Alice","Bob","Charlie","Daryl","Evelyn","Frank","Goose","Harvey","Irwin","Jack","Klause"]

print(random.choice(friends))