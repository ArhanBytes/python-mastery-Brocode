"""
Topic: Line Edits in PyQt5
Section: GUI Development (PyQt5)
Description: QLineEdit provides a single-line text input field
             where users can type and edit text. It supports
             placeholder text, styling, and methods like .text()
             to retrieve user input. Often paired with buttons
             or signals to trigger actions based on entered text.
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.line_edit = QLineEdit(self)  # add this line edit to the window
        self.button = QPushButton(
            "Submit", self
        )  # adding a button to interact with line edits
        self.initUI()

    def initUI(self):
        self.line_edit.setGeometry(10, 10, 200, 40)  # setting geometry of our line edit
        self.button.setGeometry(210, 10, 100, 40)  # setting geometry of our button
        self.line_edit.setStyleSheet(
            "font-size: 25px;" "font-family: Ariel;"
        )  # setting stylesheet of line edit
        self.button.setStyleSheet(
            "font-size: 25px;" "font-family: Ariel;"
        )  # setting stylesheet of line edit
        self.line_edit.setPlaceholderText("Enter your name")
        # setup a signal whenever button clicked
        self.button.clicked.connect(self.submit)

    # A method we call whenever user click on submit button
    def submit(self):
        text = (
            self.line_edit.text()
        )  # text method returns a string written in line edit widget
        print(f"Hello!  {text}")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
