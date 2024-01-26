from dialog_box_builder import DialogBoxBuilder
from PySide6.QtWidgets import QLabel, QPushButton


class DialogBoxNButtonBuilder(DialogBoxBuilder):
    def __init__(self, number_of_buttons: int = 2):
        DialogBoxBuilder.__init__(self, number_of_buttons)
        self.create_new_dialog_box()

    def build_title(self):
        self._dialog_box.add_title(f'{self.number_of_buttons} buttons')
        return self

    def build_text(self):
        self._dialog_box.add_text(QLabel('some text'))
        return self

    def build_button1(self):
        self._dialog_box.add_button1(QPushButton('button1'))
        return self

    def build_button2(self):
        self._dialog_box.add_button2(QPushButton('button2'))
        return self

    def build_button(self):
        self.number_of_buttons_built += 1
        self._dialog_box.add_button(
            QPushButton(f'button{self.number_of_buttons_built}')
        )
        return self
