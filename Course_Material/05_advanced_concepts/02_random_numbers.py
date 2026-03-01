"""
Topic: Random Numbers
Section: Advanced Concept
Description:
The random module is used to generate random numbers and make random selections.
It is commonly used in games, simulations, and testing.
"""

import random


# --- View all available functions in random module ---
# print(help(random))


# --- Generate a random whole number (integer) ---
# randint(start, end) → returns an integer between start and end (inclusive)

low = 1
high = 100
number = random.randint(low, high)
print(f"Random Integer between {low} and {high}: {number}")


# --- Generate a random floating-point number ---
# random() → returns a float between 0.0 and 1.0

number = random.random()
print(f"Random Float between 0 and 1: {number}")


# --- Select a random item from a collection ---
# choice(sequence) → returns one random element

options = ("Rock", "Paper", "Scissors")
option = random.choice(options)
print(f"Random Choice: {option}")


# --- Shuffle a list (changes original list order) ---
# shuffle(list) → rearranges elements randomly
# Note: shuffle works only on mutable sequences like lists

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

print(f"Before Shuffle: {cards}")
random.shuffle(cards)
print(f"After Shuffle: {cards}")