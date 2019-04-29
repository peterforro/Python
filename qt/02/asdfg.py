# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(727, 426)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 701, 401))
        self.tabWidget.setObjectName("tabWidget")
        self.records = QtWidgets.QWidget()
        self.records.setObjectName("records")
        self.gridLayoutWidget = QtWidgets.QWidget(self.records)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 701, 371))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tableView = QtWidgets.QTableView(self.gridLayoutWidget)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 1)
        self.tabWidget.addTab(self.records, "")
        self.new_record = QtWidgets.QWidget()
        self.new_record.setObjectName("new_record")
        self.formLayoutWidget = QtWidgets.QWidget(self.new_record)
        self.formLayoutWidget.setGeometry(QtCore.QRect(230, 70, 271, 175))
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
        self.email_field = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.email_field.setObjectName("email_field")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.email_field)
        self.add_button = QtWidgets.QPushButton(self.formLayoutWidget)
        self.add_button.setObjectName("add_button")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.add_button)
        self.name_field = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.name_field.setObjectName("name_field")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name_field)
        self.tabWidget.addTab(self.new_record, "")
        self.options = QtWidgets.QWidget()
        self.options.setObjectName("options")
        self.clear_button = QtWidgets.QPushButton(self.options)
        self.clear_button.setGeometry(QtCore.QRect(230, 110, 231, 101))
        self.clear_button.setObjectName("clear_button")
        self.tabWidget.addTab(self.options, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.records), _translate("Dialog", "Tab 1"))
        self.nameLabel.setText(_translate("Dialog", "Name"))
        self.birthLabel.setText(_translate("Dialog", "Birth"))
        self.phoneLabel.setText(_translate("Dialog", "Phone"))
        self.eMailLabel.setText(_translate("Dialog", "E-mail"))
        self.add_button.setText(_translate("Dialog", "Add to records!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.new_record), _translate("Dialog", "Tab 2"))
        self.clear_button.setText(_translate("Dialog", "Clear Database"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.options), _translate("Dialog", "Page"))


