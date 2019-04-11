from PyQt5.QtWidgets import QDialog
from Gui import Gui


class AppWindow(QDialog):

    def __init__(self, db):
        super().__init__()
        self.ui = Gui(db)
        self.ui.setupUi(self)
        self.show()
