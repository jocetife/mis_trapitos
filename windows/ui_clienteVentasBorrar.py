# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clienteVentasBorrarNphBVt.ui'
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
        MainWindow.resize(710, 396)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(850, 30, 191, 111))
        font = QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setPixmap(QPixmap(u":/prefijoNuevo/s.png"))
        self.label_3.setScaledContents(True)
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(80, 240, 221, 91))
        self.pushButton_5.setFont(font)
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(410, 240, 221, 91))
        self.pushButton_6.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 30, 631, 151))
        font1 = QFont()
        font1.setPointSize(22)
        self.label_2.setFont(font1)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText("")
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Borrar", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u00bfEstas seguro de que deseas\n"
"borrar la venta?", None))
    # retranslateUi

class clienteVentasBorrar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)