# 💰 Compound Interest Calculator

## 📌 Project Description

A command-line application that calculates the final amount of an investment using the compound interest formula.
The program validates user input and ensures that the principal, rate, and time values are positive before performing the calculation.

---

## 🚀 What It Does

* Prompts the user to enter:

  * Principal amount
  * Interest rate
  * Time (in years)

* Validates that inputs are positive values

* Calculates the final amount using the compound interest formula:

  **A = P(1 + r/100)^t**

* Displays the result formatted to two decimal places

---

## ▶️ How to Run It

1. Make sure Python 3 is installed.
2. Navigate to the project folder:

   ```bash
   cd projects/05_compound_interest
   ```
3. Run the program:

   ```bash
   python main.py
   ```
4. Enter the requested values when prompted.

---

## 🧠 Concepts Used

* `input()` function
* Type casting (`float`, `int`)
* `while` loops for input validation
* Conditional statements
* Mathematical operations
* `pow()` function
* Formatted string output (`:.2f`)

---

## 🖥️ Example Output

```
Enter the principle amount: 1000
Enter the interest rate: 5
Enter the time in years: 3

Principle: 1000.0 Rate: 5.0 Time: 3 year/s  Final Amount: $1157.63
```

---
## 📸 Ouput

![Compound Interest calculator Output](https://github.com/ArhanBytes/python-mastery-Brocode/blob/main/projects/05_compound_interest/output.png)

---