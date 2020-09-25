from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys, cv2, numpy, time


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("cam exam")
        self.setGeometry(150, 150, 650, 540)
        self.initUI()

    def initUI(self):
        self.cpt = cv2.VideoCapture(0)
        self.fps = 24
        self.sens = 300
        _, self.img_o = self.cpt.read()  # 영상 한컷을 읽어 드리겠다, _, 중요하지 않고 다음꺼
        self.img_o = cv2.cvtColor(self.img_o, cv2.COLOR_RGB2GRAY)  # cv2 변환 RGB를 GRAY로 변경
        cv2.imwrite('img_o.jpg', self.img_o)  # image를 저장한다 img_o.jpg로 저장

        # self.cnt = 0  # 디버깅용 평가를 위해

        # Cam  영상이 들어갈 위치를 저장
        self.frame = QLabel(self)
        self.frame.resize(640, 480)
        self.frame.setScaledContents(True)  # Label 크기에 맞게끔 CAM 영상이 들어옴
        self.frame.move(5, 5)

        # Push 버튼 생성
        self.btn_on = QPushButton("켜기", self)
        self.btn_on.resize(100, 25)
        self.btn_on.move(5, 490)
        self.btn_on.clicked.connect(self.start)

        self.btn_off = QPushButton("끄기", self)
        self.btn_off.resize(100, 25)
        self.btn_off.move(5 + 100 + 5, 490)
        self.btn_off.clicked.connect(self.stop)

        # 레이블 추가 감도 fps 현상 표시

        self.prt = QLabel(self)
        self.prt.resize(200, 25)
        self.prt.move(5 + 105 + 105, 490)

        # 슬라이더 표시

        self.sldr = QSlider(Qt.Horizontal, self)
        self.sldr.resize(100, 25)
        self.sldr.move(5 + 105 + 105 + 200, 490)
        self.sldr.setMinimum(1)
        self.sldr.setMaximum(30)
        self.sldr.setValue(24)
        self.sldr.valueChanged.connect(self.setFps)

        self.sldr1 = QSlider(Qt.Horizontal, self)
        self.sldr1.resize(100, 25)
        self.sldr1.move(5 + 105 + 105 + 200 + 105, 490)
        self.sldr1.setMinimum(50)
        self.sldr1.setMaximum(500)
        self.sldr1.setValue(300)
        self.sldr1.valueChanged.connect(self.setSens)

        self.show()

    def setFps(self):
        self.fps = self.sldr.value()
        self.prt.setText("FPS" + str(self.fps) + "로 조정!")
        self.timer.stop()
        self.timer.start(1000 / self.fps)
        print('setFps')

    def setSens(self):
        self.sens = self.sldr1.value()
        self.prt.setText("감도" + str(self.sens) + "로 조정!")
        print('setSens')

    def start(self):
        self.timer = QTimer() # 타이머 객체 불러기
        self.timer.timeout.connect(self.nextFrameslot)  # 타임아웃 신호 발생시 nextFrameslot 호출
        # 타이머가 끝날떄마다 nextFrame slot이 실행됨
        self.timer.start(1000 / self.fps)  # 1000 / 24 --> 1000ms = 1sec
        print('start')

    def nextFrameslot(self):  # 반복적으로 실행 됨
        _, cam = self.cpt.read()  # 이미지 영상 1컷을 가지고옴
        print("1")
        cam = cv2.cvtColor(cam, cv2.COLOR_BGR2RGB)  # BGR을 RGB로 변환해줌
        print("2")
        # cam = cv.flip(cam,0)  #영상 0: 상하 반전, 1: 좌우 반전 ==> 강의중 편의를 위해 추가함
        #
        self.img_p = cv2.cvtColor(cam, cv2.COLOR_RGB2GRAY)  # img_p 회색조로 변경해서 저장
        cv2.imwrite('img_p.jpg', self.img_p)  # img_p를 self.img_p로 넣어줌
        self.compare(self.img_o, self.img_p)  # img_o, img_p를 비교함
        self.img_o = self.img_p.copy()  # img_p를 img_o에 복사해줌
        # 보여주는 부분
        # cam 영상의 가로높이/세로높이/rgb888형태로 변환
        img = QImage(cam, cam.shape[1], cam.shape[0], QImage.Format_RGB888)
        print("3")
        pix = QPixmap.fromImage(img)  # img 객책를 넣어줌
        print("4")
        self.frame.setPixmap(pix)
        print("5")

        print("nextFrameslot")

    def stop(self):
        self.frame.setPixmap(QPixmap.fromImage(QImage()))
        self.timer.stop()
        print('stop')

    def compare(self, img_o,img_p):
        err = numpy.sum((img_o.astype("float")-img_p.astype("float"))**2)
        err/= float(img_o.shape[0] * img_p.shape[1])
        if (err>=self.sens):
            t = time.localtime()
            self.prt.setText("{}-{}-{} {}:{}:{} 움직임 감지".format(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour,
                                                         t.tm_min,t.tm_sec))

app = QApplication([])
ex = Example()
sys.exit(app.exec_())








