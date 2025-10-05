import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from app.views.main_window import MainWindow

# Main application execution
if __name__ == "__main__":
    app = QApplication(sys.argv)

    icon = QIcon('assets/estimate.png')
    app.setWindowIcon(icon)

    window = MainWindow()

    window.setWindowIcon(icon)
    window.show()

    sys.exit(app.exec_())
