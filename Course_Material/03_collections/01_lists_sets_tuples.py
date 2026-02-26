"""
Topic: List, Set, Tuple
Section: Collections
Description:
Collection = A variable that stores multiple values.

List  []  -> Ordered, Changeable, Duplicates allowed
Set   {}  -> Unordered Immutable , No duplicates
Tuple ()  -> Ordered, Not changeable (Immutable)
"""

# ------------------ LIST ------------------

print("\n----- LIST -----")

fruits = ["apple", "mango", "banana", "papaya"]
print("Original List:", fruits)

# Access by index (position starts at 0)
print("First item:", fruits[0])

# Slicing (returns a new list)
print("Slice [0:3]:", fruits[0:3])

# Step slicing
print("Every 2nd item:", fruits[::2])

# Reverse using slicing
print("Reversed:", fruits[::-1])

# Loop through list
print("Looping items:", end=" ")
for fruit in fruits:
    print(fruit, end=" ")

print("\nLength:", len(fruits))
print("Is 'apple' in list?:", "apple" in fruits)

# Modify list (lists are changeable)
fruits[0] = "pineapple"
fruits.append("melon")
fruits.insert(2, "orange")
fruits.remove("pineapple")

print("After changes:", fruits)

fruits.sort()
print("Sorted:", fruits)

fruits.reverse()
print("Reversed again:", fruits)

print("Index of 'orange':", fruits.index("orange"))
print("Count of 'banana':", fruits.count("banana"))


# ------------------ SET ------------------

print("\n----- SET -----")

fruits_set = {"apple", "mango", "banana", "papaya"}
print("Original Set:", fruits_set)

print("Length:", len(fruits_set))
print("Is 'apple' in set?:", "apple" in fruits_set)

# Add and remove
fruits_set.add("coconut")
print("After adding coconut:", fruits_set)

fruits_set.remove("banana")
print("After removing banana:", fruits_set)

print("Popped item:", fruits_set.pop())
print("Set now:", fruits_set)


# ------------------ TUPLE ------------------

print("\n----- TUPLE -----")

fruits_tuple = ("apple", "mango", "banana", "papaya")
print("Original Tuple:", fruits_tuple)

print("Length:", len(fruits_tuple))
print("Is 'apple' in tuple?:", "apple" in fruits_tuple)

print("Index of 'papaya':", fruits_tuple.index("papaya"))
print("Count of 'banana':", fruits_tuple.count("banana"))

# Loop through tuple
print("Looping items:", end=" ")
for fruit in fruits_tuple:
    print(fruit, end=" ")
    

# to get any method and their detail description
# print(dir(variable_name))
# print(help(variable_name))