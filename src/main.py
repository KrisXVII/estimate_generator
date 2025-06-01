from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from src.app.views.main_window import MainWindow
import sys # for command line arguments


app = QApplication(sys.argv) # application instance, pass [] if won't be using command line arguments

window = MainWindow()
window.show() # windows are hidden by default

app.exec_()
