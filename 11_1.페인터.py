import sys, random
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter,QColor,QFont,QPen, QBrush
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.a ="가나다라마바사"
        self.setGeometry(300,300,500,450)
        self.setWindowTitle('Drawing text')
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        #pain와 관련된 내용은 qp.begin과 qp.end 사이에 있어야 합니다.
        qp.begin(self)
        # self.drawText(event,qp)
        # self.drawPoints(qp)
        # self.drawRectangles(qp)
        # self.drawLines(qp)
        self.drawBrushes(qp)
        qp.end

    def drawText(self, event, qp):
        qp.setPen(QColor(168,34,3)) # 색상 표시 (R,G,B)
        qp.setFont(QFont('gulim',24))  # 폰트 크기 설정
        # test를 써준다 / rect는 좌상,우하 좌표 추출 / 좌표 안에서 12시방향으로 정렬
        qp.drawText(event.rect(),Qt.AlignHCenter,self.a)

    def drawPoints(self,qp):
        qp.setPen(Qt.red)
        size = self.size()

        for i in range(1000):
            x = random.randint(0, size.width())  # 0~가로 사이즈 범위 랜덤 정수 생성
            y = random.randint(0, size.width())  # 0~세로 사이즈 범위 랜덤 정수 생성
            qp.drawPoint(x,y)

    def drawRectangles(self,qp):  # 사각형에 색 그리기
        col = QColor()
        col.setNamedColor('#521E8D') # 16진수로 지정
        qp.setPen(col)  # QPainter /  Set pen에 col (색상) 선정

        qp.setBrush(QColor(100,0,0)) # 브러쉬 색상선정
        qp.drawRect(10,45,90,60)  # 좌상단 x,y,가로,세로

        qp.setBrush(QColor(180, 0, 0, 10))  # 브러쉬 색상선정  # R,G,B 투명도
        qp.drawRect(130, 45, 90, 60)  # 좌상단 x,y,가로,세로

        qp.setBrush(QColor(225, 0, 0))  # 브러쉬 색상선정
        qp.drawRect(250, 45, 90, 60)  # 좌상단 x,y,가로,세로

    def drawLines(self,qp):
        pen = QPen(Qt.black,2,Qt.SolidLine)  # 색/두께/ 타입

        qp.setPen(pen)
        qp.drawLine(20,100,250,100)

        pen.setStyle(Qt.DashLine) # 펜스타일  변경
        qp.setPen(pen)
        qp.drawLine(20,140,250,140) # 처음(X,Y) / 끝(X',Y')

        pen.setStyle(Qt.DashDotLine)
        qp.setPen(pen)
        qp.drawLine(20,180,250,180)

        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1,4,5,4])
        qp.setPen(pen)
        qp.drawLine(20, 300, 250, 300)

    def drawBrushes(self,qp):
        brush = QBrush(Qt.SolidPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 15, 90, 60)

        brush.setStyle(Qt.Dense1Pattern)
        qp.setBrush(brush)
        qp.drawRect(130, 15, 90, 60)

        brush.setStyle(Qt.Dense2Pattern)
        qp.setBrush(brush)
        qp.drawRect(250, 15, 90, 60)

        #2열
        brush.setStyle(Qt.DiagCrossPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 105, 90, 60)

        brush.setStyle(Qt.Dense5Pattern)
        qp.setBrush(brush)
        qp.drawRect(130, 105, 90, 60)

        brush.setStyle(Qt.Dense6Pattern)
        qp.setBrush(brush)
        qp.drawRect(250, 105, 90, 60)

        #3열

        brush.setStyle(Qt.HorPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 195, 90, 60)

        brush.setStyle(Qt.VerPattern)
        qp.setBrush(brush)
        qp.drawRect(130, 195, 90, 60)

        brush.setStyle(Qt.CrossPattern)
        qp.setBrush(brush)
        qp.drawRect(250, 195, 90, 60)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
