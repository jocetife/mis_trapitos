# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'proveedorProductoyPCTrT.ui'
##
## Created by: Qt User Interface Compiler version 5.15.15
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import db
import ui_proveedorProductoAgregar
import ui_proveedorProductoModificar
import ui_proveedorProductoBorrar
from datetime import date


class Ui_MainWindow(object):
    supplier_id = None
    def setupUi(self, MainWindow,supplier_id):
        self.supplier_id = supplier_id

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1080, 720)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
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
        self.lineEdit_2.setGeometry(QRect(30, 90, 511, 50))
        font1 = QFont()
        font1.setPointSize(20)
        self.lineEdit_2.setFont(font1)
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem01 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem01)
        __qtablewidgetitem02 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem02)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem3)
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
        self.tableWidget.horizontalHeader().setDefaultSectionSize(254)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        font3 = QFont()
        font3.setPointSize(22)
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(550, 90, 181, 51))
        self.pushButton_7.clicked.connect(self.assignRelationship)
        font4 = QFont()
        font4.setPointSize(11)
        self.pushButton_7.setFont(font4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

        self.setItems()

        self.tableWidget.setColumnWidth(0,50)
        self.tableWidget.setColumnWidth(1,50)

        self.tableWidget.cellClicked.connect(self.handleCell)
    # setupUi
        
    def handleCell(self,row,column):
        if column < 3:
            relationships = []
            if self.lineEdit_2.text() != "":
                self.cursor.execute(f"SELECT * FROM producto WHERE nombre LIKE \'%{self.lineEdit_2.text()}%\';")
                instances = self.cursor.fetchall()  
                for i in range(len(instances)):
                    self.cursor.execute(f"SELECT * FROM producto_proveedor WHERE id_producto = {instances[i][0]} AND id_proveedor = {self.supplier_id};")
                    relationships.append(self.cursor.fetchone())
            else:
                self.cursor.execute(f"SELECT * FROM producto_proveedor WHERE id_proveedor = {self.supplier_id};")
                relationships = self.cursor.fetchall()                   
            if column == 0:
                self.deleteRelationship(relationships[row][0])
            elif column == 1:
                self.modifyRelationship(relationships[row][0])

    def deleteRelationship(self,relationship):
        self.variacionBorrar = ui_proveedorProductoBorrar.proveedorProductoBorrar(relationship)
        self.variacionBorrar.show()
    
    def modifyRelationship(self,relationship):
        self.variacionModificar = ui_proveedorProductoModificar.proveedorProductoModificar(relationship,self.supplier_id)
        self.variacionModificar.show()
                   
    def assignRelationship(self):
        self.variacionAgregar = ui_proveedorProductoAgregar.proveedorProductoAgregar(self.supplier_id)
        self.variacionAgregar.show()
        
    def setItems(self):
        relationships = []
        if self.lineEdit_2.text() != "":
            self.cursor.execute(f"SELECT * FROM producto WHERE nombre LIKE \'%{self.lineEdit_2.text()}%\';")
            instances = self.cursor.fetchall()  
            for i in range(len(instances)):
                self.cursor.execute(f"SELECT producto_proveedor.id_pp, producto.nombre, producto_proveedor.id_proveedor FROM producto_proveedor JOIN producto ON producto.id_producto = producto_proveedor.id_producto WHERE producto_proveedor.id_producto = {instances[i][0]} AND producto_proveedor.id_proveedor = {self.supplier_id};")
                relationships.append(self.cursor.fetchone())
        else:
            self.cursor.execute(f"SELECT producto_proveedor.id_pp, producto.nombre, producto_proveedor.id_proveedor FROM producto_proveedor JOIN producto ON producto.id_producto = producto_proveedor.id_producto WHERE producto_proveedor.id_proveedor = {self.supplier_id};")
            relationships = self.cursor.fetchall()  
        if len(relationships) > 0:
            self.tableWidget.setRowCount(len(relationships))
            self.tableWidget.setColumnCount(len(relationships[0])+2)
            for i in range(len(relationships)):

                self.tableWidget.setItem(i,0,QTableWidgetItem("🗑️"))
                self.tableWidget.setItem(i,1,QTableWidgetItem("✏️"))

                for j in range(len(relationships[i])):
                    self.tableWidget.setItem(i,j+2,QTableWidgetItem(str(relationships[i][j])))
        QTimer.singleShot(3000, self.setItems)

    def closeEvent(self,event):
        self.connection.close()
        self.cursor.close()
        event.accept()    

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText("")
        self.lineEdit_2.setText("")
        ___qtablewidgetitem01 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem01.setText(QCoreApplication.translate("MainWindow", u"Borrar", None));
        ___qtablewidgetitem02 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem02.setText(QCoreApplication.translate("MainWindow", u"Modificar", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Proveedor", None));

        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Asignar proveedor\n"
"a producto", None))

    # retranslateUi

class proveedorProducto(QMainWindow):
    def __init__(self,supplier_id):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self,supplier_id)