# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'proveedorProductoAgregarncHxbp.ui'
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
    def setupUi(self, MainWindow, supplier_id):

        self.supplier_id = supplier_id

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(511, 226)
        self.mainWindow = MainWindow
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 140, 451, 71))
        self.pushButton.clicked.connect(self.add)
        font = QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 20, 220, 41))
        font1 = QFont()
        font1.setPointSize(18)
        self.label_5.setFont(font1)
        self.label_5.setFrameShape(QFrame.Box)
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 80, 220, 41))
        self.label_6.setFont(font1)
        self.label_6.setFrameShape(QFrame.Box)
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(270, 20, 211, 41))
        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(270, 80, 211, 41))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.connection = db.connect()
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"SELECT * FROM producto;")
        products = self.cursor.fetchall()
        for i in range(len(products)):
            self.comboBox.addItem(products[i][1])
        self.cursor.execute(f"SELECT * FROM proveedor WHERE id_proveedor = {self.supplier_id}")
        proveedor = self.cursor.fetchall()
        self.comboBox_2.addItem(proveedor[0][1])


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Asignar", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Producto", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Proveedor", None))
    # retranslateUi
        
    def add(self):
        self.cursor.execute(f"SELECT * FROM producto WHERE nombre = \'{self.comboBox.currentText()}\'")
        product_id = self.cursor.fetchall()
        self.cursor.execute(f"INSERT INTO producto_proveedor (id_producto,id_proveedor) VALUES ({product_id[0][0]},{self.supplier_id});")
        self.mainWindow.close()
    
    def closeEvent(self,event):
        self.connection.close()
        self.cursor.close()
        event.accept()

class proveedorProductoAgregar(QMainWindow):
    def __init__(self,supplier_id):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self,supplier_id)