from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from src.app.views.main_window import MainWindow
import sys


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
