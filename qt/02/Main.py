import sys
from AppWindow import AppWindow
from Database import Database
from Controller import Controller
from PyQt5.QtWidgets import QApplication, QWidget, QDialog



def main():
    app = QApplication(sys.argv)
    appWindow = AppWindow()
    db = Database()
    controller = Controller(db,appWindow.gui)
    appWindow.show()
    sys.exit(app.exec())



if __name__ == '__main__':
    main()