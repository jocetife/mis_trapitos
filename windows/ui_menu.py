# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menunBxDwP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.15
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1080, 720)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 60, 401, 31))
        font = QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(400, 430, 291, 251))
        font1 = QFont()
        font1.setPointSize(16)
        self.pushButton.setFont(font1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(860, 20, 201, 121))
        self.label_3.setFont(font)
        self.label_3.setPixmap(QPixmap(u":/prefijoNuevo/s.png"))
        self.label_3.setScaledContents(True)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(700, 160, 291, 251))
        self.pushButton_2.setFont(font1)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(400, 160, 291, 251))
        self.pushButton_3.setFont(font1)
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(100, 430, 291, 251))
        self.pushButton_5.setFont(font1)
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(100, 160, 291, 251))
        self.pushButton_6.setFont(font1)
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(700, 430, 291, 251))
        self.pushButton_4.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Bienvenido: ", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Generar\n"
"informe", None))
        self.label_3.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Ventas", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Gestionar\n"
"clientes", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Gestionar\n"
"proveedores", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Gestionar\n"
"productos", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Salir de\n"
"la aplicaci\u00f3n", None))
    # retranslateUi

class menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)