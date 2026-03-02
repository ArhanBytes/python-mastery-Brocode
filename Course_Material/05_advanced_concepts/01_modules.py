"""
Topic: Modules
Section: Advanced Concept

module = a file that contains code
use 'import' to use code from another file
helps organize and reuse code
"""

# -------- VIEW AVAILABLE MODULES --------
# help("modules")

# -------- VIEW FUNCTIONS INSIDE A MODULE --------
# help("math")


# -------- IMPORT ENTIRE MODULE --------
import math
print(math.pi)


# -------- IMPORT WITH ALIAS --------
import math as m
print(m.pi)


# -------- IMPORT SPECIFIC ITEM --------
from math import pi
print(pi)


# -------- USING MODULE ATTRIBUTES --------
a, b, c, d, e = 1, 2, 3, 4, 5

print(math.e ** a)
print(math.e ** b)
print(math.e ** c)
print(math.e ** d)
print(math.e ** e)


# -------- IMPORT CUSTOM MODULE --------
import math_module

print("Pi:", math_module.pi)
print("Square of 5:", math_module.square(5))
print("Cube of 5:", math_module.cube(5))
print("Circumference (r=5):", math_module.circumference(5))
print("Area (r=5):", math_module.area(5))