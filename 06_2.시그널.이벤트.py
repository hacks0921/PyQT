import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('signal and slot')
        self.show()
        # 윈도우 화면 구성

    def keyPressEvent(self, e):
        if e.key() == QT.Key_Escape:
            self.close()
        # KeyPressEvent 발생 시 (키보드이 특정 값이 들어왔을 경우)
        # 해당 값을 받아서 if 문을 진행 함.

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
