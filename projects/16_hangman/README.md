Here is your **README.md content** (copy and paste into your file):

---

# 🎮 Hangman Game

A classic command-line Hangman game built using Python.
The player guesses letters to reveal a hidden word before the hangman drawing is completed.

---

## 📌 Project Details

This project is a text-based Hangman game that:

* Randomly selects a word category and word
* Displays a visual hangman using ASCII art
* Allows the player to guess one letter at a time
* Tracks incorrect guesses
* Ends when the player either:

  * Successfully guesses the word (WIN)
  * Reaches the maximum number of wrong guesses (LOSE)

The game uses a separate `word_list.py` file that contains a dictionary of word categories and words.

---

## 🕹 What It Does

* Displays hangman drawing based on wrong guesses
* Shows category hint (e.g., Animal, Country, etc.)
* Prevents:

  * Multiple-letter input
  * Non-alphabet characters
  * Repeated guesses
* Updates word progress dynamically
* Announces WIN or LOSE at the end

---

## ▶️ How To Run It

1. Make sure Python 3 is installed.
2. Ensure both files exist in the same folder:
   * `main.py`
   * `word_list.py`
3. Navigate to the project folder.
```bash
cd projects/16_hangman
```
4. Run:
```bash id="t9x4mz"
python main.py
```
5. Start guessing letters!

---

## 🧠 Concepts Used

* Dictionaries
* Lists
* Tuples
* Sets
* Loops (while loop)
* Conditionals (if / else)
* String methods (`lower()`)
* Input validation
* Random module (`random.choice`)
* `"\n".join()` method
* List indexing
* Game loop logic
* `if __name__ == "__main__"` pattern

---

## 🎨 Hangman Stages

The hangman drawing updates as wrong guesses increase:

* 0 → Empty
* 1 → Head
* 2 → Body
* 3 → One Arm
* 4 → Two Arms
* 5 → One Leg
* 6 → Full Body (Game Over)

---

## 📸 Ouput

![Hangman game Output](https://github.com/ArhanBytes/python-mastery-Brocode/blob/main/projects/16_hangman/output.png)

---


## 🚀 Future Improvements (Optional Ideas)

* Add difficulty levels
* Add limited hints option
* Add scoring system
* Save high score
* Add GUI version using Tkinter or Pygame

---

Thanks for playing Hangman 🎮
