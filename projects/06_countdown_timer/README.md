# ⏳ Countdown Timer

## 📌 Project Description

A command-line countdown timer that counts down from a user-defined number of seconds and displays the remaining time in days, hours, minutes, and seconds format.

---

## 🚀 What It Does

* Prompts the user to enter time in seconds
* Converts total seconds into:

  * Days
  * Hours
  * Minutes
  * Seconds
* Updates the countdown every second
* Displays the time in `DD:HH:MM:SS` format
* Stops when the timer reaches zero and prints **"TIME UP!"**

---

## ▶️ How to Run It

1. Make sure Python 3 is installed.
2. Navigate to the project folder:

   ```bash
   cd projects/06_countdown_timer
   ```
3. Run the program:

   ```bash
   python main.py
   ```
4. Enter the number of seconds when prompted.

---

## 🧠 Concepts Used

* `input()` function
* Type casting (`int`)
* `for` loop with reverse range
* Time calculations using arithmetic
* Modulus operator (`%`)
* Formatted string output (`:02`)
* `time.sleep()` function
* `time` module

---

## 🖥️ Example Output

```
Enter a time in seconds: 10
00:00:00:10
00:00:00:09
00:00:00:08
...
00:00:00:01
TIME UP!
```

---
## 📸 Ouput

![Compound Interest calculator Output](https://github.com/ArhanBytes/python-mastery-Brocode/blob/main/projects/06_countdown_timer/output.png)

---