"""
Topic: Nester Loop
Section: Control Flow
Description:
# nested loop = A loop within another loop (outer, inner)
#     outer loop:
#         inner loop:
"""

for x in range(3):
    for y in range(1,10):
        print(y, end=" ")
    print()
    
#print statement end with new line if you want no new line you should write print(value, end="")

# ------ Exercise 1: Printing Rectangle ------- #

rows = int(input("Enter the # of rows: "))
cols = int(input("Enter the # of cols: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(cols):
        print(symbol, end=" ")
    print()