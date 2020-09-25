import sys
from PyQt5.QtCore import  Qt
from PyQt5.QtWidgets import (QWidget,QLCDNumber,QSlider,QVBoxLayout,QApplication)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('signal and slot')
        self.show()
        # 윈도우 화면 구성

        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal,self)
        # LCD, SLD 구성 설정

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)
        self.setLayout(vbox)
        # 레이아웃 구성

        sld.valueChanged.connect(lcd.display)
        # SLD의 값이 변경 되었을 경우 LCD에 표시


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
