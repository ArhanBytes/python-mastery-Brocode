"""
Topic: Python file detection
Section:  Files Exception
"""

import os  # a module provided by python to intract with operating system

# ------- 2. Relative file path -------
# Relative = Folder/test.txt

file_path = "C:/Users/ADMIN/Desktop/check"
# Course_Material/07_files_exceptions/test.txt

#  checking if file exist
if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):  # to check this file is a file not a directory
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print(f"{file_path} location doesn't exist")

# -------2. Absolute file path -------
# Absolute = D:/Github Reps/python-mastery-Brocode/Course_Material/07_files_exceptions/text.txt

file_path = "D:\\Github Reps\\python-mastery-Brocode\\Course_Material\\07_files_exceptions\\test.txt"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
else:
    print(f"{file_path} location doesn't exist")

# In path we can use double double backslash or forwardslash
