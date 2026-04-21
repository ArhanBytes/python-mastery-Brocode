# Digital Clock by using PYQT5 GUI
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase


# out digital clock is a widget
class DigitalClock(QWidget):
    # Here constructor is used for creating different entity for the clock
    def __init__(self):
        super().__init__()
        self.timer_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    # initUI for designing the layout of digital clock
    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 400, 300, 100)

        # settting up layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.timer_label)
        self.setLayout(vbox)

        # setting up alignmnet of timer label
        self.timer_label.setAlignment(Qt.AlignCenter)

        # CSS for timer label
        self.timer_label.setStyleSheet(
            "font-size: 150px;" "color: hsl(111,100%,50%);"
        )
        # background color of window
        self.setStyleSheet("background-color: black;")
        
        # setting up font
        font_id = QFontDatabase.addApplicationFont("projects/18_digital_clock/ds_digital/DS-DIGIT.TTF") # it is a class for managing quering fonts available to the application -> addApplication is used to add custon fonts
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0] # this method returns a font name -> it will return the first element of font family list
        myfont = QFont(font_family, 150) # paremeter (font name, font size)
        self.timer_label.setFont(myfont)
        
        # setting signal and slot -> whenever timeout triggers we will call our udpate time
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        
        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.timer_label.setText(current_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()

    clock.show()
    sys.exit(app.exec_())
