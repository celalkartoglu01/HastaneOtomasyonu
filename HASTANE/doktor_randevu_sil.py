# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doktorandevusil.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(897, 638)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -30, 921, 651))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Adsız.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 71, 71))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("20200316220122!Saglikbakanligi_logo (2).png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 30, 651, 41))
        self.label_3.setObjectName("label_3")
        self.randevular = QtWidgets.QTableWidget(self.centralwidget)
        self.randevular.setGeometry(QtCore.QRect(180, 150, 541, 192))
        self.randevular.setRowCount(100)
        self.randevular.setObjectName("randevular")
        self.randevular.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.randevular.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.randevular.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.randevular.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.randevular.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.randevular.setHorizontalHeaderItem(4, item)
        self.hastaara = QtWidgets.QPushButton(self.centralwidget)
        self.hastaara.setGeometry(QtCore.QRect(730, 380, 91, 23))
        self.hastaara.setObjectName("hastaara")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(470, 380, 101, 16))
        self.label_4.setObjectName("label_4")
        self.hastaid = QtWidgets.QLineEdit(self.centralwidget)
        self.hastaid.setGeometry(QtCore.QRect(580, 380, 121, 20))
        self.hastaid.setObjectName("hastaid")
        self.randevusil = QtWidgets.QPushButton(self.centralwidget)
        self.randevusil.setGeometry(QtCore.QRect(730, 430, 91, 23))
        self.randevusil.setObjectName("randevusil")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 897, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">RANDEVULAR</span></p></body></html>"))
        item = self.randevular.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "hasta_id"))
        item = self.randevular.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "klinik_adi"))
        item = self.randevular.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "doktor"))
        item = self.randevular.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "tarih"))
        item = self.randevular.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "saat"))
        self.hastaara.setText(_translate("MainWindow", "Hasta Ara"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Hasta ID</span></p></body></html>"))
        self.randevusil.setText(_translate("MainWindow", "Randevu Sil"))