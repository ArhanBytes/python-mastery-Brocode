"""
Topic: Exception Handling Introduction
Section:  Files Exception
Description:
exception = An event that interrupts the flow of a program
            (ZeroDivisionError, TypeError, ValueError)
            1.try, 2.except, 3.finally
"""

# -------SYNTAX------
"""
try:
    # try some code
except Exception:
    # handle an exception
finally:
    # do some clean up
"""

try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You can't divide by zero IDIOT!")
except ValueError:
    print("Enter only numbers please")
except Exception:
    print("Something went wrong")
finally: # it executes after all try and except portion, jaisa mena file kholi ab ussa band ma finally ma krdonga
    print("Do some cleanup")