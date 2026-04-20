"""
Topic: Checkboxes in PyQt5
Section: GUI Development (PyQt5)
Description: A simple PyQt5 window with a checkbox.
             Toggling the checkbox prints a message
             based on its state (checked/unchecked).
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLabel
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Set window position (x=700, y=300) and size (500x500)
        self.setGeometry(700, 300, 500, 500)

        # Create a checkbox widget (text + parent window)
        self.checkbox = QCheckBox("Do you like food?", self)

        self.initUI()

    def initUI(self):
        # Style the checkbox (font size and family)
        self.checkbox.setStyleSheet("font-size: 30px; font-family: Arial;")

        # Set position and size of checkbox (x, y, width, height)
        self.checkbox.setGeometry(10, 0, 500, 100)

        # Set initial state (True = checked, False = unchecked)
        self.checkbox.setChecked(True)

        # Connect checkbox state change signal to handler function
        self.checkbox.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self, state):
        """
        State values:
        0 = unchecked
        1 = partially checked
        2 = checked
        """
        # Qt.Checked is more readable than using raw value 2
        if state == Qt.Checked:
            print("You like food")
        else:
            print("You don't like food")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
