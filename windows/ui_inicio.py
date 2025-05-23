# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inicioIgEnMq.ui'
##
## Created by: Qt User Interface Compiler version 5.15.15
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
import db
import ui_inicioR
import ui_menu

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1080, 720)
        self.mainWindow = MainWindow
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(340, 356, 400, 50))
        font = QFont()
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(340, 476, 400, 50))
        self.lineEdit_2.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(340, 315, 401, 31))
        font1 = QFont()
        font1.setPointSize(22)
        self.label.setFont(font1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(340, 430, 401, 31))
        self.label_2.setFont(font1)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(340, 560, 191, 71))
        self.pushButton.clicked.connect(self.goToInicioR)
        font2 = QFont()
        font2.setPointSize(16)
        self.pushButton.setFont(font2)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(550, 560, 191, 71))
        self.pushButton_2.setFont(font2)
        self.pushButton_2.clicked.connect(self.logIn)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(340, 60, 401, 221))
        self.label_3.setFont(font1)
        self.label_3.setPixmap(QPixmap(u"img\\s.png"))
        self.label_3.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"ID de usuario", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Crear cuenta", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Ingresar", None))
        self.label_3.setText("")
    # retranslateUi
    
    def goToInicioR(self):      
        self.inicioR = ui_inicioR.inicioR()
        self.inicioR.show()
    
    def logIn(self):
        connection = db.connect()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM empleado WHERE id_empleado = \'{self.lineEdit.text()}\';")
        account = cursor.fetchall()
        if len(account) == 0:
            self.label.setText("ID inexistente")
        else:
            self.label.setText("ID de usuario")
            if self.lineEdit_2.text() == f"{account[0][1][0:2]}{account[0][2][len(account[0][2])-4:len(account[0][2])]}":
                self.label_2.setText("Contrase\u00f1a")
                self.mainWindow.close()
                self.menu = ui_menu.menu(self.lineEdit.text())
                self.menu.show()
            else:
                self.label_2.setText("Contrase\u00f1a invalida")
        cursor.close()
        connection.close()

class inicio(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)