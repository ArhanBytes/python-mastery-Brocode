"""
Topic: Super()
Section: Object Oriented Programming
Description:
super() = Function used in a child class to call methods from a parent class (superclass).
          Allows you to extend the functionality of the inherited methods
"""


class Shape:
    def __init__(self, name, color, is_filled):
        self.name = name
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"This is {self.name}. It color is {self.color} and {'filled' if self.is_filled else 'not filled'}. ", end="")

# In programming we do not want to repeat ourselves. Here color and filled is repeating. Therefore we make another class name shape
class Circle(Shape):
    def __init__(self, name, color, is_filled, radius):
        super().__init__(name, color, is_filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f"It radius is {self.radius}cm")
class Square(Shape):
    def __init__(self, name, color, is_filled, side):
        super().__init__(name, color, is_filled)
        self.side = side

    def describe(self):
        super().describe()
        print(f"It length is {self.side}cm")

class Triangle(Shape):
    def __init__(self, name, color, is_filled, width, height):
        super().__init__(name, color, is_filled)
        self.width = width
        self.height = height
    def describe(self):
        super().describe()
        print(f"It width is {self.width} and height is {self.height}")


circle = Circle("Circle", "Green", True, 5.5)
sqaure = Square(name="Square", color="Red", is_filled=False, side=2.4)
trianlge = Triangle(name="Triangle", color="Yellow", is_filled=True, width=8, height=10)

print("Circle: ")
print(circle.color)
print(circle.is_filled)
print(f"Radius: {circle.radius}cm")

print("\nSquare: ")
print(sqaure.color)
print(sqaure.is_filled)
print(f"Length: {sqaure.side}cm")

print("\nTriangle: ")
print(trianlge.color)
print(trianlge.is_filled)
print(f"Width: {trianlge.width}cm")
print(f"Height: {trianlge.height}cm")

print()

circle.describe()
trianlge.describe()
sqaure.describe()
