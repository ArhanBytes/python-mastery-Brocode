"""
Topic: Radio Buttons in PyQt5
Section: GUI Development (PyQt5)
Description: A PyQt5 window with two groups of radio buttons.
             - Group 1: Payment type (Visa, Mastercard, Gift Card)
             - Group 2: Payment method (In-Store, Online)
             Radio buttons are grouped using QButtonGroup so only
             one option per group can be selected at a time.
             Each button is connected to a slot that prints the
             selected option when toggled.
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        # PAYMENT TYPE
        self.radio1 = QRadioButton("Visa", self)  # paremeter (text, parent)
        self.radio2 = QRadioButton("Mastercard", self)
        self.radio3 = QRadioButton("Gift Card", self)
        # with the default behavior of pyqt5 all radio button unless explicitely stated are all part of the same group
        # PAYMENT METHOD
        self.radio4 = QRadioButton("In-Store", self)
        self.radio5 = QRadioButton("Online", self)
        # creating a button group
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)

        self.initUI()

    def initUI(self):
        # setting geometry of our radio button because we are not using layout managers
        self.radio1.setGeometry(0, 0, 300, 50)
        self.radio2.setGeometry(0, 50, 300, 50)
        self.radio3.setGeometry(0, 100, 300, 50)
        self.radio4.setGeometry(0, 150, 300, 50)
        self.radio5.setGeometry(0, 200, 300, 50)
        # setting stylessheet
        # we can apply multiple css property to entire group of widgets
        self.setStyleSheet(
            "QRadioButton{" "font-size: 40px;" "font-family: Aial;" "padding: 10px;" "}"
        )

        # button group for visa, mastercard, and gift card
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)
        # button group for online and in-store payment method
        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        # adding signal slot to radio button
        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)

    def radio_button_changed(self):
        radio_button = (
            self.sender()
        )  # sender method going to send the object of the widget that sends the signal
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
