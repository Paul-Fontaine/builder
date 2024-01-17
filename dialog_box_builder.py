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
        raise NotImplementedError

    @abstractmethod
    def build_text(self):
        raise NotImplementedError

    @abstractmethod
    def build_button1(self):
        raise NotImplementedError

    @abstractmethod
    def build_button2(self):
        raise NotImplementedError
