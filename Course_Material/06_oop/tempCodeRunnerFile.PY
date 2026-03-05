"""
Topic: Super()
Section: Object Oriented Programming
Description:
super() = Function used in a child class to call methods from a parent class (superclass).
          Allows you to extend the functionality of the inherited methods
"""


class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled


# In programming we do not want to repeat ourselves. Here color and filled is repeating. Therefore we make another class name shape
class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius


class Square(Shape):
    def __init__(self, color, is_filled, side):
        super().__init__(color, is_filled)
        self.side = side


class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

circle = Circle("Green", True, 5.5)
sqaure = Square(color="Red", is_filled=False, side=2.4)

print("Circle: ")
print(circle.color)
print(circle.is_filled)
print(f"Radius: {circle.radius}cm")

print("\nSquare: ")
print(sqaure.color)
print(sqaure.is_filled)
print(f"{sqaure.side}cm")