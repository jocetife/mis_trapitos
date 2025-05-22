# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'productosqUSUWI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.15
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from datetime import date

import ui_productoAgregar
import ui_productoBorrar
import ui_productoModificar
import ui_productosVariacion
import db

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1080, 720)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 90, 41, 51))
        font = QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(750, 40, 291, 151))
        font = QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setPixmap(QPixmap(u"img\\s.png"))
        self.label_3.setScaledContents(True)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(80, 90, 461, 50))
        font1 = QFont()
        font1.setPointSize(20)
        self.lineEdit_2.setFont(font1)
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 13):
            self.tableWidget.setColumnCount(13)
        __qtablewidgetitem01 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem01)
        __qtablewidgetitem02 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem02)
        __qtablewidgetitem03 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem03)
        __qtablewidgetitem04 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem04)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, __qtablewidgetitem9)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(30, 210, 1021, 481))
        font2 = QFont()
        font2.setFamily(u"MS Shell Dlg 2")
        font2.setPointSize(16)
        self.tableWidget.setFont(font2)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        font3 = QFont()
        font3.setPointSize(22)
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(550, 90, 181, 51))
        font4 = QFont()
        font4.setPointSize(12)
        self.pushButton_7.setFont(font4)
        self.pushButton_7.clicked.connect(self.addItem)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

        self.setItems()

        self.tableWidget.setColumnWidth(0,50)
        self.tableWidget.setColumnWidth(1,50)
        self.tableWidget.setColumnWidth(2,50)
        self.tableWidget.setColumnWidth(3,50)
        self.tableWidget.setColumnWidth(4,50)

        self.tableWidget.cellClicked.connect(self.handleCell)


    # setupUi
        
    def handleCell(self,row,column):
        if column < 4:
            if self.lineEdit_2.text() != "":
                self.cursor.execute(f"SELECT id_producto, nombre,descripcion,precio,oferta,porc_desc,categoria.nombre_categoria,fecha_ini_oferta,fecha_fin_oferta  FROM producto join categoria on producto.id_categoria = categoria.id_categoria WHERE producto.nombre LIKE \'%{self.lineEdit_2.text()}%\';")
            else:
                self.cursor.execute(f"SELECT id_producto, nombre,descripcion,precio,oferta,porc_desc,categoria.nombre_categoria,fecha_ini_oferta,fecha_fin_oferta  FROM producto join categoria on producto.id_categoria = categoria.id_categoria;")
            products = self.cursor.fetchall()
            if column == 0:
                self.deleteItem(products[row][0])
            elif column == 1:
                self.modifyItem(products[row][0])
            elif column == 2:
                self.itemReport(products[row][0])
            elif column == 3:
                self.goToProductosVariacion(products[row][0])
        
    def deleteItem(self,product_id):
        self.productoBorrar = ui_productoBorrar.productoBorrar(product_id)
        self.productoBorrar.show()
    
    def modifyItem(self,product_id):
        self.productoModificar = ui_productoModificar.productoModificar(product_id)
        self.productoModificar.show()

    def itemReport(self,product_id):
        with open("Reporte\\Reporte.txt", "w") as f:
            f.write(f"Fecha: {date.today()}")
            f.write("\nProducto: ")
            f.write("\nid_producto, nombre, descripcion, precio, oferta, porc_desc, categoria, inicio de oferta, fin de oferta")
            self.cursor.execute(f"SELECT id_producto, nombre,descripcion,precio,oferta,porc_desc,categoria.nombre_categoria,fecha_ini_oferta,fecha_fin_oferta  FROM producto join categoria on producto.id_categoria = categoria.id_categoria WHERE id_producto = {product_id}")
            f.write("\n"+str(self.cursor.fetchone()))
            f.write("\n\nVariaciones: ")
            f.write("\nid_variacion, talla, color, cantidad_stock, id_producto")
            self.cursor.execute(f"SELECT * FROM variacion_producto WHERE variacion_producto.id_producto = {product_id}")
            variations = self.cursor.fetchall()
            if len(variations) > 0:
                for i in range(len(variations)):
                    f.write("\n"+str(variations[i]))
            f.write("\n\nProveedores: ")
            self.cursor.execute(f"SELECT id_producto, proveedor.nombre, proveedor.telefono, proveedor.email FROM producto_proveedor JOIN proveedor ON producto_proveedor.id_proveedor = proveedor.id_proveedor WHERE producto_proveedor.id_producto = {product_id};")
            f.write("id_producto, nombre, telefono, email")
            suppliers = self.cursor.fetchall()
            if len(suppliers) > 0:
                for i in range(len(suppliers)):
                    f.write("\n"+str(suppliers[i]))
                   

    def addItem(self):
        self.productoAgregar = ui_productoAgregar.productoAgregar()
        self.productoAgregar.show()
    
    def goToProductosVariacion(self,product_id):
        self.productosVariacion = ui_productosVariacion.productosVariacion(product_id)
        self.productosVariacion.show()
        
    def setItems(self):
        if self.lineEdit_2.text() != "":
            self.cursor.execute(f"SELECT id_producto, nombre,descripcion,precio,oferta,porc_desc,categoria.nombre_categoria,fecha_ini_oferta,fecha_fin_oferta  FROM producto join categoria on producto.id_categoria = categoria.id_categoria WHERE producto.nombre LIKE \'%{self.lineEdit_2.text()}%\';")
        else:
            self.cursor.execute(f"SELECT id_producto, nombre,descripcion,precio,oferta,porc_desc,categoria.nombre_categoria,fecha_ini_oferta,fecha_fin_oferta  FROM producto join categoria on producto.id_categoria = categoria.id_categoria;")
        products = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(products))
        self.tableWidget.setColumnCount(len(products[0])+4)
        for i in range(len(products)):

            self.tableWidget.setItem(i,0,QTableWidgetItem("🗑️"))
            self.tableWidget.setItem(i,1,QTableWidgetItem("✏️"))
            self.tableWidget.setItem(i,2,QTableWidgetItem("📊"))
            self.tableWidget.setItem(i,3,QTableWidgetItem("🔍"))

            for j in range(len(products[i])):
                self.tableWidget.setItem(i,j+4,QTableWidgetItem(str(products[i][j])))
        QTimer.singleShot(3000, self.setItems)

    def closeEvent(self,event):
        self.connection.close()
        self.cursor.close()
        event.accept()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText("")
        self.label_2.setText("🔍")
        self.lineEdit_2.setText("")
        ___qtablewidgetitem01 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem01.setText(QCoreApplication.translate("MainWindow", u"Borrar", None));
        ___qtablewidgetitem02 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem02.setText(QCoreApplication.translate("MainWindow", u"Modificar", None));
        ___qtablewidgetitem03 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem03.setText(QCoreApplication.translate("MainWindow", u"Reporte", None));
        ___qtablewidgetitem04 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem04.setText(QCoreApplication.translate("MainWindow", u"Detalle", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Precio", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Oferta", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Descuento", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Categor\u00eda", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Ini_oferta", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(12)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Fin_oferta", None));
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Agregar producto", None))

    # retranslateUi

class productos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)