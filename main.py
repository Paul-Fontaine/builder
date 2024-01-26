import sys
from PySide6.QtWidgets import QApplication
from dialog_box_director import DialogBoxDirector
from dialog_box_one_button_builder import DialogBoxOneButtonBuilder
from dialog_box_n_button_builder import DialogBoxNButtonBuilder
from dialog_box import DialogBox

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # create the director
    dialog_box_director: DialogBoxDirector = DialogBoxDirector()

    # create a one button dialog box
    one_button_builder: DialogBoxOneButtonBuilder = DialogBoxOneButtonBuilder()
    dialog_box_director.set_dialog_box_builder(one_button_builder)
    dialog_box_director.build_dialog_box()
    dialog_box1: DialogBox = dialog_box_director.get_dialog_box()

    # create a n button dialog box, keep the same director but change the builder
    n_buttons_builder = DialogBoxNButtonBuilder(5)
    dialog_box_director.set_dialog_box_builder(n_buttons_builder)
    dialog_box_director.build_dialog_box()
    dialog_box2 = dialog_box_director.get_dialog_box()

    dialog_box1.show()
    dialog_box2.show()

    sys.exit(app.exec())

