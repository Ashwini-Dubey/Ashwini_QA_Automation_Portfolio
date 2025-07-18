"""
Find the Highest Student Score

This script iterates through a list of student scores and identifies the highest score.
It uses a simple loop and comparison logic to find the maximum value without using built-in functions like max().

Useful for understanding basic control flow and conditional logic in Python.
"""

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 99, 78, 65, 89, 86, 55, 91, 64, 89]

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)

# This script calculates the sum of all numbers from 1 to 99.
# It uses a for-loop and a cumulative total variable to perform the addition.

total = 0
for number in range(1,100):
    total+=number
print(total)
