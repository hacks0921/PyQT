from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QHBoxLayout
from PyQt5.QtGui import QPixmap
import sys

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("a.jpg")

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)

        self.setLayout(hbox)
        self.move(300,200)
        self.setWindowTitle('red rock')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
