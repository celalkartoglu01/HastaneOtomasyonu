from PyQt5.QtWidgets import *
from hasta import Ui_MainWindow
from hastapaneli import HastaPaneli
import mysql.connector

con = mysql.connector.connect(user='root',password = '',host = 'localhost',database = 'hastane')
cursor = con.cursor()

class HastaGiris(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.hastagiris = Ui_MainWindow()
        self.hastagiris.setupUi(self)
        self.hasta = HastaPaneli()
        self.hastagiris.btnhastagiris.clicked.connect(self.GirisYap)
    
    def GirisYap(self):
        kulladi = self.hastagiris.hastalkulladi.text()
        sifre = self.hastagiris.hastasifre.text()
        query = ("Select * from hasta where kulladi = '"+kulladi+"' and parola = '"+ sifre + "'")
        cursor.execute(query)
        result = cursor.fetchone()
        if result:
            self.hide()
            self.hasta.show()
            self.hastagiris.statusbar.showMessage("Başarıyla Giriş Yapıldı !")
            self.hastagiris.hastalkulladi.clear()
            self.hastagiris.hastasifre.clear()
        else:
            self.hastagiris.statusbar.showMessage("Kullanıcı Adı veya Şifre Hatalı !")
    

