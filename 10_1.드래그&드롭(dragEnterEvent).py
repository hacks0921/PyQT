import sys
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication
from PyQt5.QtCore import  Qt, QMimeData
from PyQt5.QtGui import QDrag

class Button(QPushButton):
    def __init__(self, title, parent):  # 버튼에 나타난 텍스트 초기화
        super().__init__(title, parent)  # 상위 클레스 객체 초기화

    def mouseMoveEvent(self, e):  # 버튼 위에서 마우스가 움직이고 있을때 발생하는 이벤트
        # if e.buttons() != Qt.RightButton: #마우스 오른쪽 버튼이 눌린 상태가 아니면 이벤트를 종료
        if e.buttons() != Qt.LeftButton:  # 마우스 오른쪽 버튼이 눌린 상태가 아니면 이벤트를 종료
            return
        mimeData = QMimeData()  # 다양한 멀티미디어 데이터를 다룬다
        drag = QDrag(self) # 드레그 객체 생성
        drag.setMimeData(mimeData)
        drag.exec_(Qt.MoveAction)  # 객체 활성화

    def mousePressEvent(self, e):
        super().mousePressEvent(e)
        if e.button() == Qt.LeftButton:
            print('press')

class Example(QWidget):  #위젯을 상속 받는다
    def __init__(self):
        super().__init__() # 상위 객체 클레스 초기화
        self.initUI()  # UI 호출하기

    def initUI(self):
        self.setAcceptDrops(True) # 드롭이벤트 활성화
        self.button = Button('Button',self)  #버튼 객책 생성
        self.button.move(100,65)
        self.setWindowTitle('click or move')
        self.setGeometry(300,300,280,150) # 화면 구성

    def dragEnterEvent(self, e):
        e.accept()  # 드레그된 데이터를 허용한다

    def dropEvent(self, e): #드롭 이벤트 드레그하다 마우스를 놓았을떄 버튼 위치 이동
        position = e.pos() # 위치 지정
        self.button.move(position)  # 버튼의 위치를 옮기는 역할
        e.accept()  # 허용 여부 지정

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
