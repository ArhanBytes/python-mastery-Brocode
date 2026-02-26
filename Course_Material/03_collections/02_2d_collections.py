"""
Topic: 2D List (Nested Collections)
Section: Collections

Description:
A 2D list is a collection inside another collection.
It is like a table (rows and columns).

- First index  -> selects the row
- Second index -> selects the item inside that row

Syntax:
collection[row][column]
"""

# ------------------ Example 1: Using Separate Lists ------------------

fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

# Method 1: Combine existing lists into a 2D list
groceries = [fruits, vegetables, meats]

# Access entire row (1 index)
print(groceries[0])        # returns fruits list

# Access specific element (2 indices)
print(groceries[0][0])     # returns "apple"


# ------------------ Method 2: Direct 2D List ------------------

groceries = [
    ["apple", "orange", "banana", "coconut"],
    ["celery", "carrots", "potatoes"],
    ["chicken", "fish", "turkey"],
]

# Iterate through 2D list
for row in groceries:
    for item in row:
        print(item, end=" ")
    print()


# ------------------ Other Combinations ------------------

# Tuples inside a list (outer list is changeable)
groceries = [
    ("apple", "orange", "banana", "coconut"),
    ("celery", "carrots", "potatoes"),
    ("chicken", "fish", "turkey"),
]

# 2D Tuple (fully immutable)
groceries = (
    ("apple", "orange", "banana", "coconut"),
    ("celery", "carrots", "potatoes"),
    ("chicken", "fish", "turkey"),
)

# Sets inside a tuple (unordered inside each row)
groceries = (
    {"apple", "orange", "banana", "coconut"},
    {"celery", "carrots", "potatoes"},
    {"chicken", "fish", "turkey"},
)

# Many combinations are possible:
# list of lists, list of tuples, tuple of lists, etc.


# ------------------ Exercise: 2D Numerical Keypad ------------------

# Using tuple (ordered and not changeable)

num_pad = (
    (1, 2, 3), 
    (4, 5, 6), 
    (7, 8, 9), 
    ("*", 0, "#")
)

for row in num_pad:
    for num in row:
        print(num, end="\t")
    print()