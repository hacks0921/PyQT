from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.img = QImage("a.jpg")
        self.refImage = QImage("b.jpg")
        if self.img.isNull():
            print("이미지 없음")
            sys.exit(1)
        self.iw = self.img.width()
        self.ih = self.img.height()

        self.setGeometry(200,200,500,500)
        self.setWindowTitle('반사')
        self.show()

    # def createReflectedImage(self):

        # self.refImage = QImage("b.jpg")
        # self.refImage = QImage(self.iw, self.ih, QImage.Format_ARGB32)  # 기존 객체 싸이즈 컴포지션 모드 설정을 위함
        # # self.refImage = QImage('b.jpg')  # 기존 객체 싸이즈 컴포지션 모드 설정
        # painter = QPainter()
        # painter.begin(self.refImage)
        # painter.drawImage(0, 0, self.img)  # 기존 이미지 복사
        # painter.setCompositionMode(QPainter.CompositionMode_DestinationIn)  # 원본이미지 불투명도
        #
        # gradient = QLinearGradient(self.iw / 2, 0, self.iw / 2, self.ih)  # 선형 그라디언트 ㅇ
        # gradient.setColorAt(1, QColor(0, 0, 0))  # 출발지점 검은색
        # gradient.setColorAt(0, Qt.transparent)  # 도착지점 투명색
        # painter.fillRect(0, 0, self.iw, self.ih, gradient)  # 원본이미지와 그라디언트가 겹친다
        # painter.end()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.draw(painter)
        painter.end()

    def draw(self,painter):
        painter.drawImage(25,15,self.img) # 25, 15 위치에 이미지를 그린다
        painter.translate(0, 2*self.ih + 15) # 가로0, 세로높이 2배에 공백 을 더한다) 좌표 중심 변경)
        painter.scale(1,-1)  # 세로 좌표 방향 반전 아래로
        painter.drawImage(125,-50,self.refImage)  # painter.drawImage(25,0,self.img)

app = QApplication([])
ex = Example()
sys.exit(app.exec_())
