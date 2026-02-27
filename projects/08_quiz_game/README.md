# 🧠 Quiz Game

## 📌 Project Description

A command-line multiple-choice quiz program that tests knowledge of data structures and algorithms.
The program asks questions, validates user input, checks answers, and calculates the final score.

---

## 🚀 What It Does

* Displays multiple-choice questions
* Shows 4 options (A, B, C, D) for each question
* Validates user input (prevents invalid options)
* Checks answers and gives instant feedback
* Stores user guesses
* Displays:

  * User answers
  * Correct answers
  * Final percentage score

---

## ▶️ How to Run It

1. Make sure Python 3 is installed.
2. Open terminal / command prompt.
3. Navigate to the project folder.
    ```bash
    cd projects/06_countdown_timer
    ```
4. Run:

    ```bash
    python main.py
    ```

5. Enter your answer using `A`, `B`, `C`, or `D`.

---

## 🧠 Concepts Used

* Tuples (questions, options, answers)
* Lists (storing user guesses)
* `for` loops
* Nested loops
* `while` loop (input validation)
* Conditional statements (`if/else`)
* String methods (`.upper()`, `.find()`)
* Index tracking (`question_num`)
* Arithmetic (percentage score calculation)

---

## 🖥️ Example Output

```
--------------------------
Which data structure uses FIFO (First In, First Out) principle?:
A. Stack
B. Queue
C. Linked List
D. Tree
Enter (A,B,C,D): B
Correct

...

Your Guess:     B C A ...
Right Answer:   B B C ...
Score: 75%
```

---

## 📸 Ouput

![Quiz Output](https://github.com/ArhanBytes/python-mastery-Brocode/blob/main/projects/08_quiz_game/output.png)
