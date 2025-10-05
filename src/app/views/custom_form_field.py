from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp

class FormField(QWidget):
    def __init__(self, label_text, placeholder="", validator_regex=None, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)  # Remove extra margins

        # Label
        self.label = QLabel(label_text)
        layout.addWidget(self.label)
        self.input = QLineEdit()
        self.input.setPlaceholderText(placeholder)

        if validator_regex:
            self.input.setValidator(QRegExpValidator(QRegExp(validator_regex)))

        # Styling
        self.input.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 2px solid #ccc;
                border-radius: 4px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border-color: #007acc;
            }
        """)

        layout.addWidget(self.input)

    def get_value(self):
        return self.input.text()

    def set_value(self, value):
        self.input.setText(value)

    def clear(self):
        self.input.clear()