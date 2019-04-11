import sys
from AppWindow import AppWindow
from Database import Database
from PyQt5.QtWidgets import QApplication, QWidget, QDialog


def main():
    db = Database()
    app = QApplication(sys.argv)
    window = AppWindow(db)
    window.show()
    sys.exit(app.exec())



if __name__ == '__main__':
    main()