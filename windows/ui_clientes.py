# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clientesSiauWN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.15
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from datetime import date

import db
import ui_clienteAgregar
import ui_clienteBorrar
import ui_clienteModificar
import ui_clienteVentas

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1080, 720)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(820, 30, 231, 121))
        font = QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setPixmap(QPixmap(u"img\\s.png"))
        self.label_3.setScaledContents(True)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(170, 60, 471, 61))
        font1 = QFont()
        font1.setPointSize(20)
        self.lineEdit_2.setFont(font1)
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 9):
            self.tableWidget.setColumnCount(9)
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
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(30, 170, 1021, 521))
        font2 = QFont()
        font2.setFamily(u"MS Shell Dlg 2")
        font2.setPointSize(16)
        self.tableWidget.setFont(font2)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(169)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(650, 60, 151, 61))
        font3 = QFont()
        font3.setPointSize(12)
        self.pushButton_7.setFont(font3)
        self.pushButton_7.clicked.connect(self.addClient)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 60, 141, 61))
        font4 = QFont()
        font4.setPointSize(22)
        self.label.setFont(font4)
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
                self.cursor.execute(f"SELECT * FROM cliente WHERE nombre LIKE \'%{self.lineEdit_2.text()}%\';")
            else:
                self.cursor.execute(f"SELECT * FROM cliente;")
            clients = self.cursor.fetchall()
            if column == 0:
                self.deleteClient(clients[row][0])
            elif column == 1:
                self.modifyClient(clients[row][0])
            elif column == 2:
                self.clientReport(clients[row][0])
            elif column == 3:
                self.goToClientSales(clients[row][0])
        
    def deleteClient(self,client_id):
        self.clienteBorrar = ui_clienteBorrar.clienteBorrar(client_id)
        self.clienteBorrar.show()
    
    def modifyClient(self,client_id):
        self.clienteModificar = ui_clienteModificar.clienteModificar(client_id)
        self.clienteModificar.show()

    def clientReport(self,client_id):
        with open("Reporte\\Reporte.txt", "w") as f:
            f.write(f"Fecha: {date.today()}")
            f.write("\nCliente: ")
            f.write("\nid_cliente, direccion, nombre, telefono, email")
            self.cursor.execute(f"SELECT * FROM cliente WHERE id_cliente = {client_id}")
            f.write("\n"+str(self.cursor.fetchone()))
            f.write("\n\nVentas: ")
            f.write("\nid_venta, fecha de venta, total, metodo de pago, cliente, empleado")
            self.cursor.execute(f"SELECT id_venta,fecha_venta,total,metodo_de_pago,cliente.nombre ,empleado.nombre FROM venta JOIN cliente ON venta.id_cliente = cliente.id_cliente JOIN empleado ON venta.id_empleado = empleado.id_empleado WHERE venta.id_cliente = {client_id};")
            sales = self.cursor.fetchall()         
            if len(sales) > 0:
                for i in range(len(sales)):
                    f.write("\n"+str(sales[i]))
                   

    def addClient(self):
        self.productoAgregar = ui_clienteAgregar.clienteAgregar()
        self.productoAgregar.show()
    
    def goToClientSales(self,client_id):
        self.productosVariacion = ui_clienteVentas.clienteVentas(client_id)
        self.productosVariacion.show()
        
    def setItems(self):
        if self.lineEdit_2.text() != "":
            self.cursor.execute(f"SELECT * FROM cliente WHERE nombre LIKE \'%{self.lineEdit_2.text()}%\';")
        else:
            self.cursor.execute(f"SELECT * FROM cliente;")
        clients = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(clients))
        if len(clients) > 0:
            self.tableWidget.setColumnCount(len(clients[0])+4)
            for i in range(len(clients)):

                self.tableWidget.setItem(i,0,QTableWidgetItem("🗑️"))
                self.tableWidget.setItem(i,1,QTableWidgetItem("✏️"))
                self.tableWidget.setItem(i,2,QTableWidgetItem("📊"))
                self.tableWidget.setItem(i,3,QTableWidgetItem("🔍"))

                for j in range(len(clients[i])):
                    self.tableWidget.setItem(i,j+4,QTableWidgetItem(str(clients[i][j])))
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
        ___qtablewidgetitem03 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem03.setText(QCoreApplication.translate("MainWindow", u"Reporte", None));
        ___qtablewidgetitem04 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem04.setText(QCoreApplication.translate("MainWindow", u"Detalle", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Telefono", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir cliente", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
    # retranslateUi

class clientes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)