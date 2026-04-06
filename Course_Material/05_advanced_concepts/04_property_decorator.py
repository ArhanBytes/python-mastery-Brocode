"""
Topic: Property Decorator
Section: Advanced Concept
Description:
@property = Decorator used to define a method as a property (it can be accessed like an attribute)
            Benefit: Add additional logic when read, write, or delete attributes
            Gives you getter, setter, and deleter method
"""


class Rectangle:
    def __init__(self, width, height):
        self._width = width  # by adding _ -> it will consider as private and prohibited to use outside class, technically you can use it!! wierd PYTHON haha.. GO FOR C++ BOYS AND GIRLS
        self._height = height

    # PROPERTY METHOD
    # ----- GETTER (Read Attributes) -----
    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    # ----- SETTER (Write Attributes) -----
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")

    # ----- DLETER (Delete Attributes) -----
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")


rectangle = Rectangle(3, 4)

# ---- GETTER -----
# ACCESS ATTRIBUTE THROUGH PROPERTY METHOD
print(rectangle.width)
print(rectangle.height)


# ---- SETTER -----
rectangle.width = 5
rectangle.height = 6
print(rectangle.width)
print(rectangle.height)

# ----- Deleter -----
del rectangle.width
del rectangle.height
