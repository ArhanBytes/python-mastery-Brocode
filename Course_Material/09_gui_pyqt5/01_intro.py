"""
Topic: Introduction to PyQt5
Section: GUI PYQT5
Description:
A basic PyQt5 program that creates a main window,
sets its title, size, and icon, and runs the application loop.
"""


import sys
# sys — System-specific parameters and functions
# This module provides access to some variables used or maintained by the interpreter
# and to functions that interact strongly with the interpreter.
# It is always available.

# from Package->module import class, class
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
# widges are building block of PyQt5 Application
# QApplication is a class
# QMainWindow is a class

class MainWindow(QMainWindow):
    def __init__ (self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(700,300,500,500) # x,y,width, height
        self.setWindowIcon(QIcon("Course_Material/09_gui_pyqt5/pf.png"))
def main():
    app = QApplication(sys.argv) # or empty list []
        # sys.argv
        # This is a list that holds the values you type when running a Python file from the command line.
        # Example: python myscript.py hello world
        # In this case:
        #   sys.argv[0] -> "myscript.py" (the script name)
        #   sys.argv[1] -> "hello"
        #   sys.argv[2] -> "world"
        #
        # Notes:
        # - argv[0] is always the script name (sometimes full path, depends on OS).
        # - If you run Python with the -c option, argv[0] will be "-c".
        # - If no script name is given, argv[0] will be an empty string.
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) # exit method ensures clean exit of our program
    # exec_() method waits around for user input and handles event such as click on buttons, press keys and close the window


if __name__ == "__main__":
    main()