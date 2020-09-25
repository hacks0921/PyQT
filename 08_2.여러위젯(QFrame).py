from PyQt5.QtWidgets import QWidget, QPushButton, QFrame, QApplication
from PyQt5.QtGui import QColor
import sys

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        self.col = QColor(0,0,0)

        # RED
        redb = QPushButton('red', self)
        redb.setCheckable(True)
        redb.move(10,10)
        redb.clicked.connect(self.setColor)

        # Green
        greenb = QPushButton('green', self)
        greenb.setCheckable(True)
        greenb.move(10, 60)
        greenb.clicked.connect(self.setColor)

        # Blue
        blueb = QPushButton('blue', self)
        blueb.setCheckable(True)
        blueb.move(10, 110)
        blueb.clicked.connect(self.setColor)

        # Squre 상자 생성 QFrame 이용
        self.squre = QFrame(self)
        self.squre.setGeometry(150,20,100,100)
        self.squre.setStyleSheet("QWidget {background-color: %s }" %
                                 self.col.name())

        # 기본 화면 구성 설정
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QCheckBox')
        self.show()

    def setColor(self, pressed):   # state 값을 받아온다
        print("tt")
        source = self.sender()
        if pressed:
            val = 255
        else :
            val = 0
        if source.text() == "red":
            self.col.setRed(val)
        elif source.text() == "green":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)
        self.squre.setStyleSheet("QFrame {background-color: %s}" % self.col.name())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
