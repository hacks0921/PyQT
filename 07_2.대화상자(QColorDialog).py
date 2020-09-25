from PyQt5.QtWidgets import QWidget, QPushButton, QColorDialog, QApplication,QFrame
from PyQt5.QtGui import QColor
import sys


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        # 초기값 설정
        col = QColor(0,0,0)
        # QFrame 스타일 색상 설정
        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget {background-color: %s }"
                               % col.name())
        # 색상 위치 설정
        self.frm.setGeometry(130,22,100,100)


        # 기본 화면 구성 설정
        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('color dialog')
        self.show()

    def showDialog(self):
        col = QColorDialog.getColor()
        # 특정 색상을 받는 객체를 사용
        if col.isValid():  # OK : True, Cancel : False
            # 선택한 색상을 frm에 넣어준다
            self.frm.setStyleSheet("QWidget {background-color: %s }"
                                    % col.name())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
