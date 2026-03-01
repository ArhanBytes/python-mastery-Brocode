"""
Topic: Fucntions
Section: Function
Description:
# function = A block of reusable code
#           place () after the function name to invoke it
"""
# ------ FUNCTIION ------
def happy_birthday():
    print("Happy birthday to you!")
    print("You are old!")
    print("Happy birthday to you!")
    print()

happy_birthday()

# ------ Parameters and Arguements ------
def happy_birthday(name):
    print(F"Happy birthday to {name}!")
    print(f"{name} are old!")
    print(f"Happy birthday to {name}!")
    print()

happy_birthday("Arhan")
happy_birthday("Roma")
happy_birthday("Josh")

# ------ Multiple parameters and arguments ------
def happy_birthday(name, age):
    print(F"Happy birthday to {name}!")
    print(f"{name} are {age} old!")
    print(f"Happy birthday to {name}!")
    print()

happy_birthday("Arhan", 20)
happy_birthday("Roma", 30)
happy_birthday("Josh", 15)


# ------ DISPLAY INVOICE USING FUNCTION ------
def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("Arhan Imran", 30234.25, "01/01")
display_invoice("Roma Ramen", 2321.25, "02/01")
print()

# -------- RETURN IN A FUNCTION -----------
# return = statement used to end a function
#          and send a result back to the caller

# ----------- ARITHMETIC FUNCTION -----------

def add(n1, n2):
    n3 = n1 + n2
    return n3

def subtract(n1, n2):
    n3 = n1 - n2
    return n3

def multiply(n1, n2):
    n3 = n1 * n2
    return n3

def divide(n1, n2):
    n3 = n1 / n2
    return n3

a = 5 
b = 6
print(f"Addition of {a} and {b}: {add(a, b)}")
print(f"Subtraction of {a} and {b}: {subtract(a, b)}")
print(f"Multiply of {a} and {b}: {multiply(a, b)}")
print(f"Divide of {a} and {b}: {divide(a, b)}")

# ----------- CREATING FULL NAME FUNCTION -----------

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("arhan", "imran")
print(f"Full name: {full_name}")