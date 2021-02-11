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

        self.grid = QtWidgets.QGridLayout()
        self.itemlist = []
        vbox.addLayout(self.grid)
        vbox.addStretch(3)
        self.groupBox.setLayout(vbox)
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
            self.grid.addWidget(label, i, 0)
            self.grid.addWidget(combobox, i, 1)
            self.itemlist.append([label, combobox])

        mainDf = er.ReadEx.lltrsDf
        list1 = []
        global_itemslist = []
        # combobox_need_func = self.combobox_need_class
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
            nameslist = current_combobox_list[m]
            try:
                self.itemlist[m][1].addItems(nameslist)
            except:
                print(Exception)
            print("Завершение программы заполнения", m, "комбобокса")

    def onBtnClick(self):
        pass


if __name__ == "__main__":
    app = QApplication([])
    widget = NotFigurator()
    # widget.verticalLayout.addWidget(widget.qbtn)
    widget.show()
    sys.exit(app.exec_())
