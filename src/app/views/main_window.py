from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Genera preventivo")

        label = QLabel("Generatore preventivo")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)
        self.setFixedSize(QSize(400, 300))


def generate_estimate():
    print("let's do it")
