from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt
import sys

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        cb = QCheckBox('show title',self)
        cb.move(20, 20)
        cb.toggle()   #기본 설정을 체크로 해줌
        cb.stateChanged.connect(self.changeTitle)

        # 기본 화면 구성 설정
        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('QCheckBox')
        self.show()

    def changeTitle(self, state):   # state 값을 받아온다
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBOX 선택')
        else:
            self.setWindowTitle('선택 안함')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
