from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from widget.ui_mainwindow import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.uic.newProjectBtn.clicked.connect(showColorDialog)
    def show(self):
        self.main_win.show()
    def hide(self):
        self.main_win.hide()
def showColorDialog():
        color = QColorDialog.getColor()
        if color.isValid():
            print("color name :  "+color.name())

