Here is your clean `README.md` content 👇
(You can copy-paste directly into your file.)

---

# 🎲 Dice Roll Game

## 📌 Project Description

A command-line dice rolling game that generates one or more dice rolls and displays them using ASCII art.

The program visually prints the dice faces and calculates the total of all rolled dice.

---

## 🚀 What It Does

* Asks the user how many dice to roll
* Generates random dice values (1–6)
* Displays dice using ASCII art
* Prints multiple dice side-by-side (horizontal layout)
* Calculates and displays the total sum of all dice

---

## ▶️ How to Run It

1. Make sure Python 3 is installed.
2. Open terminal / command prompt.
3. Navigate to the project folder.
```bash
cd projects/12_dice_roller
```
4. Run:

```bash id="t9x4mz"
python main.py
```

5. Enter the number of dice you want to roll.

---

## 🧠 Concepts Used

* `random` module
* `random.randint()`
* Dictionary (mapping dice number → ASCII art)
* Tuples (storing multi-line dice art)
* Lists (storing generated dice)
* `for` loops (nested loops for printing)
* Dictionary `.get()` method
* Indexing
* `range()` function
* Accumulator pattern (calculating total)
* Formatted string output (f-strings)

---

## 🖥️ Example Output

```id="k8r2pl"
How many dice?: 2

┌─────────┐ ┌─────────┐
│  ●   ●  │ │    ●    │
│         │ │         │
│  ●   ●  │ │         │
└─────────┘ └─────────┘

Total: 5
```

---

## 📸 Ouput

![Dice Roll Game Output](https://github.com/ArhanBytes/python-mastery-Brocode/blob/main/projects/12_dice_roller/output.png)

---