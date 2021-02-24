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
        last_cell_number = 0

        for current_cell in range(len(mainDf)):
            cell_value = mainDf.iloc[current_cell, 0]
            if cell_value != 'X':
                itemslist = global_itemslist
                itemslist.append(mainDf.iloc[current_cell, 2])
                last_cell_number = current_cell
                print(last_cell_number, len(mainDf))
                if last_cell_number == ((len(mainDf))-1):
                    try:
                        print("Entered to the elif")
                        list1.append(global_itemslist)
                    except:
                        print("Exception list out of range")
            else:
                list1.append(global_itemslist)
                global_itemslist = []
                # для ввода первых не выбранных элементов сюда добавить в скобки кавычки
        print("Исходный:", list1)

        cells_left = len(mainDf) - last_cell_number
        """
        try:
            for k in range(cells_left):
                # cell_value = mainDf.iloc[current_cell, 0]
        except:
            print(Exception)
        print("Завершение программы заполнения последнего", "комбобокса")
        """
        current_combobox_list = list1

        for m in range(combobox_need):
            llt_labelsnamelist = ['Вид:', 'Тип:', 'Присоединение к процессу:', 'Форма уплотнительной поверхности', 'Материал штока', 'Диаметр штока', 'Погрешность измерения', 'Температурное исполнение', 'Корпус', 'Кабельный ввод',
                                  'Первичный преобразователь', 'Поплавок', 'Балансировка поплавка на раздел сред', 'Футеровка поплавка', 'Взрывозащита', 'Дополнительно', 'Первичная государственная поверка']
            try:
                nameslist = current_combobox_list[m]
                self.itemlist[m][1].addItems(nameslist)
                self.itemlist[m][0].setText(str(m+1) + '. ' + str(llt_labelsnamelist[m]))
            except:
                print(Exception)
            print("Завершение программы заполнения", m+1, "комбобокса")

    def onBtnClick(self):
        def codeFilling():
            code_of_order_out = ""
            current_combobox = 0
            code_order_final = ""
            current_row = 0
            cdf = er.ReadEx.lltrsDf
            try:
                while current_combobox != combobox_need:
                    code_order_in_cbox = self.itemlist[current_combobox][1].currentText()
                    current_row = str(cdf.loc[cdf['Name'] == code_order_in_cbox])
                    print(current_row)
                    # current cell = find needed column in current row

                    code_order_final += current_row
                    current_combobox += 1
            except:
                print(Exception)
            self.lineEdit.setText(code_order_final)
            print("Завершение записи кода заказа", "")
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
