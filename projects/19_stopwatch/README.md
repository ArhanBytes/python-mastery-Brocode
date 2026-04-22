# ⏱️ Stop Watch (PyQt5 GUI)

A clean and responsive **Stopwatch application** built using PyQt5.
It provides real-time tracking with start, stop, and reset functionality inside a simple GUI.

---

## 🚀 Features

* ⏱️ Real-time time tracking
* ▶️ Start the stopwatch
* ⏸️ Stop/pause anytime
* 🔄 Reset back to zero
* 🎨 Styled UI using CSS
* ⚡ Smooth updates with milliseconds

---

## 📂 Project Structure

```
19_stopwatch/
│── main.py
│── README.md
│── output.png
```

---

## ▶️ How To Run

### 1. Install Requirements

```bash
pip install PyQt5
```

### 2. Run the App

```bash
python 19_stopwatch/main.py
```

---

## 🧠 Concepts Used

* Object-Oriented Programming (OOP)
* PyQt5 GUI Development
* QLabel & QPushButton
* Layout Management (QVBoxLayout, QHBoxLayout)
* QTimer (real-time updates)
* QTime (time handling)
* Signals & Slots
* Event Handling
* Styling with CSS

---

## 🖥️ Preview

![Stopwatch UI](https://github.com/ArhanBytes/python-mastery-Brocode/blob/main/projects/19_stopwatch/output.png)

---

## 📌 How It Works

* `QTimer` updates every **10ms**
* Time is stored using `QTime`
* Buttons trigger actions using **signals & slots**
* Display updates dynamically in the label

---

## 💡 Future Improvements

* Lap time feature
* Keyboard shortcuts
* Dark/Light mode toggle
* Save session history

---