# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lab2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 316)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -40, 831, 321))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Adsız.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 10, 381, 41))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 71, 71))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("20200316220122!Saglikbakanligi_logo (2).png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(520, 150, 81, 20))
        self.label_8.setObjectName("label_8")
        self.testgonder = QtWidgets.QPushButton(self.centralwidget)
        self.testgonder.setGeometry(QtCore.QRect(630, 240, 75, 23))
        self.testgonder.setObjectName("testgonder")
        self.testler = QtWidgets.QTableWidget(self.centralwidget)
        self.testler.setGeometry(QtCore.QRect(20, 110, 431, 131))
        self.testler.setRowCount(20)
        self.testler.setColumnCount(6)
        self.testler.setObjectName("testler")
        item = QtWidgets.QTableWidgetItem()
        self.testler.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.testler.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.testler.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.testler.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.testler.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.testler.setHorizontalHeaderItem(5, item)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(80, 80, 111, 20))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label_4 = QtWidgets.QLabel(self.splitter)
        self.label_4.setObjectName("label_4")
        self.testid = QtWidgets.QLineEdit(self.splitter)
        self.testid.setObjectName("testid")
        self.splitter_3 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_3.setGeometry(QtCore.QRect(590, 100, 0, 20))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.hastaadi = QtWidgets.QLineEdit(self.centralwidget)
        self.hastaadi.setGeometry(QtCore.QRect(651, 10, 111, 20))
        self.hastaadi.setObjectName("hastaadi")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(565, 10, 81, 20))
        self.label_6.setObjectName("label_6")
        self.hastasoyadi = QtWidgets.QLineEdit(self.centralwidget)
        self.hastasoyadi.setGeometry(QtCore.QRect(651, 40, 111, 20))
        self.hastasoyadi.setObjectName("hastasoyadi")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(555, 40, 91, 20))
        self.label_7.setObjectName("label_7")
        self.doktoradi = QtWidgets.QComboBox(self.centralwidget)
        self.doktoradi.setGeometry(QtCore.QRect(650, 70, 131, 20))
        self.doktoradi.setObjectName("doktoradi")
        self.doktoradi.addItem("")
        self.doktoradi.addItem("")
        self.doktoradi.addItem("")
        self.doktoradi.addItem("")
        self.doktoradi.addItem("")
        self.doktoradi.addItem("")
        self.doktoradi.addItem("")
        self.doktoradi.addItem("")
        self.doktoradi.addItem("")
        self.doktoradi.addItem("")
        self.doktoradi.addItem("")
        self.doktoradi.addItem("")
        self.doktoradi.addItem("")
        self.doktoradi.addItem("")
        self.doktoradi.addItem("")
        self.doktoradi.addItem("")
        self.doktoradi.addItem("")
        self.doktoradi.addItem("")
        self.doktoradi.addItem("")
        self.doktoradi.addItem("")
        self.doktoradi.addItem("")
        self.doktoradi.addItem("")
        self.doktoradi.addItem("")
        self.doktoradi.addItem("")
        self.doktoradi.addItem("")
        self.doktoradi.addItem("")
        self.doktoradi.addItem("")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(550, 70, 91, 20))
        self.label_9.setObjectName("label_9")
        self.testadi = QtWidgets.QLineEdit(self.centralwidget)
        self.testadi.setGeometry(QtCore.QRect(650, 110, 111, 20))
        self.testadi.setObjectName("testadi")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(550, 110, 91, 20))
        self.label_10.setObjectName("label_10")
        self.ara = QtWidgets.QPushButton(self.centralwidget)
        self.ara.setGeometry(QtCore.QRect(470, 220, 75, 23))
        self.ara.setObjectName("ara")
        self.testsonuc = QtWidgets.QLineEdit(self.centralwidget)
        self.testsonuc.setGeometry(QtCore.QRect(650, 150, 111, 81))
        self.testsonuc.setObjectName("testsonuc")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">LABORATUVAR</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Test Sonucu :</span></p></body></html>"))
        self.testgonder.setText(_translate("MainWindow", "Gönder"))
        item = self.testler.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "test_id"))
        item = self.testler.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "test_adi"))
        item = self.testler.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "doktor_adi"))
        item = self.testler.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "hasta_adi"))
        item = self.testler.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "hasta_soyadi"))
        item = self.testler.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "aciklama"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Test ID</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Hasta Adi:</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Hasta Soyadi:</span></p></body></html>"))
        self.doktoradi.setItemText(0, _translate("MainWindow", "Betül YÜRÜRDURMAZ"))
        self.doktoradi.setItemText(1, _translate("MainWindow", "Meltem KANAR"))
        self.doktoradi.setItemText(2, _translate("MainWindow", "Onur HANBEYOĞLU"))
        self.doktoradi.setItemText(3, _translate("MainWindow", "Serdal ALBAYRAK"))
        self.doktoradi.setItemText(4, _translate("MainWindow", "Serkan YILMAZ"))
        self.doktoradi.setItemText(5, _translate("MainWindow", "İbrahim AKDENİZ"))
        self.doktoradi.setItemText(6, _translate("MainWindow", "Asiye Elvan KUMKAYIR"))
        self.doktoradi.setItemText(7, _translate("MainWindow", "Cihan ÖNDER"))
        self.doktoradi.setItemText(8, _translate("MainWindow", "Savaş ÖZTÜRK"))
        self.doktoradi.setItemText(9, _translate("MainWindow", "Münevver Gizem HEKİM"))
        self.doktoradi.setItemText(10, _translate("MainWindow", "Tamer GÜNDOĞDU"))
        self.doktoradi.setItemText(11, _translate("MainWindow", "Sadık KEŞMER"))
        self.doktoradi.setItemText(12, _translate("MainWindow", "Semih KOÇYİĞİT"))
        self.doktoradi.setItemText(13, _translate("MainWindow", "Sinem KESER"))
        self.doktoradi.setItemText(14, _translate("MainWindow", "Ahmet SERTKAYA"))
        self.doktoradi.setItemText(15, _translate("MainWindow", "Selçuk KAPLAN"))
        self.doktoradi.setItemText(16, _translate("MainWindow", "Suna AYDIN"))
        self.doktoradi.setItemText(17, _translate("MainWindow", "Mücahid YILMAZ"))
        self.doktoradi.setItemText(18, _translate("MainWindow", "Nihat SUSAMAN"))
        self.doktoradi.setItemText(19, _translate("MainWindow", "Ersin KILIÇ"))
        self.doktoradi.setItemText(20, _translate("MainWindow", "Ali Sami ŞEKER"))
        self.doktoradi.setItemText(21, _translate("MainWindow", "Tevfik BALIKÇI"))
        self.doktoradi.setItemText(22, _translate("MainWindow", "Ela KAPLAN"))
        self.doktoradi.setItemText(23, _translate("MainWindow", "Mustafa Hakan DEMİRBAŞ"))
        self.doktoradi.setItemText(24, _translate("MainWindow", "İrfan GÜLER"))
        self.doktoradi.setItemText(25, _translate("MainWindow", "Asude AKSOY"))
        self.doktoradi.setItemText(26, _translate("MainWindow", "Kadir YILDIRIM"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Doktor Adi:</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Test Adi:</span></p></body></html>"))
        self.ara.setText(_translate("MainWindow", "Ara"))
