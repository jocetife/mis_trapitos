# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'categoriaAgregarlYeFWp.ui'
##
## Created by: Qt User Interface Compiler version 5.15.15
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import db

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
            self.mainWindow = MainWindow
        MainWindow.setEnabled(True)
        MainWindow.resize(511, 164)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 80, 451, 71))
        self.pushButton.clicked.connect(self.add)
        font = QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 20, 220, 51))
        font1 = QFont()
        font1.setPointSize(18)
        self.label_5.setFont(font1)
        self.label_5.setFrameShape(QFrame.Box)
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(270, 20, 211, 51))
        self.lineEdit_4.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def add(self):
        self.connection = db.connect()
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"INSERT INTO categoria (nombre_categoria) VALUES (\'{self.lineEdit_4.text()}\');")
        self.mainWindow.close()
    
    def closeEvent(self,event):
        self.connection.close()
        self.cursor.close()
        event.accept()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar categoria", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
    # retranslateUi

class categoriaAgregar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
