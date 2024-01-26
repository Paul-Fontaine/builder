from dialog_box_builder import DialogBoxBuilder


class DialogBoxDirector:
    def __init__(self):
        self.__dialog_box_builder: DialogBoxBuilder = None

    def set_dialog_box_builder(self, dbb: DialogBoxBuilder):
        self.__dialog_box_builder: DialogBoxBuilder = dbb

    def get_dialog_box(self):
        return self.__dialog_box_builder.get_dialog_box()

    def build_dialog_box(self):
        if self.__dialog_box_builder is None:
            print('No builder set !')
            raise AttributeError('No builder set !')

        self.__dialog_box_builder\
            .create_new_dialog_box()\
            .build_title()\
            .build_text()

        for _ in range(self.__dialog_box_builder.number_of_buttons):
            self.__dialog_box_builder.build_button()

