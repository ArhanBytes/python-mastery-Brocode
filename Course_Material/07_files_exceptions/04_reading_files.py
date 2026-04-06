"""
Topic: Reading Files
Section:  Files Exception
Description:
Python reading files (.txt, .json, .csv)
"""

# -----------------TEXT FILE (.txt)-----------------

file_path = "D:/Github Reps/python-mastery-Brocode/Course_Material/07_files_exceptions/output.txt"

try:
    with open(file=file_path, mode="r") as file:
        content = file.read()  # return long string
        print(content)
except FileNotFoundError:  # if file not found
    print("That file is not exist")
except PermissionError:  # If we have no permisssion to access the file
    print("U do not have permission to read that file")

# -----------------JSON FILE (.json)-----------------

import json

file_path = "D:/Github Reps/python-mastery-Brocode/Course_Material/07_files_exceptions/output3.json"

try:
    with open(file=file_path, mode="r") as file:
        content = json.load(file)
        print(content.items())
except FileNotFoundError:  # if file not found
    print("That file is not exist")
except PermissionError:  # If we have no permisssion to access the file
    print("U do not have permission to read that file")


# -----------------Comma Seperated Values: CSV FILE (.csv) -----------------
import csv

file_path = "D:/Github Reps/python-mastery-Brocode/Course_Material/07_files_exceptions/output4.csv"

try:
    with open(file=file_path, mode="r") as file:
        content = csv.reader(file)
        for line in content:
            print(line[::-1])
except FileNotFoundError:  # if file not found
    print("That file is not exist")
except PermissionError:  # If we have no permisssion to access the file
    print("U do not have permission to read that file")
