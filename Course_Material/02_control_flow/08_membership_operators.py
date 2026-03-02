"""
Topic: Membership Operators
Section: Control Flow
Description:
Membership operators = used to test whether a value or variable is found in a sequence
                        (string, list, tuple, set, or dictionary)
      1. in
      2. not in
"""

word = "APPLE"

# --------- EXAMPLE 02 ---------
# ---- GUESS A LETTER ------
letter = input("Guess the letter in the secret word: ").upper()

# IN
if letter in word:
    print(f"There is a {letter}")
# NOT IN
if letter not in word:
    print(f"{letter} was not found")

# --------- EXAMPLE 01 ---------
students = {"Ronaldo", "Marcelo", "Ramos"}

student = input("Enter the name of studnet: ").capitalize()

if student not in students:
    print(f"{student} was not found")
else:
    print(f"{student} is a student")

# --------- DICTIONARY ---------
grades = {"Mbappe": "A", "Vini": "B", "Bellingham": "C", "Valverde": "A+"}

student = input("Enter the name of student: ")

if student in grades:
    print(f"{student} has {grades[student]} grade.")
if student not in grades:
    print(f"{student} has not any grade")
    
# ------- EMAIL VALIDATION ---------
email = "arhan1234567890@gmail.com"
if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid Email")