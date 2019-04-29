from PyQt5.QtWidgets import QTableWidgetItem


class Controller:

    def __init__(self, db, gui):
        self.__db = db
        self.__gui = gui
        self.__gui.add_button.clicked.connect(self.insert)
        self.__gui.clear_button.clicked.connect(self.delete_records)
        self.get_records()
        self.load_records()


    def get_records(self):
        records = self.__db.get_records()
        records.sort(key=lambda record: record['name'])
        string = '\n'
        for record in records:
            string += ', '.join([record['name'], str(record['birth']), record['phone'], record['email']]) + '\n'
        # self.__gui.textBrowser.setText(string)



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
        self.load_records()



    def delete_records(self):
        self.__db.delete_records()
        self.load_records()
        print('Records have been deleted')



    def load_records(self):
        records = self.__db.get_records()
        self.__gui.tableView.setRowCount(len(records))
        self.__gui.tableView.setColumnCount(4)
        for i, record in enumerate(records):
            for j, value in enumerate(record.values()):
                print(value)
                self.__gui.tableView.setItem(i,j,QTableWidgetItem(str(value)))

