from PyQt5.QtWidgets import *
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(1200,200,300,300)

        self.btnList = []
        self.btnTop = 100
        self.cnt =0

        self.lbl = QLabel ("생성될 버튼의 수를 입력하세요", self)
        self.lbl.move(10,10)

        self.txt = QLineEdit("", self)
        self.txt.move(10,self.lbl.height())  # 레이블의 높이 값으로 지정

        self.btn = QPushButton("버튼생성",self)
        # self.btn.resize(QSize(80,25))
        self.btn.resize(80, 25) # 버튼의 싸이즈 생성
        self.btn.move(10, self.lbl.height()+ self.txt.height())

        self.btn.clicked.connect(self.createBtn)
        self.show()

    def createBtn(self):
        self.cnt = int(self.txt.text())  # txt를 정수로 변환 -> cnt 변수에 받아서 사용
        for i in range(self.cnt):
            self.btnList.append(QPushButton(str(i+1)+"번째 버튼", self))  # QPushButton 누적 / 버튼의 이름을 생성
            self.btnList[i].resize(80,25) # 싸이즈 조정
            self.btnList[i].move(10,self.btnTop + (i*25))  # 버튼의 위치 조정 25만큼씩 아래 표시
            self.btnList[i].show()





app = QApplication([])
ex = Example()
sys.exit(app.exec_())

