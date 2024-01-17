from abc import ABC, abstractmethod
from dialog_box import DialogBox


class DialogBoxBuilder:
    def __init__(self):
        self._dialog_box: DialogBox = None

    def create_new_dialog_box(self):
        self._dialog_box = DialogBox()

    def get_dialog_box(self) -> DialogBox:
        return self._dialog_box

    @abstractmethod
    def build_title(self):
        pass

    @abstractmethod
    def build_text(self):
        pass

    @abstractmethod
    def build_button1(self):
        pass

    @abstractmethod
    def build_button2(self):
        pass
