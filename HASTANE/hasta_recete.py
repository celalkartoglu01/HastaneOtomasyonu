# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hastarecete.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(956, 728)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -40, 1001, 781))
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
        self.label_3.setGeometry(QtCore.QRect(150, 30, 651, 41))
        self.label_3.setObjectName("label_3")
        self.tahliller = QtWidgets.QTableWidget(self.centralwidget)
        self.tahliller.setGeometry(QtCore.QRect(120, 190, 701, 192))
        self.tahliller.setRowCount(100)
        self.tahliller.setObjectName("tahliller")
        self.tahliller.setColumnCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tahliller.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tahliller.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tahliller.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tahliller.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tahliller.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tahliller.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tahliller.setHorizontalHeaderItem(6, item)
        self.hastaad = QtWidgets.QLineEdit(self.centralwidget)
        self.hastaad.setGeometry(QtCore.QRect(160, 430, 113, 20))
        self.hastaad.setObjectName("hastaad")
        self.ara = QtWidgets.QPushButton(self.centralwidget)
        self.ara.setGeometry(QtCore.QRect(100, 530, 91, 23))
        self.ara.setObjectName("ara")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 430, 141, 21))
        self.label_4.setObjectName("label_4")
        self.receteyazdir = QtWidgets.QPushButton(self.centralwidget)
        self.receteyazdir.setGeometry(QtCore.QRect(440, 460, 91, 23))
        self.receteyazdir.setObjectName("receteyazdir")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(330, 410, 331, 20))
        self.label_5.setObjectName("label_5")
        self.hastasoyad = QtWidgets.QLineEdit(self.centralwidget)
        self.hastasoyad.setGeometry(QtCore.QRect(160, 460, 113, 20))
        self.hastasoyad.setObjectName("hastasoyad")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 460, 141, 21))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 956, 21))
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
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">REÇETELERİM</span></p></body></html>"))
        item = self.tahliller.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "receteid"))
        item = self.tahliller.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "doktorad"))
        item = self.tahliller.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "doktorsoyad"))
        item = self.tahliller.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "hastaad"))
        item = self.tahliller.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "hastasoyad"))
        item = self.tahliller.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "tani"))
        item = self.tahliller.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "recete"))
        self.ara.setText(_translate("MainWindow", "Ara"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Hasta Ad</span></p></body></html>"))
        self.receteyazdir.setText(_translate("MainWindow", "Yazdır"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">*(Yazdırmak istediğiniz ilaçların üzerine tıklayınız.)</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Hasta Soyad</span></p></body></html>"))