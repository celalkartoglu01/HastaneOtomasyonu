# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kaydol.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(489, 682)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-30, -30, 641, 701))
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
        self.label_3.setGeometry(QtCore.QRect(60, 10, 391, 41))
        self.label_3.setObjectName("label_3")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(30, 530, 141, 34))
        self.label_16.setObjectName("label_16")
        self.kayitol = QtWidgets.QPushButton(self.centralwidget)
        self.kayitol.setGeometry(QtCore.QRect(360, 540, 111, 51))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("png-transparent-computer-icons-register-button-miscellaneous-text-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kayitol.setIcon(icon)
        self.kayitol.setObjectName("kayitol")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(10, 70, 327, 451))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget)
        self.label_17.setObjectName("label_17")
        self.verticalLayout.addWidget(self.label_17)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        self.label_15.setObjectName("label_15")
        self.verticalLayout.addWidget(self.label_15)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tc = QtWidgets.QLineEdit(self.layoutWidget1)
        self.tc.setObjectName("tc")
        self.verticalLayout_2.addWidget(self.tc)
        self.hastaadi = QtWidgets.QLineEdit(self.layoutWidget1)
        self.hastaadi.setObjectName("hastaadi")
        self.verticalLayout_2.addWidget(self.hastaadi)
        self.hastasoyadi = QtWidgets.QLineEdit(self.layoutWidget1)
        self.hastasoyadi.setObjectName("hastasoyadi")
        self.verticalLayout_2.addWidget(self.hastasoyadi)
        self.cinsiyet = QtWidgets.QComboBox(self.layoutWidget1)
        self.cinsiyet.setObjectName("cinsiyet")
        self.cinsiyet.addItem("")
        self.cinsiyet.addItem("")
        self.verticalLayout_2.addWidget(self.cinsiyet)
        self.kayitkangrubu = QtWidgets.QComboBox(self.layoutWidget1)
        self.kayitkangrubu.setObjectName("kayitkangrubu")
        self.kayitkangrubu.addItem("")
        self.kayitkangrubu.addItem("")
        self.kayitkangrubu.addItem("")
        self.kayitkangrubu.addItem("")
        self.kayitkangrubu.addItem("")
        self.kayitkangrubu.addItem("")
        self.kayitkangrubu.addItem("")
        self.kayitkangrubu.addItem("")
        self.verticalLayout_2.addWidget(self.kayitkangrubu)
        self.kayitdogumyeri = QtWidgets.QComboBox(self.layoutWidget1)
        self.kayitdogumyeri.setObjectName("kayitdogumyeri")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.kayitdogumyeri.addItem("")
        self.verticalLayout_2.addWidget(self.kayitdogumyeri)
        self.dogumtarihi = QtWidgets.QLineEdit(self.layoutWidget1)
        self.dogumtarihi.setObjectName("dogumtarihi")
        self.verticalLayout_2.addWidget(self.dogumtarihi)
        self.babaadi = QtWidgets.QLineEdit(self.layoutWidget1)
        self.babaadi.setObjectName("babaadi")
        self.verticalLayout_2.addWidget(self.babaadi)
        self.anaadi = QtWidgets.QLineEdit(self.layoutWidget1)
        self.anaadi.setObjectName("anaadi")
        self.verticalLayout_2.addWidget(self.anaadi)
        self.cepno = QtWidgets.QLineEdit(self.layoutWidget1)
        self.cepno.setObjectName("cepno")
        self.verticalLayout_2.addWidget(self.cepno)
        self.eposta = QtWidgets.QLineEdit(self.layoutWidget1)
        self.eposta.setObjectName("eposta")
        self.verticalLayout_2.addWidget(self.eposta)
        self.kullaniciadi = QtWidgets.QLineEdit(self.layoutWidget1)
        self.kullaniciadi.setObjectName("kullaniciadi")
        self.verticalLayout_2.addWidget(self.kullaniciadi)
        self.parola = QtWidgets.QLineEdit(self.layoutWidget1)
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.parola.setObjectName("parola")
        self.verticalLayout_2.addWidget(self.parola)
        self.adres = QtWidgets.QLineEdit(self.centralwidget)
        self.adres.setGeometry(QtCore.QRect(210, 530, 131, 71))
        self.adres.setObjectName("adres")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 489, 21))
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
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">KAYIT EKRANI</span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Hasta Adres</span></p></body></html>"))
        self.kayitol.setText(_translate("MainWindow", "Kaydol"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Hasta T.C. </span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Hasta Adı</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Hasta Soyadı</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Hasta Cinsiyeti</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Kan Grubu</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Hasta Doğum Yeri</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Hasta Doğum Tarihi</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Hasta Baba Adı</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Hasta Anne Adı</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Hasta Cep No.</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Hasta E-Posta</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Kullanıcı Adı</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Parola</span></p></body></html>"))
        self.cinsiyet.setItemText(0, _translate("MainWindow", "Erkek"))
        self.cinsiyet.setItemText(1, _translate("MainWindow", "Kadın"))
        self.kayitkangrubu.setItemText(0, _translate("MainWindow", "A+"))
        self.kayitkangrubu.setItemText(1, _translate("MainWindow", "A-"))
        self.kayitkangrubu.setItemText(2, _translate("MainWindow", "B+"))
        self.kayitkangrubu.setItemText(3, _translate("MainWindow", "B-"))
        self.kayitkangrubu.setItemText(4, _translate("MainWindow", "AB+"))
        self.kayitkangrubu.setItemText(5, _translate("MainWindow", "AB-"))
        self.kayitkangrubu.setItemText(6, _translate("MainWindow", "0+"))
        self.kayitkangrubu.setItemText(7, _translate("MainWindow", "0-"))
        self.kayitdogumyeri.setItemText(0, _translate("MainWindow", "Adana"))
        self.kayitdogumyeri.setItemText(1, _translate("MainWindow", "Adıyaman"))
        self.kayitdogumyeri.setItemText(2, _translate("MainWindow", "Afyonkarahisar"))
        self.kayitdogumyeri.setItemText(3, _translate("MainWindow", "Ağrı"))
        self.kayitdogumyeri.setItemText(4, _translate("MainWindow", "Aksaray"))
        self.kayitdogumyeri.setItemText(5, _translate("MainWindow", "Amasya"))
        self.kayitdogumyeri.setItemText(6, _translate("MainWindow", "Ankara"))
        self.kayitdogumyeri.setItemText(7, _translate("MainWindow", "Antalya"))
        self.kayitdogumyeri.setItemText(8, _translate("MainWindow", "Ardahan"))
        self.kayitdogumyeri.setItemText(9, _translate("MainWindow", "Artvin"))
        self.kayitdogumyeri.setItemText(10, _translate("MainWindow", "Aydın"))
        self.kayitdogumyeri.setItemText(11, _translate("MainWindow", "Balıkesir"))
        self.kayitdogumyeri.setItemText(12, _translate("MainWindow", "Bartın"))
        self.kayitdogumyeri.setItemText(13, _translate("MainWindow", "Batman"))
        self.kayitdogumyeri.setItemText(14, _translate("MainWindow", "Bayburt"))
        self.kayitdogumyeri.setItemText(15, _translate("MainWindow", "Bilecik"))
        self.kayitdogumyeri.setItemText(16, _translate("MainWindow", "Bingöl"))
        self.kayitdogumyeri.setItemText(17, _translate("MainWindow", "Bitlis"))
        self.kayitdogumyeri.setItemText(18, _translate("MainWindow", "Bolu"))
        self.kayitdogumyeri.setItemText(19, _translate("MainWindow", "Burdur"))
        self.kayitdogumyeri.setItemText(20, _translate("MainWindow", "Bursa"))
        self.kayitdogumyeri.setItemText(21, _translate("MainWindow", "Çanakkale"))
        self.kayitdogumyeri.setItemText(22, _translate("MainWindow", "Çankırı"))
        self.kayitdogumyeri.setItemText(23, _translate("MainWindow", "Çorum"))
        self.kayitdogumyeri.setItemText(24, _translate("MainWindow", "Denizli"))
        self.kayitdogumyeri.setItemText(25, _translate("MainWindow", "Diyarbakır"))
        self.kayitdogumyeri.setItemText(26, _translate("MainWindow", "Düzce"))
        self.kayitdogumyeri.setItemText(27, _translate("MainWindow", "Edirne"))
        self.kayitdogumyeri.setItemText(28, _translate("MainWindow", "Elazığ"))
        self.kayitdogumyeri.setItemText(29, _translate("MainWindow", "Erzincan    "))
        self.kayitdogumyeri.setItemText(30, _translate("MainWindow", "Erzurum"))
        self.kayitdogumyeri.setItemText(31, _translate("MainWindow", "Eskişehir"))
        self.kayitdogumyeri.setItemText(32, _translate("MainWindow", "Gaziantep"))
        self.kayitdogumyeri.setItemText(33, _translate("MainWindow", "Giresun"))
        self.kayitdogumyeri.setItemText(34, _translate("MainWindow", "Gümüşhane    "))
        self.kayitdogumyeri.setItemText(35, _translate("MainWindow", "Hakkâri"))
        self.kayitdogumyeri.setItemText(36, _translate("MainWindow", "Hatay"))
        self.kayitdogumyeri.setItemText(37, _translate("MainWindow", "Iğdır"))
        self.kayitdogumyeri.setItemText(38, _translate("MainWindow", "Isparta"))
        self.kayitdogumyeri.setItemText(39, _translate("MainWindow", "İstanbul"))
        self.kayitdogumyeri.setItemText(40, _translate("MainWindow", "İzmir"))
        self.kayitdogumyeri.setItemText(41, _translate("MainWindow", "Kahramanmaraş"))
        self.kayitdogumyeri.setItemText(42, _translate("MainWindow", "Karabük"))
        self.kayitdogumyeri.setItemText(43, _translate("MainWindow", "Karaman"))
        self.kayitdogumyeri.setItemText(44, _translate("MainWindow", "Kars"))
        self.kayitdogumyeri.setItemText(45, _translate("MainWindow", "Kastamonu"))
        self.kayitdogumyeri.setItemText(46, _translate("MainWindow", "Kayseri"))
        self.kayitdogumyeri.setItemText(47, _translate("MainWindow", "Kırıkkale"))
        self.kayitdogumyeri.setItemText(48, _translate("MainWindow", "Kırklareli"))
        self.kayitdogumyeri.setItemText(49, _translate("MainWindow", "Kırşehir"))
        self.kayitdogumyeri.setItemText(50, _translate("MainWindow", "Kilis"))
        self.kayitdogumyeri.setItemText(51, _translate("MainWindow", "Kocaeli"))
        self.kayitdogumyeri.setItemText(52, _translate("MainWindow", "Konya"))
        self.kayitdogumyeri.setItemText(53, _translate("MainWindow", "Kütahya"))
        self.kayitdogumyeri.setItemText(54, _translate("MainWindow", "Malatya"))
        self.kayitdogumyeri.setItemText(55, _translate("MainWindow", "Manisa"))
        self.kayitdogumyeri.setItemText(56, _translate("MainWindow", "Mardin"))
        self.kayitdogumyeri.setItemText(57, _translate("MainWindow", "Mersin"))
        self.kayitdogumyeri.setItemText(58, _translate("MainWindow", "Muğla"))
        self.kayitdogumyeri.setItemText(59, _translate("MainWindow", "Muş"))
        self.kayitdogumyeri.setItemText(60, _translate("MainWindow", "Nevşehir"))
        self.kayitdogumyeri.setItemText(61, _translate("MainWindow", "Niğde"))
        self.kayitdogumyeri.setItemText(62, _translate("MainWindow", "Ordu"))
        self.kayitdogumyeri.setItemText(63, _translate("MainWindow", "Osmaniye"))
        self.kayitdogumyeri.setItemText(64, _translate("MainWindow", "Rize"))
        self.kayitdogumyeri.setItemText(65, _translate("MainWindow", "Sakarya"))
        self.kayitdogumyeri.setItemText(66, _translate("MainWindow", "Samsun"))
        self.kayitdogumyeri.setItemText(67, _translate("MainWindow", "Siirt"))
        self.kayitdogumyeri.setItemText(68, _translate("MainWindow", "Sinop"))
        self.kayitdogumyeri.setItemText(69, _translate("MainWindow", "Sivas"))
        self.kayitdogumyeri.setItemText(70, _translate("MainWindow", "Şanlıurfa"))
        self.kayitdogumyeri.setItemText(71, _translate("MainWindow", "Şırnak"))
        self.kayitdogumyeri.setItemText(72, _translate("MainWindow", "Tekirdağ"))
        self.kayitdogumyeri.setItemText(73, _translate("MainWindow", "Tokat"))
        self.kayitdogumyeri.setItemText(74, _translate("MainWindow", "Trabzon"))
        self.kayitdogumyeri.setItemText(75, _translate("MainWindow", "Tunceli"))
        self.kayitdogumyeri.setItemText(76, _translate("MainWindow", "Uşak"))
        self.kayitdogumyeri.setItemText(77, _translate("MainWindow", "Van"))
        self.kayitdogumyeri.setItemText(78, _translate("MainWindow", "Yalova"))
        self.kayitdogumyeri.setItemText(79, _translate("MainWindow", "Yozgat"))
        self.kayitdogumyeri.setItemText(80, _translate("MainWindow", "Zonguldak"))
