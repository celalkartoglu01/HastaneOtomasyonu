from PyQt5.QtWidgets import *
from yonetici import Ui_MainWindow
from yoneticisayfasi import YoneticiPaneli
import mysql.connector

con = mysql.connector.connect(user='root',password = '',host = 'localhost',database = 'hastane')
cursor = con.cursor()



class Yonetici(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.yoneticigiris = Ui_MainWindow()
        self.yoneticigiris.setupUi(self)
        self.yoneticisayfasi = YoneticiPaneli()
        self.yoneticigiris.btnyoneticigiris.clicked.connect(self.GirisYap)
    
    def GirisYap(self):
        kulladi = self.yoneticigiris.lneyoneticikulladi.text()
        sifre = self.yoneticigiris.lneyoneticisifre.text()
        query = ("Select * From yonetici where username = '"+kulladi+"'and password ='" + sifre +"'")
        cursor.execute(query)
        result = cursor.fetchone()
        if result:
            self.hide()
            self.yoneticisayfasi.show()
            self.yoneticigiris.statusbar.showMessage("Başarıyla Giriş Yapıldı !")
            self.yoneticigiris.lneyoneticikulladi.clear()
            self.yoneticigiris.lneyoneticisifre.clear()

        else:
            self.yoneticigiris.statusbar.showMessage("Kullanıcı Adı veya Şifre Hatalı !")

   


