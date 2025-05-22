# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'productoVariacionAgregarxTXMcN.ui'
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
    def setupUi(self, MainWindow,product_id):

        self.product_id = product_id

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(511, 350)
        self.mainWindow = MainWindow
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 260, 451, 71))
        self.pushButton.clicked.connect(self.add)
        font = QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 200, 220, 41))
        font1 = QFont()
        font1.setPointSize(18)
        self.label_3.setFont(font1)
        self.label_3.setFrameShape(QFrame.Box)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 20, 220, 41))
        self.label_5.setFont(font1)
        self.label_5.setFrameShape(QFrame.Box)
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 80, 220, 41))
        self.label_6.setFont(font1)
        self.label_6.setFrameShape(QFrame.Box)
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(270, 80, 211, 41))
        self.lineEdit_3.setFont(font1)
        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(270, 200, 211, 41))
        self.spinBox.setFont(font1)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 140, 220, 41))
        self.label_7.setFont(font1)
        self.label_7.setFrameShape(QFrame.Box)
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(270, 140, 211, 41))
        self.lineEdit_5.setFont(font1)
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(270, 20, 211, 41))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.connection = db.connect()
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"SELECT * FROM producto WHERE id_producto = {self.product_id};")
        products = self.cursor.fetchall()
        for i in range(len(products)):
            self.comboBox.addItem(products[i][1])

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar variaci\u00f3n", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Stock", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Producto", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Talla", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Color", None))
    # retranslateUi
    
    def add(self):
        self.cursor.execute(f"SELECT * FROM producto WHERE nombre = \'{self.comboBox.currentText()}\'")
        product_id = self.cursor.fetchall()
        self.cursor.execute(f"INSERT INTO variacion_producto (talla,color,cantidad_stock,id_producto) VALUES (\'{self.lineEdit_3.text()}\', \'{self.lineEdit_5.text()}\', {self.spinBox.value()},{product_id[0][0]});")
        self.mainWindow.close()
    
    def closeEvent(self,event):
        self.connection.close()
        self.cursor.close()
        event.accept()

class productoVariacionAgregar(QMainWindow):
    def __init__(self,product_id):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self,product_id)