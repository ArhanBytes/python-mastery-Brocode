# Concession stand program

menu = {
    "burger": 5.75,
    "hotdog": 3.25,
    "taco": 4.00,
    "salad": 6.50,
    "sandwich": 4.75,
    "ice cream": 3.80,
    "coffee": 2.25,
    "tea": 2.00,
    "smoothie": 5.25,
    "water": 1.50
}

# initialiing variables
cart = {}
total = 0

# printing menu
print("----------------- MENU -----------------")
for key, value in menu.items():
    print(f"{key:10} : ${value:.2f}")
print("----------------------------------------")

# choose your item
while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is None:
        print(f"{food} is not available at menu.")
    else:
        quantity = 0
        while True:
            quantity = int(input(f"Enter quantity of {food}: "))
            if quantity <= 0:
                print(f"{quantity} is an inavlid quantity")
            else:
                break
        
        # push food and quantity to cart
        cart.update({food : quantity})

# printing selected item and calculate total amount
print("Selected item: ", end="")
for key, value in cart.items():
    print(f"{value} x {key},", end=" ")
    total = total +  (menu.get(key) * value)
print(f"\nTotal Bill: {total}")
