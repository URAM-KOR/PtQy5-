import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Exam(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton("눌러", self)
        btn.resize(btn.sizeHint())
        btn.setToolTip("기능없음")
        btn.move(25, 30)
        btn.clicked.connect(QCoreApplication.instance().quit)


        self.resize(500, 500)
        self.setGeometry(300, 300, 400, 500)
        self.setWindowTitle('첫번째 학습')

        self.statusBar()  # 상태표시줄 생성
        self.statusBar().showMessage("상태표시줄")

        menu = self.menuBar()              #메뉴 생성
        menu_file = menu.addMenu('File')    #그룹 생성
        menu_edit = menu.addMenu('Edit')

        file_exit = QAction('Exit', self)    #메뉴 객체 생성
        file_exit.setShortcut('Ctrl+Q')
        file_exit.setStatusTip('누르면 죵료')
        new_txt = QAction("텍스트 파일",self)
        new_py = QAction("파이썬 파일",self)

        file_exit.triggered.connect(QCoreApplication.instance().quit)


        file_new = QMenu('New', self)  #서브 그룹

        file_new.addAction(new_txt)     #서브 메뉴추가
        file_new.addAction(new_py)

        menu_file.addMenu(file_new)  # 메뉴 등록 (주 메뉴 추가)
        menu_file.addAction(file_exit)  #메뉴 등록


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
