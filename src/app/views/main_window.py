from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches, Pt
from datetime import date
from .const import COMPANY, ADDRESS, CITY, TAX_CODE, VAT_ID, EMAIL
import uuid
import sys
import subprocess
import os
from pathlib import Path

def generate_estimate():
    document = Document()
    header = document.sections[0].header
    document.sections[0].header_distance = Inches(1.5)
    table = header.add_table(rows=1, cols=3, width=Inches(6.5))  # Full page width
    table.autofit = False

    # col1
    left_col = table.cell(0, 0)
    left_col.width = Inches(2.5)
    left_para = left_col.paragraphs[0]
    left_para.add_run("Informazioni cliente")

    left_col.paragraphs[0].paragraph_format.border_bottom = True
    left_col.paragraphs[0].paragraph_format.border_top = True
    left_col.paragraphs[0].paragraph_format.border_left = True
    left_col.paragraphs[0].paragraph_format.border_right = True

    # col2
    middle_col = table.cell(0, 1)
    middle_col.width = Inches(1.5)
    middle_para = middle_col.paragraphs[0]
    middle_para.add_run("\n\n")
    middle_para.add_run("Preventivo").bold = True

    # col3
    right_col = table.cell(0, 2)
    right_col.width = Inches(2.5)
    right_para = right_col.paragraphs[0]
    right_para.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    right_para.add_run(COMPANY + "\n")
    right_para.add_run(ADDRESS + "\n")
    right_para.add_run(CITY + "\n")
    right_para.add_run(TAX_CODE + "\n")
    right_para.add_run(VAT_ID + "\n")
    right_para.add_run(EMAIL + "\n")

    date_sig = date.today().strftime('%d-%m-%Y')  # file signature
    uuid_sig = uuid.uuid4().hex[:8]
    document.add_paragraph("Corpo documento...")

    downloads_dir = Path.home() / "Downloads"
    filename = "Preventivo_{date}_{uuid}.docx".format(date=date_sig, uuid=uuid_sig)

    directory = downloads_dir / filename
    document.save(str(directory))
    open_file(directory)

def open_file(filepath):
    try:
        if sys.platform == "win32":
            os.startfile(filepath)
        elif sys.platform == "darwin":
            subprocess.run(["open", filepath])
        else:  # Linux
            subprocess.run(["xdg-open", filepath])
    except Exception as e:
        print(f"Error opening file: {e}")

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
