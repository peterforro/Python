from gui import Gui
from util import Util
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog


class AppWindow(QDialog):

    def __init__(self, util):
        super().__init__()
        self.ui = Gui(util)
        self.ui.setupUi(self)
        self.show()

util = Util()
app = QApplication(sys.argv)
window = AppWindow(util)
window.show()
sys.exit(app.exec())