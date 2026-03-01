# 🍔 Concession Stand Program

## 📌 Project Description

A command-line concession stand ordering system where users can select food items from a menu, enter quantities, and receive a final bill.

The program simulates a small food ordering system using a dictionary-based menu.

---

## 🚀 What It Does

* Displays a formatted food menu with prices
* Allows users to select items
* Validates item availability
* Validates quantity (must be positive)
* Stores selected items in a cart
* Calculates the total bill
* Displays selected items with quantities
* Ends ordering when the user enters `q`

---

## ▶️ How to Run It

1. Make sure Python 3 is installed.
2. Open terminal / command prompt.
3. Navigate to the project folder.
    ```bash
    cd projects/09_concession_stand
    ```
4. Run:
    ```bash
    python main.py
    ```
5. Select items from the menu.
6. Enter quantity.
7. Type `q` to finish and see the total bill.

---

## 🧠 Concepts Used

* Dictionary (`menu`, `cart`)
* `for` loop
* `while` loop
* Nested loops
* `dict.items()` method
* `dict.get()` method
* `dict.update()` method
* Conditional statements (`if/elif/else`)
* Input validation
* Type casting (`int`)
* Arithmetic operations
* Formatted string output (`:.2f` formatting)

---

## 🖥️ Example Output

```
----------------- MENU -----------------
burger     : $5.75
hotdog     : $3.25
...
----------------------------------------

Select an item (q to quit): burger
Enter quantity of burger: 2
Select an item (q to quit): coffee
Enter quantity of coffee: 1
Select an item (q to quit): q

Selected item: 2 x burger, 1 x coffee,
Total Bill: 13.75
```

---

## 📸 Ouput

![Concession Stand Output](https://github.com/ArhanBytes/python-mastery-Brocode/blob/main/projects/09_concession_stand/output.png)

---