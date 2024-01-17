from dialog_box_builder import DialogBoxBuilder
from PySide6.QtWidgets import QLabel, QPushButton


class DialogBoxTwoButtonBuilder(DialogBoxBuilder):
    def __init__(self):
        DialogBoxBuilder.__init__(self)
        self.create_new_dialog_box()

    def build_title(self):
        self._dialog_box.add_title('one button')

    def build_text(self):
        self._dialog_box.add_text(QLabel('some text'))

    def build_button1(self):
        self._dialog_box.add_button1(QPushButton('button1'))

    def build_button2(self):
        self._dialog_box.add_button2(QPushButton('button2'))
