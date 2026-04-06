"""
Topic: Magic Methods
Section: Object Oriented Programming
Description:
- Magic methods =   Dunder methods (double underscore) __init__, __str__, __eq__
                    They are automatically called by many of Python's built-in operations.
                    They allow developers to define or customize the behavior of objects
"""


class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __str__(self):
        return f"name: {self.name} gpa: {self.gpa}"

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.gpa > other.gpa


student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 2.0)

print(student1)
print(student1 == student2)
print(student1 > student2)
print()


# --------------------------------------
class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __add__(self, other):
        return self.num_pages + other.num_pages

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "pages":
            return self.num_pages
        else:
            return f"Key '{key}' was not found."


# when we call class Book we are automatically calling a magic method named __init__
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)
book4 = Book("The Hobbit", "J.R.R. Tolkien", 220)
# calls the __str__ whenever you print the object
print(book1)
print(book2)
print(book3)


# calls a magic method named __eq__ whenever you compare two object by ==, you can customize the behavior of this
print(f"Is  book 1 title and author same as book 4?? {book1 == book4}")

# calls a magic method named __gt__ whenever you compare two object by >, you can customize the behavior of this
print(f"Is Book 1 page is greater than book 4?? {book1 > book4}")

# calls a magic method named __lt__ whenever you compare two object by <, you can customize the behavior of this
print(f"Is Book 2 page is lesser than book 3?? {book2 < book3}")

# calls a magic method named __add__ whenever you add two object by +, you can customize the behavior of this
print(
    f"1st book pages: {book1.num_pages}\n2nd Book pages: {book3.num_pages}\nTotal pages: {book1 + book3}"
)

# calls a magic method named __contains__ whenever you apply membership in object by 'in', you can customize the behavior of this
print(f"Is Lion is in book 3?? {'Lion' in book3}")
print(f"Is Lion is in book 1?? {'Lion' in book1}")
print(f"Is Rowling is in book 2?? {'Rowling' in book2}")


# calls a magic method named __getitem__ whenever you do object[key], you can customize the behavior of this
print(f"Title: {book1['title']} , Author: {book1['author']}, Pages: {book1['pages']}")
print(book3["audio"])
