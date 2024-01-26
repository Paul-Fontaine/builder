from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QVBoxLayout


class DialogBox(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setMinimumSize(300, 100)
        vlayout = QVBoxLayout(self)
        self.h_layout1: QHBoxLayout = QHBoxLayout(self)
        self.h_layout2: QHBoxLayout = QHBoxLayout(self)
        vlayout.addLayout(self.h_layout1)
        vlayout.addLayout(self.h_layout2)

    def add_title(self, title: str):
        self.setWindowTitle(title)

    def add_text(self, label: QLabel):
        label.setParent(self)
        self.h_layout1.addWidget(label)

    def add_button1(self, button: QPushButton):
        button.setParent(self)
        self.h_layout2.addWidget(button)

    def add_button2(self, button: QPushButton):
        button.setParent(self)
        self.h_layout2.addWidget(button)

    def add_button(self, button: QPushButton):
        button.setParent(self)
        self.h_layout2.addWidget(button)
