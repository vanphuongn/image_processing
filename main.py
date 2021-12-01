import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication

from MainWindow import  MainWindow
from canvas import Canvas
from PyQt5.QtGui import  *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # main_win = MainWindow()
    # main_win.show()

    canvas = Canvas()
    canvas.setGeometry(0,0,1920 ,1080)
    pixmap = QPixmap("./images/phuong.jpg")
    canvas.loadPixmap( pixmap)
    canvas.show()
    sys.exit(app.exec())
