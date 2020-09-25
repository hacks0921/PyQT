from PyQt5.QtWidgets import QWidget,QPushButton,QLineEdit,QInputDialog,QApplication

import sys

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        self.btn = QPushButton('Dialog',self)
        self.btn.move(20,20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130,22)

        #기본 화면 구성 설정
        self.setGeometry(300,300,300,150)
        self.setWindowTitle('input dialog')
        self.show()

    def showDialog(self):
        text,ok = QInputDialog.getText(self,'input Dialog','Enter your name:')
        # 제목 설정 / 기본 메시지창 설정
        if ok:
            self.le.setText(str(text))

if __name__ =='__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())



