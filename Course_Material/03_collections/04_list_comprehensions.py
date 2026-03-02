"""
Topic: List Comprehension
Section: Collections
Description:
List comprehension = A concise way to create lists in Python
                     Compact and easier to read than traditional loops
                     [expression for value in iterable if condition]
"""

# -------- DOUBLE THE NUMBER --------
# ------- Method 01: -------
doubles = []
for x in range(1, 11):
    doubles.append(x + x)
print(doubles)

# ------- Method 02: -------
doubles = [x+x for x in range(1, 11) if x < 6]
print(doubles)

# -------- TRIPLES THE NUMBER --------
triples = [y+y+y for y in range(1, 11)]
print(triples)

# -------- SQAURE THE NUMBER --------
square = [z*z for z in range(1,11)]
print(square)

# ------- UPPER CASE TO FRUITS LIST ---------
fruits = ["apple", "banana", "orange", "coconut"]
# make it upper case
fruits = [fruit.upper() for fruit in fruits]
print(fruits)

# ------- ONLY FIRST LETTER OF FRUITS -------
fruit_char = [fruit[0].upper() for fruit in ["banana", "papaya", "melon", "tomato"]]
print(fruit_char)

# ------- POSTIVE AND NEGATIVE SEPERATION -------
numbers = [1,-2,3,4,-5, 6]
positive = [num for num in numbers if num >= 0 ]
negative = [num for num in numbers if num < 0]
even_nos = [num for num in numbers if num%2 == 0]
odd_nos = [num for num in numbers if num%2 == 1]
print(f"Postive: {positive}")
print(f"Negative: {negative}")
print(f"Even: {even_nos}")
print(f"Odd: {odd_nos}")

# -------- GRADES SELECTION --------
grades = [85, 42, 79, 90, 56, 61, 30]
passing_grads = [grade for grade in grades if grade >= 60]
print(f"Passing Grade: {passing_grads}")