"""
Topic: Arbitrary Arguments
Section: Function
Description:
*args     = allows you to pass multiple non-key arguments
**kwargs  = allows you to pass multiple keyword-arguments
          * unpacking operator
          1. positional 2. default 3. keyword 4. ARBITRARY

"""

# Arbitrary Argument: Varying amount of argument, we do not know how many arguments user pass while invoking a function

# *args: pack all arguments into tuple if it is args
# **kwargs: pack all arguments into dictionary if it is kwargs

# ------- *args -------


# ------ ADD 2 NUMBER ------
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(add(1, 2, 4))


# ------- YOU CAN CHAGNE THE NAME OF PARAMETER TOO ------
def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total


print(add(1, 2, 4))


# ------- DISPLAY NAME FUNCTION -------
def display_name(*names):
    for name in names:
        print(name, end=" ")


display_name("Dr.", "Spongebob", "Harold")

print()

# ------- **kwargs -------
def print_address(**kwargs):
    for item in kwargs.items():
        print(f"{item[0].capitalize()}: {item[1].capitalize()}")


print_address(street="402", apt="100", city="Karachi", state="sindh", zip="2341")

print()
# ------- EXERCISE 01: PRINTING SHIPPING LABEL -------
def shipping_label(*args, **kwargs):
    print("Name: ", end="")
    for arg in args:
        print(arg, end=" ")
    print()
    
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
        
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")
    
# passing positional argument followed by keyword argumen, it won't work other way around
shipping_label("Mr.", "Cristiano", "Ronaldo", "Santos", "07",
               street="123", pobox="PO box #1001", city="Lisbon", state="madeira", zip="123")