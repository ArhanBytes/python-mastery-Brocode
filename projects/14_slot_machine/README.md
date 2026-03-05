# 🎰 Slot Machine Game

A simple command-line Slot Machine game built using Python.
Players can place bets, spin the slot machine, and win payouts based on matching symbols.

---

## 📌 What It Does

* Starts with an initial balance of **$100**
* Allows the player to:

  * Place a bet
  * Spin the slot machine
  * Win money if all 3 symbols match
* Different symbols have different payout multipliers
* Prevents:

  * Invalid bets
  * Negative bets
  * Betting more than available balance
* Game continues until:

  * Player chooses to stop
  * Balance reaches $0

---

## ▶️ How To Run It

1. Make sure Python 3 is installed.
2. Open terminal / command prompt.
3. Navigate to the project folder.
```bash
cd projects/14_slot_machine
```
4. Run:
```bash id="t9x4mz"
python main.py
```
5. Follow the on-screen instructions to play.

---

## 🧠 Concepts Used

* Functions
* Lists
* Loops (while loop)
* Conditionals (if / elif / else)
* Input validation
* String methods (`isdigit()`, `upper()`)
* List comprehension
* `random.choice()`
* Joining strings using `" | ".join()`
* Main function pattern (`if __name__ == '__main__'`)

---

## 🎲 Symbols & Payouts

| Symbol | Multiplier |
| ------ | ---------- |
| 🍒     | 3x         |
| 🍉     | 4x         |
| 🍋     | 5x         |
| 🔔     | 7x         |
| ⭐      | 10x        |

To win, all three symbols must match.

---

## 📸 Ouput

![Slot machine Output](https://github.com/ArhanBytes/python-mastery-Brocode/blob/main/projects/14_slot_machine/output.png)

---

## 🚀 Future Improvements (Optional Ideas)

* Add multiple paylines
* Add random probability weighting
* Save high score
* Add sound effects
* Create a GUI version using Tkinter or Pygame

---

Thanks for playing 🎰
