# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'iletisim.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 643)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 861, 681))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Adsız.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 71, 71))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("20200316220122!Saglikbakanligi_logo (2).png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 20, 651, 41))
        self.label_3.setObjectName("label_3")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(20, 140, 561, 23))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label_4 = QtWidgets.QLabel(self.splitter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.splitter)
        self.label_5.setObjectName("label_5")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(20, 210, 311, 23))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_6 = QtWidgets.QLabel(self.splitter_2)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.splitter_2)
        self.label_7.setObjectName("label_7")
        self.splitter_3 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_3.setGeometry(QtCore.QRect(30, 290, 161, 23))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.label_8 = QtWidgets.QLabel(self.splitter_3)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.splitter_3)
        self.label_9.setObjectName("label_9")
        self.splitter_4 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_4.setGeometry(QtCore.QRect(18, 360, 561, 23))
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.label_10 = QtWidgets.QLabel(self.splitter_4)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.splitter_4)
        self.label_11.setObjectName("label_11")
        self.splitter_5 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_5.setGeometry(QtCore.QRect(20, 430, 251, 23))
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.label_12 = QtWidgets.QLabel(self.splitter_5)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.splitter_5)
        self.label_13.setObjectName("label_13")
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
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">İLETİŞİM BİLGİLERİMİZ</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Adres :</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Roboto\',\'sans-serif\'; font-size:9pt; font-weight:600; color:#000000; background-color:#ffffff;\">Ulukent Mahallesi (Doğukent Depo Mevkii) Onbaşı Sokak No: 99 Elazığ / Merkez</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Telefon :</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Roboto\',\'sans-serif\'; font-size:14px; color:#444444; background-color:#ffffff;\">0424 606 60 00--0424 238 10 00</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Fax :</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Roboto\',\'sans-serif\'; font-size:14px; color:#444444; background-color:#ffffff;\">0424 212 14 61</span><span style=\" font-family:\'Roboto\',\'sans-serif\'; font-size:14px; color:#444444; background-color:#ffffff;\"/></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Yüksek Güvenlikli Adli Psikiyatri (YGAP) Fax :</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Roboto\',\'sans-serif\'; font-size:14px; color:#444444; background-color:#ffffff;\"> 0424 238 76 58</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">E-Posta :</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Roboto\',\'sans-serif\'; font-size:14px; color:#444444; background-color:#ffffff;\">elazigsehir@saglik.gov.tr</span></p></body></html>"))