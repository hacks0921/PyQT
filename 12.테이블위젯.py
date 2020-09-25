#-*- coding:utf-8 -*-
import sys, pickle
from PyQt5.QtWidgets import QApplication,QWidget,QTableWidget,QTableWidgetItem,QVBoxLayout,QPushButton

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.size = 5  # 테이블의 싸이즈 지정하기위한 변수 / Claas 영역을 지정하기 위해 Self를 붙인다
        self.initUI()

    def initUI(self):
        self.setWindowTitle('서종학')
        self.setGeometry(50, 50, 660, 240)

        self.createTable()  # x테이블 형성
        self.btn = QPushButton('저장')
        self.btn.clicked.connect(on_cl)  # 버튼 연결

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.table)
        self.layout.addWidget(self.btn)

        self.setLayout(self.layout)
        self.show()

    def createTable(self):
        self.table = QTableWidget()
        self.table.setRowCount(self.size)  # 행 개수 지정
        self.table.setColumnCount(self.size)  # 열 개수 지정
        self.table.setHorizontalHeaderLabels(('이름','국어','영어,','수학'))  # 필드명 지정  / 지정하지 않으면 일련번호

        try:
            fp = open("out.txt", "rb")  # 파일을 읽어와서 rb읽기모드로 읽어온다
            for r in range(self.size):  # 중복 포문을 가지고 파일을 읽어 드린다
                for c in range(self.size):
                    self.table.setItem(r,c,QTableWidgetItem(str(pickle.load(fp))))
            fp.close()  # 파일을 닫아준다

        except:
            for r in range(self.size):  # 파일이 없으면 아래 내용으로 진행
                for c in range(self.size):
                    self.table.setItem(r,c,QTableWidgetItem("")) # 공백으로 초기화 시켜준다
def on_cl():
    fp = open("out.txt", "wb")
    for r in range(ex.size):
        for c in range(ex.size):
            pickle.dump(ex.table.item(r,c).text(),fp)   # 셀의 각 위치를 돌면서 값을 읽고 파일에 작성한다

    fp.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())