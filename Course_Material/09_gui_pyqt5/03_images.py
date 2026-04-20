"""
Topic: Working with Images in PyQt5
Section: GUI PYQT5
Description:
Demonstrates how to load and display an image in a QLabel using QPixmap,
resize it to fit the label, and position the label within the window.
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel # common way to display images is insert image to a label 
from PyQt5.QtGui import QPixmap # this class use to handling images and providing functionalities like loading, manipulating and displaying images


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(700, 300, 500, 500)
        
        label = QLabel(self)
        label.setGeometry(0, 0, 250, 250)
        
        pixmap = QPixmap("Course_Material/09_gui_pyqt5/markhor_dp.jpg") # make a picture object
        label.setPixmap(pixmap) # setting our picture to our label
        
        label.setScaledContents(True)# fit our image within  label

        # positioning of label
        # 1: top left ->x = 0, y =  0
        # 2: top right ->x = self.width() - label.width(), y =  0
        # 3: bottom right ->x = self.width() - label.width(), y =  self.height() - label.height()
        # 4: bottom left ->x = 0, y =  self.height() - label.height()
        # 5: CENTER -> x = (self.width() - label.width()) // 2, y = (self.height() - label.height()) // 2
        # //: is used to divide value and return integer not any other for round of
        
        label.setGeometry((self.width() - label.width()) // 2,
                          (self.height() - label.height()) // 2,
                          label.width(),
                          label.height()) 
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
