from PyQt5.QtWidgets import QWidget,QApplication,QFileDialog,QPushButton
from PyQt5.QtGui import *
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.sid = QImage("a.jpg").scaled(120,120) # 초기 이미지를 설정 120,120 Size로
        # self.sid = QImage("").scaled(120,120)

        btn = QPushButton("이미지 변경",self)
        btn.resize(btn.sizeHint())   # btn 적절히 사이즈 조절
        btn.move(20,150)
        btn.clicked.connect(self.openFileNameDialog)  # 파일 오픈 연결

        self.setGeometry(1400,250,320,200)
        self.show()

    def paintEvent(self, event):  # 2) 이미지 생성
        painter = QPainter()
        painter.begin(self)  # begin ~~~ end 사이에 이벤트 정의 (매번 불러올떄마다 실행)
        self.drawImages(painter)  # drawImage 호출하여 그림 그리기
        painter.end()


    def drawImages(self, painter):  # 3) 이미지 그리기
        # painter 객채에서 받아와서 drawImage 매소드 사용
        painter.drawImage(5,15, self.sid)  # 좌상단 5,15위치에 그림 그리기
        painter.drawImage(self.sid.width()+10, 15,
                          self.grayScale(self.sid.copy()))  # 좌상단 5,15위치에 그림 그리기

    def grayScale(self, image):
        for i in range(self.sid.width()):
            for j in range(self.sid.height()):
                c = image.pixel(i,j)
                gray = qGray(c)
                alpha = qAlpha(c)
                image.setPixel(i,j,
                               qRgba(gray,gray,gray,alpha))
        return image



    def openFileNameDialog(self): # 1) 이미지 파일 오픈
        # 경로 / 타입을 불러옴
        fileName , _ = QFileDialog.getOpenFileName(self,"불러올이미지 선택","",
                                                   "ALL Files(*);;Python Files(*.py)")
        if fileName:
             #sid 변수에 이미지를 120nt(fileName),120으로 축소하여 가지고 있음
            self.sid = QImage(fileName).scaled(120,120)  # self.sid에 120, 120크기로 저장함

app = QApplication([])
ex = Example()
sys.exit(app.exec_())

