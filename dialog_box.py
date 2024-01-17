from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton


class DialogBox(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.h_layout1: QHBoxLayout = QHBoxLayout(self)
        self.h_layout2: QHBoxLayout = QHBoxLayout(self)

    def set_title(self, title: str):
        self.setWindowTitle(title)

    def add_text(self, label: QLabel):
        self.h_layout1.addWidget(label)

    def add_button1(self, button: QPushButton):
        self.h_layout2.addWidget(button)

    def add_button2(self, button: QPushButton):
        self.h_layout2.addWidget(button)
