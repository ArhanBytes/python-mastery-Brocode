"""
Topic: Static Methods
Section: Object Oriented Programming
Description:
- Static methods =  A method that belongs to a class rather than any object from that class (instance).
                    Usually used for general utility functions.

- Instance methods = Best for operations on instances of the class (objects).
- Static methods = Best for utility functions that do not need access to class data.
"""


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_position = ["Manager", "Cashier", "Cook", "Janitor"]

        return position in valid_position

emp1 = Employee("Luka Modric", "Manager")
emp2 = Employee("Sergio Ramos", "Janitor")
emp3 = Employee("Ronaldo", "Cook")

# CALLING STATIC METHOD
print(Employee.is_valid_position("Chai wala"))
# CALLING INSTANCE METHOD
print(emp1.get_info())
print(emp2.get_info())
print(emp3.get_info())