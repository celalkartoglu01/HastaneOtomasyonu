# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doktorpaneli.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(833, 653)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -50, 881, 691))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("5c4bd40a58fe131cf068arkaplan2.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 71, 71))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("20200316220122!Saglikbakanligi_logo (2).png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 20, 651, 41))
        self.label_3.setObjectName("label_3")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 70, 151, 541))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.doktorkullanici = QtWidgets.QPushButton(self.layoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("indir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.doktorkullanici.setIcon(icon)
        self.doktorkullanici.setObjectName("doktorkullanici")
        self.verticalLayout.addWidget(self.doktorkullanici)
        self.doktorrandevularim = QtWidgets.QPushButton(self.layoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("png-transparent-southeast-physical-therapy-management-computer-icons-business-diary-appointment-miscellaneous-employment-medicine.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.doktorrandevularim.setIcon(icon1)
        self.doktorrandevularim.setObjectName("doktorrandevularim")
        self.verticalLayout.addWidget(self.doktorrandevularim)
        self.randevusil = QtWidgets.QPushButton(self.layoutWidget)
        self.randevusil.setIcon(icon1)
        self.randevusil.setObjectName("randevusil")
        self.verticalLayout.addWidget(self.randevusil)
        self.doktorbekleyenhasta = QtWidgets.QPushButton(self.layoutWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("png-transparent-user-logo-computer-icons-industry-icon-user-experience-room-logo-black.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.doktorbekleyenhasta.setIcon(icon2)
        self.doktorbekleyenhasta.setObjectName("doktorbekleyenhasta")
        self.verticalLayout.addWidget(self.doktorbekleyenhasta)
        self.tahlilsonuclari = QtWidgets.QPushButton(self.layoutWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("png-transparent-adobe-logo-document-computer-software-management-data-business-finance-user-report-marketing.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tahlilsonuclari.setIcon(icon3)
        self.tahlilsonuclari.setObjectName("tahlilsonuclari")
        self.verticalLayout.addWidget(self.tahlilsonuclari)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 833, 21))
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
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">DOKTOR PANELİ</span></p></body></html>"))
        self.doktorkullanici.setText(_translate("MainWindow", "Kullanıcı"))
        self.doktorrandevularim.setText(_translate("MainWindow", "Randevularım"))
        self.randevusil.setText(_translate("MainWindow", "Randevu Sil"))
        self.doktorbekleyenhasta.setText(_translate("MainWindow", "Bekleyen Hasta"))
        self.tahlilsonuclari.setText(_translate("MainWindow", "Tahlil Sonuçları"))