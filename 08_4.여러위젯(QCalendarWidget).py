from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QCalendarWidget
from PyQt5.QtCore import QDate
import sys

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout(self)  # Vbox Layout을 설정
        cal = QCalendarWidget(self)  # CalenderWidget 설정
        cal.setGridVisible(True) # Calender에 그리드를설정 / 달력 표시 옵션
        cal.clicked[QDate].connect(self.showDate) # 선택된 Qdate를 showDate에 연결함
        vbox.addWidget(cal)  # Vobx레이아웃에 Cal 위젯을 추가함

        self.lbl = QLabel(self)  #lbl 설정
        date = cal.selectedDate()  # data에 선택된 날자를 받음
        self.lbl.setText(date.toString()) # lbl에 날자를 문자 형식으로 변경하여 보여줌
        vbox.addWidget(self.lbl) # Vobx레이아웃에 lbl 위젯을 추가함

        self.setLayout(vbox)  # Layout 구성을 vbox로 선정함
        # 기본 화면 구성 설정
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calender')
        self.show()

    def showDate(self,date):  # date 값을 받아서 온다
        self.lbl.setText(date.toString()) #lbl에 받아온 data 값을 보여줌

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
