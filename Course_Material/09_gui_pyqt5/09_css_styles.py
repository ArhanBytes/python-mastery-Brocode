"""
Topic: CSS Styles in PyQt5
Section: GUI Development (PyQt5)
Description: PyQt5 supports styling widgets using CSS-like
             style sheets. You can set global styles for
             all widgets of a type (e.g., QPushButton) and
             apply unique styles by assigning object names
             with setObjectName(). Style sheets allow control
             over font, padding, borders, colors, and hover
             effects, making GUIs more visually appealing.
"""


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button1 = QPushButton("#1")  # since we are using layout manager we don't need to add second argument "self" which is a parent
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        
        self.initUI()

    def initUI(self):
        # creating a widget where we add the layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # layout creation
        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)
        
        # APPLYING CSS
        # we have to set object name for button to individually access then while applying cascading style sheet
        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")
        
        self.setStyleSheet("""
                          QPushButton {
                            font-size: 40px;
                            font-family: Arial;  
                            padding: 15px 75px;
                            margin: 25px;
                            border: 3px solid black;
                            border-radius: 15px;
                          } 
                          QPushButton#button1{
                              background-color: hsl(44, 34%, 54%);
                          }
                          QPushButton#button2{
                              background-color: hsl(171, 24%, 53%);
                          }
                          QPushButton#button3{
                              background-color: hsl(338, 30%, 60%);
                          }
                          QPushButton#button1:hover{
                              background-color: hsl(44, 34%, 74%);
                          }
                          QPushButton#button2:hover{
                              background-color: hsl(171, 24%, 73%);
                          }
                          QPushButton#button3:hover{
                              background-color: hsl(338, 30%, 80%);
                          }
                          
        """)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
