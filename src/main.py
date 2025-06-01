import sys  # for command line arguments
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from app.views.main_window import MainWindow

app = QApplication(sys.argv)  # application instance, pass [] if won't be using command line arguments

window = MainWindow()
window.show()  # windows are hidden by default

app.exec_()
