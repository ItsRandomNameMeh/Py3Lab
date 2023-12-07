from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication,  QInputDialog, QLabel, QLineEdit
import math

import sys
class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Лабораторная работа №3")
        self.setGeometry(200, 150, 800, 400)

        self.LnEdA = QLabel(self)
        self.LnEdA.move(140,67)
        self.LnEdA.setFixedWidth(50)
        self.LnEdA.setFixedHeight(15)

        self.LnEdB = QLabel(self)
        self.LnEdB.move(140, 100)
        self.LnEdB.setFixedWidth(50)
        self.LnEdB.setFixedHeight(15)

        self.LnEdH = QLabel(self)
        self.LnEdH.move(140, 132)
        self.LnEdH.setFixedWidth(50)
        self.LnEdH.setFixedHeight(15)

        self.ans_labl = QtWidgets.QLabel(self)
        self.ans_labl.setText("")
        self.ans_labl.move(555,55)

        self.mainAct = QtWidgets.QLabel(self)
        self.mainAct.setText("Написать программу, которая выводит"
                             " таблицу значений функции f(x) в диапазоне от "
                             "a до b, с шагом h.")
        self.mainAct.move(40, 20)
        self.mainAct.adjustSize()

        self.mainActInf = QtWidgets.QLabel(self)
        self.mainActInf.setText("Функция: ln(x) \nПараметр a: \n\nПараметр b: \n\nШаг h:")
        self.mainActInf.move(40, 50)
        self.mainActInf.adjustSize()

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(350, 250)
        self.btn.setText("Start")
        self.btn.setFixedWidth(100)
        self.btn.clicked.connect(self.makemath)

    def makemath(self):
        self.ans_labl.setText("")
        x, b_ok = QInputDialog.getText(self,'X','Введите значение x: ')
        y, b_ok = QInputDialog.getText(self, 'Y', 'Введите значение y: ')
        z, b_ok = QInputDialog.getText(self, 'Z', 'Введите значение z: ')
        x,y,z = int(x)*10,int(y)*10+1,int(float(z)*10)
        for i in range(x, y, z):
            if i != 0:
                a = math.log(i / 10)
                self.ans_labl.setText(self.ans_labl.text()+"f("+str(i/10)+") = "+str(a)+"\n")
            else:
                self.ans_labl.setText(self.ans_labl.text() + "f(" + str(i / 10) + ") = неопределено\n")
        self.LnEdA.setText(str(x/10))
        self.LnEdB.setText(str((y-1)/10))
        self.LnEdH.setText(str(z/10))
        self.ans_labl.adjustSize()