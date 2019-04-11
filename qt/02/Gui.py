from PyQt5 import QtCore, QtGui, QtWidgets



class Gui(object):


    def __init__(self, db):
        self.__db = db


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(531, 388)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 531, 401))
        self.tabWidget.setObjectName("tabWidget")
        self.records = QtWidgets.QWidget()
        self.records.setObjectName("records")
        self.textBrowser = QtWidgets.QTextBrowser(self.records)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 531, 361))
        self.textBrowser.setObjectName("textBrowser")
        self.tabWidget.addTab(self.records, "")
        self.new_record = QtWidgets.QWidget()
        self.new_record.setObjectName("new_record")
        self.formLayoutWidget = QtWidgets.QWidget(self.new_record)
        self.formLayoutWidget.setGeometry(QtCore.QRect(150, 60, 271, 175))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.nameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.birthLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.birthLabel.setObjectName("birthLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.birthLabel)
        self.birth_field = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.birth_field.setObjectName("birth_field")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.birth_field)
        self.phoneLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.phoneLabel.setObjectName("phoneLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.phoneLabel)
        self.phone_field = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.phone_field.setObjectName("phone_field")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.phone_field)
        self.eMailLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.eMailLabel.setObjectName("eMailLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.eMailLabel)
        self.email_filed = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.email_filed.setObjectName("email_filed")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.email_filed)
        self.add_button = QtWidgets.QPushButton(self.formLayoutWidget)
        self.add_button.setObjectName("add_button")
        self.add_button.clicked.connect(self.insert)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.add_button)
        self.name_filed = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.name_filed.setObjectName("name_filed")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name_filed)
        self.tabWidget.addTab(self.new_record, "")
        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.get_records()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Telephon book by Peter Cs. Forro"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.records), _translate("Dialog", "Records"))
        self.nameLabel.setText(_translate("Dialog", "Name"))
        self.birthLabel.setText(_translate("Dialog", "Birth"))
        self.phoneLabel.setText(_translate("Dialog", "Phone"))
        self.eMailLabel.setText(_translate("Dialog", "E-mail"))
        self.add_button.setText(_translate("Dialog", "Add to records!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.new_record), _translate("Dialog", "Add record"))



    def get_records(self):
        records = self.__db.get_records()
        records.sort(key=lambda record:record['name'])
        string = ''
        for record in records:
            string += ', '.join([record['name'],str(record['birth']),record['phone'],record['email']]) + '\n'
        self.textBrowser.setText(string)



    def clear_form(self):
        self.name_filed.clear()
        self.phone_field.clear()
        self.email_filed.clear()
        self.birth_field.clear()



    def insert(self):
        user_input = {
            'name' : self.name_filed.text(),
            'birth' : self.birth_field.dateTime().toPyDateTime(),
            'email' : self.email_filed.text(),
            'phone' : self.phone_field.text()
        }
        self.__db.insert(user_input)
        print('Record has been added!')
        self.clear_form()
        self.get_records()