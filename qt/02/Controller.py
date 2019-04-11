from PyQt5 import QtCore, QtGui, QtWidgets


class Controller:

    def __init__(self, db, gui):
        self.__db = db
        self.__gui = gui
        self.__gui.add_button.clicked.connect(self.insert)
        self.get_records()


    def get_records(self):
        records = self.__db.get_records()
        records.sort(key=lambda record: record['name'])
        string = '\n'
        for record in records:
            string += ', '.join([record['name'], str(record['birth']), record['phone'], record['email']]) + '\n'
        self.__gui.textBrowser.setText(string)


    def clear_form(self):
        self.__gui.name_field.clear()
        self.__gui.birth_field.clear()
        self.__gui.email_field.clear()
        self.__gui.phone_field.clear()


    def insert(self):
        user_input = {
            'name': self.__gui.name_field.text(),
            'birth': self.__gui.birth_field.dateTime().toPyDateTime(),
            'email': self.__gui.email_field.text(),
            'phone': self.__gui.phone_field.text()
        }
        self.__db.insert(user_input)
        print('Record has been added!')
        self.clear_form()
        self.get_records()