from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QHBoxLayout, QLineEdit, QComboBox
from PyQt5.QtGui import QPixmap
import sys

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        self.lbl = QLabel("Ubuntu", self)

        combo = QComboBox(self)
        combo.addItem("a")
        combo.addItem("b")
        combo.addItem("c")
        combo.addItem("d")
        combo.addItem("e")

        combo.move(50,50)
        self.lbl.move(50,150)

        combo.activated[str].connect(self.onAcitvated)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('QComboBox')
        self.show()

    def onAcitvated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
