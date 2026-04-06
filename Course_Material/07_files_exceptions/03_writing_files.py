"""
Topic: Writing Files
Section:  Files Exception
Description:
Python writing files (.txt, .json, .csv)
"""

# -----------------TEXT FILE (.txt)-----------------
txt_data = "I like Pizza!"

file_path = "Course_Material/07_files_exceptions/output.txt"  # relatvie file path

# open(file path, "mode such as w,r,x") -> it will create file if not exist otherwise open it

# with is and statement. it wrap a block of code to execute. if we open a file with statement also close the file when we done with it.
# open function return the file object
# w = write a file
# x = write a file if this file doesn't exist, if exist throw error
# a = append a file
# r = read
# when the open fucntion return as object of file we are naming that object as 'file' using alias

try:
    with open(file=file_path, mode="a") as file:
        file.write("\n" + txt_data)
        print(f"Text file '{file_path}; was created")
except FileExistsError:
    print("That file already Exist")

# ------- Interaction Collections with files ----------

file_path = "Course_Material/07_files_exceptions/output2.txt"  # relatvie file path

employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]
try:
    with open(file=file_path, mode="w") as file:
        for employee in employees:
            file.write(employee + "\n")
        print(f"Text file '{file_path}; was created")
except FileExistsError:
    print("That file already Exist")

# -----------------JSON FILE (.json)-----------------
import json

employee = {"name": "Spongebob", "age": 30, "job": "cook"}

file_path = "Course_Material/07_files_exceptions/output3.json"

try:
    with open(file=file_path, mode="w") as file:
        json.dump(
            employee, file, indent=4
        )  # dump method convert our dictionary to json string for output and indent shows for each key value pair how many space do you want
        print(f"Json file '{file_path} was created")
except FileExistsError:
    print("That file already Exist")

# -----------------Comma Seperated Values: CSV FILE (.csv) -----------------

import csv

employees = [
    ["Name", "Age", "Job"],
    ["Ronaldo", 41, "Footballer"],
    ["Ramos", 39, "CEO"],
    ["Mourinho", 64, "Manager"],
]

file_path = "Course_Material/07_files_exceptions/output4.csv"

try:
    with open(file=file_path, mode="w", newline="") as file:
        writer = csv.writer(
            file
        )  # Writer is an object it provides method to writing data in csv file
        for row in employees:
            writer.writerow(row) # gives additional new line tough by default

        print(f"CSV file '{file_path}' was created")
except FileExistsError:
    print("That file already exist")
