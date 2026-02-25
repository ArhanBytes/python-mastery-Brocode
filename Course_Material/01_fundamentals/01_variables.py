"""
Topic: Variables
Section: Fundamentals
Description: A container for a value (string, integer, float, boolean). A variable behaves as if it was the value it contains
"""

#--------------STRING--------------
first_name = "Arhaan"
food = "Shawarma"
email = "muhammadarhan7t6@gmail.com"
print(first_name)

# f-string: To use formatted string literals, begin a string with f or F before the opening quotation mark or triple quotation mark. Inside this string, you can write a Python expression between { and } characters that can refer to variables or literal values.

print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is: \"{email}\"")

#--------------INTEGERS--------------
age = 21 
quantity = 3
num_of_students = 30

print(f"You are {age} years old")
print(f"You are purchasing {quantity} items")
print(f"Your class has {num_of_students} students")

#--------------FLOATS--------------
price = 10.99
gpa = 3.8
distance = 5.5

print(f"The price is: {price}")
print(f"Your GPA is: {gpa}")
print(f"You ran {distance} km")

#--------------BOOLEAN--------------
is_student = True
for_sale = True
is_online = False
 
print(f"Are you a student?: {is_student}")

# for is_student
if is_student:
    print("You are a student")
else:
    print("You are not a student")
    
# for sale
if for_sale:
    print("That item is for sale")
else:
    print("That item is not available")

# check online or offline
if is_online:
    print("You are online")
else:
    print("You are offline")