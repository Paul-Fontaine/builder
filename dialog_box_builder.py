from abc import ABC, abstractmethod
from dialog_box import DialogBox


class DialogBoxBuilder(ABC):
    def __init__(self, number_of_buttons: int):
        self._dialog_box: DialogBox = None
        self.number_of_buttons: int = number_of_buttons
        self.number_of_buttons_built: int = 0

    def create_new_dialog_box(self):
        self._dialog_box = DialogBox()
        return self

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

    @abstractmethod
    def build_button(self):
        raise NotImplementedError
