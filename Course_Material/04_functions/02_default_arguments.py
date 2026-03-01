"""
Topic: Default Arguments
Section: Function
Description:
default arguments = A default value for certain parameters
                    default is used when that argument is omitted
                    make your functions more flexible, reduces # of arguments
                    1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary
"""


# --------- CALCULATING NET PRICE FUNCTION ---------
def net_price(list_price, discount=0, tax=0.05):
    return (list_price * (1 - discount) * (1 + tax))

print(f"Net Price: {net_price(500, 0.1):.2f}")

# --------- EXERCISE 01: COUNT UP TIMER ---------
import time
def count(end, start = 0):
    for x in range(start, end+1):
        print(f"{x:02}")
        time.sleep(1)
    print("DONE!")

count(10, 3)