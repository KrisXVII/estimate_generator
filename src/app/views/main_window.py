from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


def generate_estimate():
    print("palle")


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.setWindowTitle("Genera preventivo")

        btn = QPushButton("Genera Preventivo")
        btn.clicked.connect(generate_estimate)
        btn.setFixedHeight(100)
        layout.addWidget(btn)

        self.setFixedSize(QSize(500, 400))


