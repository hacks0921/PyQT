from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QHBoxLayout, QLineEdit
from PyQt5.QtGui import QPixmap
import sys

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        self.lbl = QLabel(self)  # lbl 생성
        qle = QLineEdit(self)  #qle 생성

        qle.move(60,100) # qle 위치
        self.lbl.move(60,40)  # lbl 위치

        qle.textChanged[str].connect(self.onChanged)  #qle 텍스트가 변경되면 연결한다

        self.setGeometry(300,300,280,170)
        self.setWindowTitle('QLineEdit')
        self.show()

    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
