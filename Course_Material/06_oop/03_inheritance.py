"""
Topic: Inheitence
Section: Object Oriented Programming
Description:
Inheritance = Allows a class to inherit attributes and methods from another class
              Helps with code reusability and extensibility
              class Child(Parent)
"""
class Amimal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
    def eat(self):
        print(f"{self.name} is eating")
        
    def sleep(self):
        print(f"{self.name} is asleep")

class Dog(Amimal):
    def speak(self):
        print("WOOF!")

class Cat(Amimal):
    def speak(self):
        print("MEOW!")

class Mouse(Amimal):
    def speak(self):
        print("SQUEEK!")

dog = Dog("Bob")
cat = Cat("Garfield")
mouse = Mouse("Micky")

# PARENT METHODS AND ATTRIBUTES
print(mouse.name)
print(mouse.is_alive)
mouse.eat()
mouse.sleep()
mouse.speak()