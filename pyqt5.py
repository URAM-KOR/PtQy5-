import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton("눌러", self)
        btn.resize(btn.sizeHint())
        btn.setToolTip("툴팁:기능없음")
        btn.move(25, 30)
        btn.clicked.connect(QCoreApplication.instance().quit)


        self.resize(500, 500)
        self.setGeometry(300, 300, 400, 500)
        self.setWindowTitle('첫번째 학습')
        self.show()

    def closeEvent(self, QCloseEvent):
        ans = QMessageBox.question(self, "종료할거니", " yes 누르면 종료 ",
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if ans == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())
