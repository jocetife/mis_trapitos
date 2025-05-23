# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clienteVentasDetallewclrBC.ui'
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

    sale_id = None
    def setupUi(self, MainWindow, sale_id):
        self.sale_id = sale_id
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
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
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
        self.tableWidget.horizontalHeader().setMinimumSectionSize(203)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(203)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 90, 151, 51))
        font2 = QFont()
        font2.setPointSize(22)
        self.label_4.setFont(font2)
        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(190, 90, 551, 51))
        self.comboBox_2.setFont(font)
        self.comboBox_2.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

        self.setItems()

        self.tableWidget.setColumnWidth(0,50)
    # setupUi
        
    def setItems(self):
        if self.comboBox_2.currentText() == "Cantidad (descendente)":
            self.cursor.execute(f"SELECT * FROM detalle_articulo WHERE id_venta = {self.sale_id} ORDER BY cantidad DESC;")
        elif self.comboBox_2.currentText() == "Cantidad (ascendente)":
            self.cursor.execute(f"SELECT * FROM detalle_articulo WHERE id_venta = {self.sale_id} ORDER BY cantidad ASC;")
        elif self.comboBox_2.currentText() == "P/U (descendente)":
            self.cursor.execute(f"SELECT * FROM detalle_articulo WHERE id_venta = {self.sale_id} ORDER BY precio_unitario DESC;")
        else:
            self.cursor.execute(f"SELECT * FROM detalle_articulo WHERE id_venta = {self.sale_id} ORDER BY precio_unitario ASC;")
        details = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(details))
        if len(details) > 0:
            self.tableWidget.setColumnCount(len(details[0]))
            for i in range(len(details)):
                for j in range(len(details[i])):
                    self.tableWidget.setItem(i,j,QTableWidgetItem(str(details[i][j])))
        QTimer.singleShot(3000, self.setItems)

    def closeEvent(self,event):
        self.connection.close()
        self.cursor.close()
        event.accept()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"P/U", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Descuento", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Venta", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Tipo de articulo", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Ordenar", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Cantidad (descendente)", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Cantidad (ascendente)", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"P/U (descendente)", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"P/U (ascendente)", None))

    # retranslateUi

class clienteVentasDetalle(QMainWindow):
    def __init__(self,sale_id):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self,sale_id)
