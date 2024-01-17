from dialog_box_builder import DialogBoxBuilder


class DialogBoxDirector:
    def __init__(self):
        self.__dialog_box_builder: DialogBoxBuilder = None

    def set_dialog_box_builder(self, dbb: DialogBoxBuilder):
        self.__dialog_box_builder = dbb

    def get_dialog_box(self):
        self.__dialog_box_builder.get_dialog_box()

    def build_dialog_box(self):
        if self.__dialog_box_builder is None:
            raise AttributeError

        dbb = self.__dialog_box_builder
        dbb.create_new_dialog_box()
        dbb.build_title()
        dbb.build_text()
        dbb.build_button1()
        dbb.build_button2()
