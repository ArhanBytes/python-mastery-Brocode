"""
Topic: Working Buttons in PyQt5
Section: GUI Development (PyQt5)
Description: A simple PyQt5 window with a button and label.
             Clicking the button changes its text, disables it,
             and updates the label.
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Set window position (x=700, y=300) and size (500x500)
        self.setGeometry(700, 300, 500, 500)

        # Define button and label as class attributes (accessible everywhere in the class)
        self.button = QPushButton("Click me!", self)  # parameters: (text, parent widget)
        self.label = QLabel("Hello", self)

        self.initUI()

    def initUI(self):
        # Position and style the button
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 30px")

        # Connect button click signal to the handler function
        self.button.clicked.connect(self.on_click)

        # Position and style the label
        self.label.setGeometry(150, 300, 200, 100)
        self.label.setStyleSheet("font-size: 50px;")

    def on_click(self):
        # Actions performed when button is clicked
        print("Button Clicked")
        self.button.setText("Button Clicked")   # Change button text
        self.button.setDisabled(True)           # Disable button after click
        self.label.setText("Goodbye")           # Update label text


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
