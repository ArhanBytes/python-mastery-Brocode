"""
Topic: Layout Management in PyQt5
Section: GUI PYQT5
Description:
Demonstrates how to arrange widgets in a PyQt5 window using different layout managers
(QVBoxLayout, QHBoxLayout, and QGridLayout). Since QMainWindow does not allow layouts
to be set directly, we place layouts inside a QWidget and then set that QWidget as the
central widget of the main window.
"""

import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
)

# Note: QMainWindow cannot directly hold layouts.
# We must first create a QWidget, apply our layout to it,
# and then set that QWidget as the central widget of QMainWindow.


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.initUI()

    # Method to organize our layout setup
    def initUI(self):
        central_widget = QWidget()  # Create a QWidget container
        self.setCentralWidget(central_widget)  # Place QWidget inside QMainWindow

        # Create labels to visualize layout positions
        label1 = QLabel("#1", self)
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)

        # Add background colors to labels for clarity
        label1.setStyleSheet("Background-color: red;")
        label2.setStyleSheet("Background-color: yellow;")
        label3.setStyleSheet("Background-color: green;")
        label4.setStyleSheet("Background-color: blue;")
        label5.setStyleSheet("Background-color: purple;")

        # -------------------------------
        # Example 1: Vertical Layout
        # -------------------------------
        """
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        vbox.addWidget(label5)

        central_widget.setLayout(vbox)
        """

        # -------------------------------
        # Example 2: Horizontal Layout
        # -------------------------------
        """
        hbox = QHBoxLayout()
        hbox.addWidget(label1)
        hbox.addWidget(label2)
        hbox.addWidget(label3)
        hbox.addWidget(label4)
        hbox.addWidget(label5)

        central_widget.setLayout(hbox)
        """

        # -------------------------------
        # Example 3: Grid Layout
        # -------------------------------
        grid = QGridLayout()
        grid.addWidget(label1, 0, 0)  # row 0, col 0
        grid.addWidget(label2, 0, 1)  # row 0, col 1
        grid.addWidget(label3, 1, 1)  # row 1, col 1
        grid.addWidget(label4, 1, 0)  # row 1, col 0
        grid.addWidget(label5, 1, 2)  # row 1, col 2

        central_widget.setLayout(grid)  # Apply grid layout to central widget


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
