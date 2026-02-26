"""
Topic: While Loop
Section: Control Flow
Description:
while loop = execute some code WHILE some condition remains true
"""

# ---------- Example 1 ----------

name = input("Enter you name: ")

while name == "":
    print("You did not enter your name.")
    name = input("Enter you name: ")

print(f"Hello {name}")

# ---------- Example 2 ----------
age = int(input("Enter your age: "))

while age <= 0:
    print("Age can't be negative")
    age = int(input("Enter your age: "))
print(f"You are {age} years old")

# ---------- Example 3 ----------
food = input("Enter a food you like (q to quit): ")

while not food == "q" :
    print(F"You like {food}.")
    food = input("Enter another food you like (q to quit): ")
print(f"Bye")

# ---------- Example 4 ----------
num = int(input("Enter a # betweeen 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid.")
    num = int(input("Enter a # betweeen 1 - 10: "))

print(f"Your number is {num}")