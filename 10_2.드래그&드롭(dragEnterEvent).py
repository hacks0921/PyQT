import sys
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication, QLineEdit

class Button(QPushButton):
    def __init__(self, title, parent):  # 버튼에 나타난 텍스트 초기화
        super().__init__(title, parent)  # 상위 클레스 객체 초기화
        self.setAcceptDrops(True)  # 버튼 자체의 드롭 기능 활성화

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):  # 만약에 일반적인 텍스트가 들어왔을 경우에 허용
            e.accept()
        else:
            e.ignore()
        # e.accept()

    def dropEvent(self, e):  # 드롭이 되었을경우 텍스트를 버튼에 넣는다
        self.setText(e.mimeData().text())

class Example(QWidget):  #위젯을 상속 받는다
    def __init__(self):
        super().__init__() # 상위 객체 클레스 초기화
        self.initUI()  # UI 호출하기

    def initUI(self):
        edit = QLineEdit('',self)
        edit.setDragEnabled(True) # 위젯창에 있는 드레그 기능 활성화
        edit.move(30,65)

        button = Button("Button", self)
        button.move(190,65)

        self.setWindowTitle('Simple drag and drop')
        self.setGeometry(300,300,300,150)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
