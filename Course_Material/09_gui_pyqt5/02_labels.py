"""
Topic: Label in PyQt5
Section: GUI PYQT5
Description:
Shows how to create and style a QLabel in PyQt5,
including setting text, font, colors, CSS styles, and alignment.
"""


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel 
# Qlabel is use to create text and display images
from PyQt5.QtGui import QFont # to add font
from PyQt5.QtCore import Qt # imported for alignment
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(700, 300, 500, 500)
        
        # working with label
        label = QLabel("Hello", self) # it returns an object of label (text, parent object which is window)
        label.setFont(QFont("Ariel", 20)) # font and font size 
        label.setGeometry(0,0,500,100) # setting geometry of label
        label.setStyleSheet("color: blue;"
                            "background-color: black;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;") # setting CSS of label
        # -----VERTICAL ALIGNEMNT-----
        label.setAlignment(Qt.AlignTop) # Vertically top alignment to label
        label.setAlignment(Qt.AlignBottom) # Vertically Bottom alignment to label
        label.setAlignment(Qt.AlignVCenter) # Vertically Center alignment to label
        
        # -----HORIZONTAL ALIGNEMNT-----
        label.setAlignment(Qt.AlignRight) # Horizontally right alignment to label
        label.setAlignment(Qt.AlignLeft) # Horizontally left alignment to label
        label.setAlignment(Qt.AlignHCenter) # Horizontally Center alignment to label
        
        # BOTH HORIZONTAL AND VERTICAL ALIGNMENT
        label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # center and top
        label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # center and bottom
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # center and center
        label.setAlignment(Qt.AlignCenter) # shortcut for both center
def main(): 
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())  


if __name__ == "__main__":
    main()
