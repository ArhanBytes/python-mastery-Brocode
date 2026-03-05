"""
Topic: Intro to OOP
Section:  Oriented Programming
Description:
# object = A "bundle" of related attributes (variables) and methods (functions)
#     Ex. phone, cup, book
#     You need a "class" to create many objects
# class = (blueprint) used to design the structure and layout of an object
"""

# ----- MAKING CLASS -----
# classes can take lot of space(lines) for better organization write in new python file
from car import Car 

car1 = Car("Mustang", "2026", "red", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Charger", 2026, "yellow", True)

# ATTRIBUTES
print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)
# METHODS
car1.drive()
car2.stop()

car1.describe()
car2.describe()
car3.describe()