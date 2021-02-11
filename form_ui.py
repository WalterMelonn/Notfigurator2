# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_NotFigurator(object):
    def setupUi(self, NotFigurator):
        if not NotFigurator.objectName():
            NotFigurator.setObjectName(u"NotFigurator")
        NotFigurator.resize(1099, 1098)
        NotFigurator.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(NotFigurator)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(NotFigurator)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(0, 0))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_10 = QVBoxLayout(self.tab)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout = QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName(u"formLayout")
        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_10)

        self.lineEdit_2 = QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_2)

        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_11)

        self.lineEdit_3 = QLineEdit(self.groupBox_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_3)

        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_12)

        self.lineEdit_4 = QLineEdit(self.groupBox_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_4)


        self.horizontalLayout_4.addWidget(self.groupBox_2)

        self.groupBox_10 = QGroupBox(self.tab)
        self.groupBox_10.setObjectName(u"groupBox_10")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_10.sizePolicy().hasHeightForWidth())
        self.groupBox_10.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_6 = QPushButton(self.groupBox_10)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_2.addWidget(self.pushButton_6)


        self.horizontalLayout_4.addWidget(self.groupBox_10)


        self.verticalLayout_8.addLayout(self.horizontalLayout_4)

        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lineEdit = QLineEdit(self.groupBox_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_7.addWidget(self.lineEdit)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_2 = QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setFlat(False)

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.groupBox_3)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_3.addWidget(self.pushButton)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)


        self.verticalLayout_8.addWidget(self.groupBox_3)


        self.horizontalLayout_5.addLayout(self.verticalLayout_8)

        self.groupBox_7 = QGroupBox(self.tab)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy1)
        self.groupBox_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout_2 = QFormLayout(self.groupBox_7)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_13 = QLabel(self.groupBox_7)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_13)

        self.lineEdit_5 = QLineEdit(self.groupBox_7)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit_5)

        self.label_14 = QLabel(self.groupBox_7)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_14)

        self.lineEdit_6 = QLineEdit(self.groupBox_7)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lineEdit_6)

        self.label_15 = QLabel(self.groupBox_7)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_15)

        self.lineEdit_7 = QLineEdit(self.groupBox_7)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lineEdit_7)

        self.label_16 = QLabel(self.groupBox_7)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_16)

        self.lineEdit_8 = QLineEdit(self.groupBox_7)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.lineEdit_8)

        self.label_17 = QLabel(self.groupBox_7)
        self.label_17.setObjectName(u"label_17")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_17)

        self.lineEdit_9 = QLineEdit(self.groupBox_7)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.lineEdit_9)


        self.horizontalLayout_5.addWidget(self.groupBox_7)

        self.groupBox_8 = QGroupBox(self.tab)
        self.groupBox_8.setObjectName(u"groupBox_8")
        sizePolicy1.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy1)
        self.formLayout_3 = QFormLayout(self.groupBox_8)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_18 = QLabel(self.groupBox_8)
        self.label_18.setObjectName(u"label_18")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_18)

        self.lineEdit_14 = QLineEdit(self.groupBox_8)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.lineEdit_14)

        self.label_22 = QLabel(self.groupBox_8)
        self.label_22.setObjectName(u"label_22")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_22)

        self.lineEdit_10 = QLineEdit(self.groupBox_8)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.lineEdit_10)

        self.label_19 = QLabel(self.groupBox_8)
        self.label_19.setObjectName(u"label_19")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_19)

        self.lineEdit_13 = QLineEdit(self.groupBox_8)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.lineEdit_13)

        self.label_21 = QLabel(self.groupBox_8)
        self.label_21.setObjectName(u"label_21")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_21)

        self.lineEdit_11 = QLineEdit(self.groupBox_8)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.lineEdit_11)

        self.label_20 = QLabel(self.groupBox_8)
        self.label_20.setObjectName(u"label_20")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.label_20)

        self.lineEdit_12 = QLineEdit(self.groupBox_8)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.lineEdit_12)


        self.horizontalLayout_5.addWidget(self.groupBox_8)

        self.groupBox_9 = QGroupBox(self.tab)
        self.groupBox_9.setObjectName(u"groupBox_9")
        sizePolicy.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.textEdit = QTextEdit(self.groupBox_9)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.textEdit)


        self.horizontalLayout_5.addWidget(self.groupBox_9)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_10.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy3)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scrollArea = QScrollArea(self.groupBox)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 618, 818))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(600, 800))
        self.frame.setStyleSheet(u"background-color: rgb(210, 220, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.frame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)


        self.verticalLayout_9.addWidget(self.groupBox)

        self.groupBox_4 = QGroupBox(self.tab)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.pushButton_4 = QPushButton(self.groupBox_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(10, 20, 151, 23))
        self.pushButton_5 = QPushButton(self.groupBox_4)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(10, 50, 151, 23))

        self.verticalLayout_9.addWidget(self.groupBox_4)


        self.horizontalLayout_8.addLayout(self.verticalLayout_9)

        self.groupBox_5 = QGroupBox(self.tab)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalLayout = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.textEdit_2 = QTextEdit(self.groupBox_5)
        self.textEdit_2.setObjectName(u"textEdit_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy4)

        self.horizontalLayout.addWidget(self.textEdit_2)


        self.horizontalLayout_8.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.tab)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tableView = QTableView(self.groupBox_6)
        self.tableView.setObjectName(u"tableView")
        sizePolicy4.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy4)

        self.horizontalLayout_2.addWidget(self.tableView)


        self.horizontalLayout_8.addWidget(self.groupBox_6)


        self.verticalLayout_10.addLayout(self.horizontalLayout_8)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(NotFigurator)
        self.pushButton_2.clicked.connect(self.lineEdit.clear)

        self.tabWidget.setCurrentIndex(0)
        self.pushButton_2.setDefault(False)


        QMetaObject.connectSlotsByName(NotFigurator)
    # setupUi

    def retranslateUi(self, NotFigurator):
        NotFigurator.setWindowTitle(QCoreApplication.translate("NotFigurator", u"NotFigurator", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("NotFigurator", u"\u0422\u041a\u041f", None))
        self.label_10.setText(QCoreApplication.translate("NotFigurator", u"\u2116 \u0422\u041a\u041f", None))
        self.label_11.setText(QCoreApplication.translate("NotFigurator", u"\u2116 \u041f\u043e\u0437\u0438\u0446\u0438\u0438", None))
        self.label_12.setText(QCoreApplication.translate("NotFigurator", u"Tag-\u043d\u043e\u043c\u0435\u0440", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("NotFigurator", u"OEM", None))
        self.pushButton_6.setText(QCoreApplication.translate("NotFigurator", u"VEGA", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("NotFigurator", u"\u041a\u043e\u0434 \u0437\u0430\u043a\u0430\u0437\u0430", None))
        self.pushButton_2.setText(QCoreApplication.translate("NotFigurator", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.pushButton.setText(QCoreApplication.translate("NotFigurator", u"\u0421\u043a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("NotFigurator", u"\u0425\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438 \u0441\u0440\u0435\u0434\u044b", None))
        self.label_13.setText(QCoreApplication.translate("NotFigurator", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435:", None))
        self.label_14.setText(QCoreApplication.translate("NotFigurator", u"\u041f\u043b\u043e\u0442\u043d\u043e\u0441\u0442\u044c:", None))
        self.label_15.setText(QCoreApplication.translate("NotFigurator", u"\u0422. \u043e\u043a\u0440:", None))
        self.label_16.setText(QCoreApplication.translate("NotFigurator", u"\u0422. \u0441\u0440\u0435\u0434\u044b:", None))
        self.label_17.setText(QCoreApplication.translate("NotFigurator", u"\u0414\u0430\u0432\u043b\u0435\u043d\u0438\u0435:", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("NotFigurator", u"\u0424\u043b\u0430\u043d\u0446\u044b", None))
        self.label_18.setText(QCoreApplication.translate("NotFigurator", u"\u0421\u0442\u0430\u043d\u0434\u0430\u0440\u0442:", None))
        self.label_22.setText(QCoreApplication.translate("NotFigurator", u"DN:", None))
        self.label_19.setText(QCoreApplication.translate("NotFigurator", u"PN:", None))
        self.label_21.setText(QCoreApplication.translate("NotFigurator", u"\u0422\u0438\u043f:", None))
        self.label_20.setText(QCoreApplication.translate("NotFigurator", u"\u0423\u043f\u043b. \u043f\u043e\u0432:", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("NotFigurator", u"\u041f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u0435 \u0434\u043b\u044f \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0441\u0442\u0432\u0430", None))
        self.groupBox.setTitle(QCoreApplication.translate("NotFigurator", u"\u041a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u044f", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("NotFigurator", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u0435", None))
        self.pushButton_4.setText(QCoreApplication.translate("NotFigurator", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043f\u043e\u0437\u0438\u0446\u0438\u044e \u0432 \u0422\u041a\u041f", None))
        self.pushButton_5.setText(QCoreApplication.translate("NotFigurator", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0432 Excel", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("NotFigurator", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("NotFigurator", u"\u0426\u0435\u043d\u043e\u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("NotFigurator", u"\u041a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u044f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("NotFigurator", u"\u0426\u0435\u043d\u043e\u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u0435 (\u043f\u043e\u0434\u0440\u043e\u0431\u043d\u043e)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("NotFigurator", u"\u0427\u0435\u0440\u0442\u0435\u0436", None))
    # retranslateUi

