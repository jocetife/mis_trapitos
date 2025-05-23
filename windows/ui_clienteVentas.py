# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clienteVentascwXHXW.ui'
##
## Created by: Qt User Interface Compiler version 5.15.15
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import db
import ui_clienteVentasBorrar
import ui_clienteVentasDetalle

class Ui_MainWindow(object):
    def setupUi(self, MainWindow,client_id):
        self.client_id = client_id

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1080, 720)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 90, 141, 51))
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
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem0 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem0)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(30, 210, 1021, 481))
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(16)
        self.tableWidget.setFont(font1)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(145)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        font2 = QFont()
        font2.setPointSize(22)
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(160, 90, 571, 51))
        self.comboBox.setFont(font)
        self.comboBox.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.connection = db.connect()
        self.cursor = self.connection.cursor()


        self.setItems()

        self.tableWidget.setColumnWidth(0,50)
        self.tableWidget.setColumnWidth(1,50)
        self.tableWidget.setColumnWidth(2,50)

        self.tableWidget.cellClicked.connect(self.handleCell)
    # setupUi
        
    def handleCell(self,row,column):
        if column < 2:
            if self.comboBox.currentText() == "Fecha (descendente)":
                self.cursor.execute(f"SELECT * FROM venta WHERE id_cliente = {self.client_id} ORDER BY fecha_venta DESC;")
            elif self.comboBox.currentText() == "Fecha (ascendente)":
                self.cursor.execute(f"SELECT * FROM venta WHERE id_cliente = {self.client_id} ORDER BY fecha_venta ASC;")
            elif self.comboBox.currentText() == "Total (descendente)":
                self.cursor.execute(f"SELECT * FROM venta WHERE id_cliente = {self.client_id} ORDER BY total DESC;")
            else:
                self.cursor.execute(f"SELECT * FROM venta WHERE id_cliente = {self.client_id} ORDER BY total ASC;")
            sale = self.cursor.fetchall()
            if column == 0:
                self.deleteSale(sale[row][0])
            if column == 1:
                self.GoToSaleDetails(sale[row][0])

    def deleteSale(self,sale_id):
        self.clienteVentaBorrar = ui_clienteVentasBorrar.clienteVentasBorrar(sale_id)
        self.clienteVentaBorrar.show()
    
    def GoToSaleDetails(self,sale_id):
        self.clienteVentasDetalle = ui_clienteVentasDetalle.clienteVentasDetalle(sale_id)
        self.clienteVentasDetalle.show()

        
    def setItems(self):
        if self.comboBox.currentText() == "Fecha (descendente)":
            self.cursor.execute(f"SELECT * FROM venta WHERE id_cliente = {self.client_id} ORDER BY fecha_venta DESC;")
        elif self.comboBox.currentText() == "Fecha (ascendente)":
            self.cursor.execute(f"SELECT * FROM venta WHERE id_cliente = {self.client_id} ORDER BY fecha_venta ASC;")
        elif self.comboBox.currentText() == "Total (descendente)":
            self.cursor.execute(f"SELECT * FROM venta WHERE id_cliente = {self.client_id} ORDER BY total DESC;")
        else:
            self.cursor.execute(f"SELECT * FROM venta WHERE id_cliente = {self.client_id} ORDER BY total ASC;")
        sales = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(sales))
        if len(sales) > 0:
            self.tableWidget.setColumnCount(len(sales[0])+2)
            for i in range(len(sales)):

                self.tableWidget.setItem(i,0,QTableWidgetItem("🗑️"))
                self.tableWidget.setItem(i,1,QTableWidgetItem("🔍"))

                for j in range(len(sales[i])):
                    self.tableWidget.setItem(i,j+2,QTableWidgetItem(str(sales[i][j])))
        QTimer.singleShot(3000, self.setItems)

    def closeEvent(self,event):
        self.connection.close()
        self.cursor.close()
        event.accept()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Ordenar", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Borrar", None));
        ___qtablewidgetitem0 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem0.setText(QCoreApplication.translate("MainWindow", u"Detalle", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Total", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Metodo", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Empleado", None));
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Fecha (descendente)", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Fecha (ascendente)", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Total (descendente)", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Total (ascendente)", None))

    # retranslateUi

class clienteVentas(QMainWindow):
    def __init__(self,client_id):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self,client_id)