# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'productoModificaraEfRXn.ui'
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

    product_id = None

    def setupUi(self, MainWindow,product_id):
        self.product_id = product_id
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(511, 752)
        self.mainWindow = MainWindow
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 270, 220, 41))
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setFrameShape(QFrame.Box)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 330, 220, 91))
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QFrame.Box)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 660, 451, 71))
        self.pushButton.clicked.connect(self.modify)
        font1 = QFont()
        font1.setPointSize(16)
        self.pushButton.setFont(font1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 140, 220, 41))
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QFrame.Box)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 200, 220, 51))
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QFrame.Box)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 20, 220, 41))
        self.label_5.setFont(font)
        self.label_5.setFrameShape(QFrame.Box)
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 80, 220, 41))
        self.label_6.setFont(font)
        self.label_6.setFrameShape(QFrame.Box)
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 440, 220, 91))
        self.label_7.setFont(font)
        self.label_7.setFrameShape(QFrame.Box)
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 550, 220, 91))
        self.label_8.setFont(font)
        self.label_8.setFrameShape(QFrame.Box)
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.doubleSpinBox = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setGeometry(QRect(270, 140, 210, 41))
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setMaximum(10000.000000000000000)
        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(270, 330, 210, 91))
        self.spinBox.setFont(font)
        self.spinBox.setMaximum(100)
        self.dateEdit = QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(270, 440, 210, 91))
        self.dateEdit.setFont(font)
        self.dateEdit_2 = QDateEdit(self.centralwidget)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setGeometry(QRect(270, 550, 210, 91))
        self.dateEdit_2.setFont(font)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(270, 270, 211, 41))
        self.lineEdit_2.setFont(font)
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(270, 200, 211, 51))
        self.comboBox.setFont(font)
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(270, 80, 211, 41))
        self.lineEdit_3.setFont(font)
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(270, 20, 211, 41))
        self.lineEdit_4.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.connection = db.connect()
        
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"SELECT id_producto, nombre,descripcion,precio,oferta,porc_desc,categoria.nombre_categoria,fecha_ini_oferta,fecha_fin_oferta  FROM producto join categoria on producto.id_categoria = categoria.id_categoria WHERE id_producto = {self.product_id};")
        product = self.cursor.fetchall()
        self.lineEdit_4.setText(product[0][1])
        self.lineEdit_3.setText(product[0][2])
        self.doubleSpinBox.setValue(float(product[0][3]))
        self.cursor.execute("SELECT * FROM categoria;")
        categories = self.cursor.fetchall()
        for i in range(len(categories)):
            self.comboBox.addItem(categories[i][1])
        self.comboBox.setCurrentText(product[0][6])
        self.lineEdit_2.setText(product[0][4])
        self.spinBox.setValue(int(product[0][5]))
        if self.lineEdit_2.text() == "" and self.spinBox.value() == 0:
            self.dateEdit.setEnabled(False)
            self.dateEdit_2.setEnabled(False)
        else:
            self.dateEdit.setDate(QDate(int(str(product[0][7])[0:4]),int(str(product[0][7])[5:7]),int(str(product[0][7])[8:10])))
            self.dateEdit_2.setDate(QDate(int(str(product[0][8])[0:4]),int(str(product[0][8])[5:7]),int(str(product[0][8])[8:10])))
        self.lineEdit_2.textChanged.connect(self.isEmpty)
        self.spinBox.valueChanged.connect(self.isEmpty)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
        
    def modify(self):
        self.cursor.execute(f"SELECT * FROM categoria WHERE nombre_categoria = \'{self.comboBox.currentText()}\'")
        category_id = self.cursor.fetchall()
        if self.lineEdit_2.text() == "" or self.spinBox.value() == 0:
            self.cursor.execute(f"UPDATE producto SET nombre = \'{self.lineEdit_4.text()}\',descripcion = \'{self.lineEdit_3.text()}\',precio = {self.doubleSpinBox.value()},oferta = \'{self.lineEdit_2.text()}\', porc_desc = {self.spinBox.value()},id_categoria = {category_id[0][0]},fecha_ini_oferta = NULL,fecha_fin_oferta = NULL WHERE id_producto = {self.product_id};")
        else:
            self.cursor.execute(f"UPDATE producto SET nombre = \'{self.lineEdit_4.text()}\',descripcion = \'{self.lineEdit_3.text()}\',precio = {self.doubleSpinBox.value()},oferta = \'{self.lineEdit_2.text()}\', porc_desc = {self.spinBox.value()},id_categoria = {category_id[0][0]},fecha_ini_oferta = \'{str(self.dateEdit.date())}\',fecha_fin_oferta = \'{str(self.dateEdit_2.date())}\' WHERE id_producto = {self.product_id};")
        self.mainWindow.close()

    def isEmpty(self):
        if self.lineEdit_2.text() == "" and self.spinBox.value() == 0:
            self.dateEdit.setEnabled(False)
            self.dateEdit_2.setEnabled(False)
        else:
            self.dateEdit.setEnabled(True)
            self.dateEdit_2.setEnabled(True)

    def closeEvent(self,event):
        self.connection.close()
        self.cursor.close()
        event.accept()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Oferta", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Porcentaje de\n"
"descuento", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Modificar producto", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Precio", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Categor\u00eda", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Fecha de inicio\n"
"de la oferta", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Fecha de inicio\n"
"de la oferta", None))
    # retranslateUi

class productoModificar(QMainWindow):
    def __init__(self,product_id):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self,product_id)