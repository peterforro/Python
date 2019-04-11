# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Gui(object):

    def __init__(self,util):
        self.__util = util


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(207, 347)
        self.add_btn = QtWidgets.QPushButton(Dialog)
        self.add_btn.setGeometry(QtCore.QRect(10, 80, 151, 41))
        self.add_btn.setObjectName("add_btn")
        self.add_btn.clicked.connect(self.add)
        self.input1 = QtWidgets.QLineEdit(Dialog)
        self.input1.setGeometry(QtCore.QRect(30, 30, 113, 25))
        self.input1.setObjectName("input1")
        self.print_btn = QtWidgets.QPushButton(Dialog)
        self.print_btn.setGeometry(QtCore.QRect(10, 150, 151, 41))
        self.print_btn.setObjectName("print_btn")
        self.print_btn.clicked.connect(self.print)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.add_btn.setText(_translate("Dialog", "Add"))
        self.print_btn.setText(_translate("Dialog", "print"))


    def add(self):
        value = int(self.input1.text())
        self.__util.add(value)
        self.input1.setText('')


    def print(self):
        print(self.__util)

