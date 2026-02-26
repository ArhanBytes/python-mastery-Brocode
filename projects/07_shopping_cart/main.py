# Shopping Cart Program

foods = []
prices = []
total = 0

while True:
    food = input("What food do you want (q to quite): ")
    if food.lower() == "q":
        break
    else:
        while True:
            price = float(input(f"Enter a price of {food}: $"))
            if price <= 0:
                print("Price should be positive.")
            else:
                break
        foods.append(food)
        prices.append(price)


# listing the cart
print("-------Your Cart-------")
for i in range(len(foods)):
    print(f"Item: {foods[i]}\tPrice: ${prices[i]}")
    
# Calculate Total
for price in prices:
    total += price
print(f"Your Total Price: {total}")