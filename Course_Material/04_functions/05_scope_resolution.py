"""
Topic: Scope Resolution
Section: Function
Description:
variable scope = where a variable can be used
scope resolution follows LEGB rule:
Local -> Enclosed -> Global -> Built-in
"""

# -------- LOCAL SCOPE --------
# Variable created inside a function
# Can only be used inside that function

"""
def func1():
    x = 1
    print(x)

def func2():
    x = 2
    print(x)

func1()
func2()
"""


# -------- ENCLOSED SCOPE --------
# Inner function can access variable from outer function

"""
def func1():
    x = 1
    def func2():
        print(x)  # x found in enclosed scope
    func2()

func1()
"""


# -------- GLOBAL SCOPE --------
# Variable created outside functions
# Accessible inside functions (if not redefined locally)

"""
def func1():
    print(x)

def func2():
    print(x)

x = 3
func1()
func2()
"""


# -------- BUILT-IN SCOPE --------
# Python built-in names (always available)

from math import e

print(e)
