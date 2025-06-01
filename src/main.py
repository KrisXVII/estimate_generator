import sys
import shutil
from pathlib import Path
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from app.views.main_window import MainWindow

TMP_DIR = Path(__file__).parent.parent / "tmp"

def cleanup_tmp():
    try:
        for item in TMP_DIR.glob("*"):
            if item.is_file():
                item.unlink()
            elif item.is_dir():
                shutil.rmtree(item)
        print(f"Cleaned {TMP_DIR}")
    except Exception as e:
        print(f"Cleanup error: {e}")


# Main application execution
if __name__ == "__main__":
    app = QApplication(sys.argv)

    icon = QIcon('assets/estimate.png')
    app.setWindowIcon(icon)

    window = MainWindow()

    window.setWindowIcon(icon)
    window.show()

    app.aboutToQuit.connect(cleanup_tmp)

    sys.exit(app.exec_())
