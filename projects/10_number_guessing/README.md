# 🎯 Number Guessing Game

## 📌 Project Description

A simple command-line number guessing game where the player tries to guess a randomly generated number within a specific range.

The program provides hints (too high or too low) and tracks the number of attempts.

---

## 🚀 What It Does

* Generates a random number between 1 and 100
* Prompts the user to guess the number
* Validates user input (must be a number)
* Checks if the guess is within range
* Gives hints:

  * Too high
  * Too low
* Counts the number of guesses
* Displays the total attempts when guessed correctly

---

## ▶️ How to Run It

1. Make sure Python 3 is installed.
2. Open terminal / command prompt.
3. Navigate to the project folder.
    ```bash
    cd projects/10_number_guessing
    ```
4. Run:

    ```bash id="n9kf2p"
    python main.py
    ```

5. Enter your guesses until you find the correct number.

---

## 🧠 Concepts Used

* `random` module
* `random.randint()`
* `while` loop
* Boolean flag (`is_running`)
* Conditional statements (`if/elif/else`)
* Input validation (`.isdigit()`)
* Type casting (`int`)
* Comparison operators
* Counter variable (tracking guesses)
* Formatted string output (f-strings)

---

## 🖥️ Example Output

```id="h2v7sl"
Select a number between 1 and 100
Enter your guess: 50
50 is low! Try again.
Enter your guess: 75
75 is high! Try again.
Enter your guess: 63
CORRECT! The answer was 63
Number of Guesses: 3
```
---

## 📸 Ouput

![Number Guessing Game Output](https://github.com/ArhanBytes/python-mastery-Brocode/blob/main/projects/10_number_guessing/output.png)
