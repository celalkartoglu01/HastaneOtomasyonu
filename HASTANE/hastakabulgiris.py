from PyQt5.QtWidgets import *
from hasta_kabul import Ui_MainWindow
from hastakabul import HastaKabul
import mysql.connector

con = mysql.connector.connect(user='root',password = '',host = 'localhost',database = 'hastane')
cursor = con.cursor()


class HastaKabulGiris(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.hastakabulgiris = Ui_MainWindow()
        self.hastakabulgiris.setupUi(self)
        self.hastakabul = HastaKabul()
        self.hastakabulgiris.btnhastakabul.clicked.connect(self.GirisYap)
    

    def GirisYap(self):
        kulladi = self.hastakabulgiris.hastakabulkulladi.text()
        sifre = self.hastakabulgiris.hastakabulsifre.text()
        query = ("Select * from doktor where kulladi = '"+kulladi+"' and parola = '"+ sifre + "'")
        cursor.execute(query)
        result = cursor.fetchone()
        if result:
            self.hide()
            self.hastakabul.show()
            self.hastakabulgiris.statusbar.showMessage("Başarıyla Giriş Yapıldı !")
            self.hastakabulgiris.hastakabulkulladi.clear()
            self.hastakabulgiris.hastakabulsifre.clear()
        else:
            self.hastakabulgiris.statusbar.showMessage("Kullanıcı Adı veya Şifre Hatalı !")


