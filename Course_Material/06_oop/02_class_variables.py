"""
Topic: Class Variables
Section: Object Oriented Programming
Description:
Class variables = Shared among all instances of a class  
Defined outside the constructor  
Allow you to share data among all objects created from that class
"""
class Student:
    # class variable
    class_year = 2024
    no_of_students = 0
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age
        # class variable
        Student.no_of_students +=1

std1 = Student("Doreamon", 21)
std2 = Student("Nobita", 18)
std3 = Student("Shizuka", 20)
std4 = Student("Gian", 25)
print(std1.name)
print(std1.age)
# access by object
print(std2.class_year)
# access by name of the class
print(Student.class_year)
print(Student.no_of_students)

# printing class varibles
print(f"My graduating class of {Student.class_year} has {Student.no_of_students} students.")
print(std1.name)
print(std2.name)
print(std3.name)
print(std4.name)