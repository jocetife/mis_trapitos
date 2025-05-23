# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'proveedorAgregarmhXCQc.ui'
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
        MainWindow.setEnabled(True)
        MainWindow.resize(511, 293)
        self.mainWindow = MainWindow
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 210, 451, 71))
        self.pushButton.clicked.connect(self.add)
        font = QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 80, 220, 51))
        font1 = QFont()
        font1.setPointSize(18)
        self.label_3.setFont(font1)
        self.label_3.setFrameShape(QFrame.Box)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 140, 220, 51))
        self.label_4.setFont(font1)
        self.label_4.setFrameShape(QFrame.Box)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 20, 220, 51))
        self.label_5.setFont(font1)
        self.label_5.setFrameShape(QFrame.Box)
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(270, 20, 211, 51))
        self.lineEdit_4.setFont(font1)
        self.lineEdit_6 = QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(270, 140, 211, 51))
        self.lineEdit_6.setFont(font1)
        self.lineEdit_7 = QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(270, 80, 211, 51))
        self.lineEdit_7.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar proveedor", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
    # retranslateUi
        
    def add(self):
        self.connection = db.connect()
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"INSERT INTO proveedor (nombre,telefono,email) VALUES (\'{self.lineEdit_4.text()}\', \'{self.lineEdit_6.text()}\',\'{self.lineEdit_7.text()}\');")
        self.mainWindow.close()
    
    def closeEvent(self,event):
        self.connection.close()
        self.cursor.close()
        event.accept()

class proveedorAgregar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)