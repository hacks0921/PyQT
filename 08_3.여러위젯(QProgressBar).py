from PyQt5.QtWidgets import QWidget, QApplication, QProgressBar, QPushButton
from PyQt5.QtCore import QBasicTimer
import sys

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.pbar = QProgressBar(self) #pbar 프로그래스바 설정
        self.pbar.setGeometry(30,40,200,25)  # 위치 설정

        self.btn = QPushButton('start',self) #푸시버든 생성
        self.btn.move(40,80) # 버튼 위치 설정
        self.btn.clicked.connect(self.doAction)  # 클릭버튼 doAction 연결

        self.timer = QBasicTimer()
        self.step = 0

        # 기본 화면 구성 설정
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgreseBar')
        self.show()

    def timerEvent(self, e): # 일정 시간 단위로 동작
        if self.step >=  100:
            self.timer.stop()  #100이상일 경우 멈추고 1증가
            self.btn.setText('Finished')
            return

        self.step = self.step + 1 # 100보다 작은경우 Step을 1씩 증가
        self.pbar.setValue(self.step)  # pbar에 표시


    def doAction(self):
        if self.timer.isActive():  # 타이머 활성화 여부 확인
            self.timer.stop() # 활성화 상태면 중단
            self.btn.setText('Start') # 타이머가 실행이 되고 있으면 Start로 변경해라
        else:
            self.timer.start(100,self) # 100/1000= 0.1초 마다 타이머를 실행
            self.btn.setText('stop') # 버튼을 stop으로 변경해라

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
