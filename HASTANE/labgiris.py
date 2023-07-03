from PyQt5.QtWidgets import *
from laboratuvar import Ui_MainWindow
from lab_2 import Lab2
import mysql.connector

con = mysql.connector.connect(user='root',password = '',host = 'localhost',database = 'hastane')
cursor = con.cursor()


class Laboratuvar(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.laboratuvar = Ui_MainWindow()
        self.laboratuvar.setupUi(self)
        self.lab2 = Lab2()
        self.laboratuvar.btnlabgiris.clicked.connect(self.GirisYap)
    
    def GirisYap(self):
        kulladi = self.laboratuvar.labkulladi.text()
        sifre = self.laboratuvar.labsifre.text()
        query = ("Select * from laboratuvar where kulladi = '"+kulladi+"' and parola = '"+ sifre + "'")
        cursor.execute(query)
        result = cursor.fetchone()
        if result:
            self.lab2.show()
            self.laboratuvar.statusbar.showMessage("Başarıyla Giriş Yapıldı !")
            self.laboratuvar.labkulladi.clear()
            self.laboratuvar.labsifre.clear()
        else:
            self.laboratuvar.statusbar.showMessage("Kullanıcı Adı veya Şifre Hatalı !")
        