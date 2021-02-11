# This Python file uses the following encoding: utf-8
import sys
import os

import PySide2

from form_ui import Ui_NotFigurator
from PySide2 import QtWidgets

import excel_reader as er
import pandas as pd

from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLayout, QComboBox
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

combobox_need = er.excelRead.parameters_counter()


class NotFigurator(QtWidgets.QWidget, Ui_NotFigurator):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.load_ui()
        # -----загрузка файла интерфейса .ui через
        vbox = QtWidgets.QVBoxLayout(self)

        self.combobox_need_class = combobox_need

        qbtn = QPushButton('Рассчитать', self)
        qbtn.clicked.connect(self.onBtnClick)
        self.itemlist = []
        self.btncounter0 = 0
        self.m1 = 0

        self.grid = QtWidgets.QVBoxLayout()
        self.itemlist = []
        vbox.addLayout(self.grid)
        vbox.addStretch(3)
        self.frame.setLayout(vbox)
        vbox.addWidget(qbtn)
        self.cgen()

    """
    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()
    """

    def cgen(self):
        for label, combobox in self.itemlist:
            label.deleteLater()
            combobox.deleteLater()
        self.itemlist = []
        for i in range(combobox_need):
            label = QtWidgets.QLabel('Параметр{}'.format(i + 1))
            combobox = QtWidgets.QComboBox()
            self.grid.addWidget(label, i)
            self.grid.addWidget(combobox, i)
            self.itemlist.append([label, combobox])

        mainDf = er.ReadEx.lltrsDf
        global_itemslist = []
        list1 = []

        for current_cell in range(len(mainDf)):
            cell_value = mainDf.iloc[current_cell, 0]
            if cell_value != 'X':
                itemslist = global_itemslist
                itemslist.append(mainDf.iloc[current_cell, 2])

            else:
                list1.append(global_itemslist)
                itemslist = []
                global_itemslist = []
        print("Исходный:", list1)

        current_combobox_list = list1

        for m in range(combobox_need):
            llt_labelsnamelist = ['Вид:', 'Тип:', 'Присоединение к процессу:', 'Форма уплотнительной поверхности', 'Материал штока', 'Диаметр штока', 'Погрешность измерения', 'Температурное исполнение', 'Корпус', 'Кабельный ввод', 'Первичный преобразователь', 'Поплавок', 'Балансировка поплавка на раздел сред', 'Футеровка поплавка', 'Взрывозащита', 'Дополнительно', 'Первичная государственная поверка']
            nameslist = current_combobox_list[m]
            try:
                self.itemlist[m][1].addItems(nameslist)
                self.itemlist[m][0].setText(str(m) + '. ' + str(llt_labelsnamelist[m]))
            except:
                print(Exception)
            print("Завершение программы заполнения", m, "комбобокса")

    def onBtnClick(self):
        def codeFilling():
            pass
        codeFilling()

        def descriptionFilling():
            pass
        descriptionFilling()

        def priceFilling():
            pass
        priceFilling()


if __name__ == "__main__":
    app = QApplication([])
    widget = NotFigurator()
    # widget.verticalLayout.addWidget(widget.qbtn)
    widget.show()
    sys.exit(app.exec_())
