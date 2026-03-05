# 🔐 Encryption Game

A simple Python-based encryption and decryption program.
This program creates a shuffled key to encrypt and decrypt user messages using character substitution.

---

## 📌 What It Does

* Generates a list of characters (letters, digits, punctuation, space)
* Shuffles the characters to create a secret key
* Encrypts a user’s message using character substitution
* Decrypts an encrypted message back to original text
* Uses the same shuffled key during program execution

⚠️ Note: The key changes each time the program runs.

---

## ▶️ How To Run It

1. Make sure Python 3 is installed.
2. Open terminal / command prompt.
3. Navigate to the project folder.
```bash
cd projects/15_encryption_program
```
4. Run:
```bash id="t9x4mz"
python main.py
```

5. Enter a message to encrypt.
6. Enter an encrypted message to decrypt.

---

## 🧠 Concepts Used

* Functions
* Strings
* Lists
* Type casting (`list()`)
* Loops (for loop, while loop)
* Indexing
* String concatenation
* `random.shuffle()`
* `string` module (`ascii_letters`, `digits`, `punctuation`)
* Copying lists (`list.copy()`)
* `if __name__ == "__main__"` pattern

---

## 🔄 How It Works

1. Create a character list.
2. Make a copy of that list.
3. Shuffle the copy to create a key.
4. Encrypt:

   * Find index of character in original list.
   * Replace it with character at same index in shuffled key.
5. Decrypt:

   * Find index of character in shuffled key.
   * Replace it with character at same index in original list.


---

## 📸 Ouput

![Encryption Decryption Output](https://github.com/ArhanBytes/python-mastery-Brocode/blob/main/projects/15_encryption_program/output.png)

---

## 🚀 Future Improvements (Optional Ideas)

* Save the encryption key to a file
* Allow custom keys
* Add error handling for unsupported characters
* Create GUI version
* Add password protection

---

Thanks for trying the Encryption Game 🔐
