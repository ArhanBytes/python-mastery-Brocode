"""
Topic: Iterables
Section: Collections

Description:
Iterables = An object/collection that can return its elements one at a time,
            allowing it to be iterated over in a loop
"""

# ---------- LIST ----------

numbers = [1, 2, 3, 4, 5]

# for every number in iterable
for number in reversed(numbers):
    print(number, end=" ")
    
# ---------- TUPLE ----------
numbers = (1, 2, 3, 4, 5)
# for every number in my iterable
for number in numbers:
    print(number)
    
# ---------- SETS ----------
fruits = {"apple", "banana", "orange", "coconut"}
for fruit in fruits:
    print(fruit)

# ---------- STRINGS ----------
name = "ARHAN IMRAN"
# for every character in my iterable(string)
for character in name:
    print(character, end=" ")
    
print()

# ---------- STRINGS ----------
my_dictionary = {"A":1, "B":2, "C":3}
# printing only key
# for every key in dectionary
print("Printing keys:")
for key in my_dictionary:
    print(key)
# printing only value
# for every value in dectionary
print("Printing values:")
for value in my_dictionary.values():
    print(value)
    
# printin key and value both
# for every key and value in dectionary
for key, value in my_dictionary.items():
    print(f"{key} = {value}")