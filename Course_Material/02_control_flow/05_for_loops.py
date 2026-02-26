"""
Topic: For Loop
Section: Control Flow
Description:
Demonstrates how to use for loops to iterate over ranges and sequences,
including forward counting, backward counting, stepping, and loop control
using break and continue.
"""

# What range() does
# The range() function generates a sequence of numbers.
# Its general form is:
# range(start, stop, step)
# start: The first number in the sequence (included).
# stop: The sequence stops before this number (not included).
# step: How much to increase (or decrease) each time.

# ----- Counting Forward -----
# range(start, stop) → stop value is excluded
for x in range(1, 11):
    print(x)

print("HAPPY NEW YEAR!")


# ----- Counting Backward -----
# reversed() allows us to iterate in reverse order
for x in reversed(range(1, 11)):
    print(x)

print("HAPPY NEW YEAR!")


# ----- Using Step in range() -----
# range(start, stop, step) → increments by step value
for x in range(1, 11, 2):
    print(x)

print("HAPPY NEW YEAR!")


# ----- Iterating Through a String -----
# A string is a sequence, so we can loop through each character
credit_card = "1234-5678-8543-4521"

for char in credit_card:
    print(char)

print("HAPPY NEW YEAR!")


# ----- Using continue -----
# continue skips the current iteration and moves to the next one
for x in range(1, 21):
    if x == 13:
        continue  # skip number 13
    print(x)


# ----- Using break -----
# break immediately stops the loop
for x in range(1, 21):
    if x == 13:
        break  # stop loop when x becomes 13
    print(x)