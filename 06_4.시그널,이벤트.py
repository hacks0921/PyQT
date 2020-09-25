#[파이썬]PYQT5 공부하기(06.시그널,이벤트)


import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication

class Communicate(QObject):
    closeApp = pyqtSignal()
    # pyqtSignal 슬롯을 이용하기 위해만들어줌

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)
        # 3) closeApp과 연결된 self.close 실행

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('emit signal')
        self.show()

    def mousePressEvent(self, event):
        # 1) 마우스 클릭, 마우스 프레스 이벤트 발생
        self.c.closeApp.emit()
        # 2) 클릭 이벤트를 받아서 c,closeApp에 Emit 발생

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
