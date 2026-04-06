"""
Topic: Class Methods
Section: Object Oriented Programming
Description:
-- Class methods =  Allow operations related to the class itself
                    Take (cls) as the first parameter, which represents the class itself.

- Instance methods = Best for operations on instances of the class (objects)
- Static methods = Best for utility functions that do not need access to class data
- Class methods = Best for class-level data or require access to the class itself

"""

class Student:
    count = 0
    total_gpa = 0
    # CONSTRUCTOR
    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count = Student.count + 1
        Student.total_gpa = Student.total_gpa + self.gpa
    
    # INSTANCE METHOD
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    # CLASS METHOD
    @classmethod
    def get_count(cls):
        return f"Total Number of Students: {cls.count}"
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.total_gpa / cls.count:.2f}"

std1 = Student("Arhan", 3.74)
std1 = Student("Farhan", 2.74)
std1 = Student("Arham", 1.00)

print(Student.get_count())
print(Student.get_average_gpa())