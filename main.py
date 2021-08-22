import sys, random
from test import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit




app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

#Code

#chars = '+-/*!&#?=@<>abcdefghijklnmopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

def gen():
    number = int(ui.lineEdit.text())
    password = ''


    if ui.radioButton.isChecked():
        chars_int = '+-/*!&#?=@<>1234567890'
        for x in range(number):
            password += random.choice(chars_int)
            ui.lineEdit_2.setText(str(password))


    if ui.radioButton_2.isChecked():
        chars_lit = 'abcdefghijklnmopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for x in range(number):
            password += random.choice(chars_lit)
            ui.lineEdit_2.setText(str(password))


    if ui.radioButton_3.isChecked():
        chars = '+-/*!&#?=@<>abcdefghijklnmopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234567890'
        for x in range(number):
            password += random.choice(chars)
            ui.lineEdit_2.setText(str(password))

    if ui.radioButton_4.isChecked():
        chars = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        for x in range(number):
            password += random.choice(chars)
            ui.lineEdit_2.setText(str(password))

    if ui.radioButton_5.isChecked():
        chars = '+-/*!&#?=@<>абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ12345678901234567890'
        for x in range(number):
            password += random.choice(chars)
            ui.lineEdit_2.setText(str(password))

    if ui.radioButton_6.isChecked():
        chars = '+-/*!&#?=@<>абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklnmopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234567890'
        for x in range(number):
            password += random.choice(chars)
            ui.lineEdit_2.setText(str(password))

def clr():
    ui.lineEdit.clear()
    ui.lineEdit_2.clear()


ui.pushButton.clicked.connect(gen)
ui.pushButton_2.clicked.connect(clr)
sys.exit(app.exec_())