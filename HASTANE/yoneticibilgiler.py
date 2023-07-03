from PyQt5.QtWidgets import *
from yonetici_bilgiler import Ui_MainWindow
import mysql.connector

con = mysql.connector.connect(user='root',password = '',host = 'localhost',database = 'hastane')
cursor = con.cursor()


class YoneticiBilgileri(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.yoneticibilgiler = Ui_MainWindow()
        self.yoneticibilgiler.setupUi(self)
        self.yoneticibilgiler.yoneticigetir.clicked.connect(self.YoneticiGetir)
        self.yoneticibilgiler.temizle.clicked.connect(self.Temizle)
        self.yoneticibilgiler.yoneticiekle.clicked.connect(self.YoneticiEkle)
        self.yoneticibilgiler.yoneticisil.clicked.connect(self.YoneticiSil)
        self.yoneticibilgiler.yoneticiguncelle.clicked.connect(self.YoneticiGuncelle)
    

    def YoneticiGuncelle(self):
        id = self.yoneticibilgiler.yoneticiid.text()
        kulladi = self.yoneticibilgiler.yoneticikulladi.text()
        ad = self.yoneticibilgiler.yoneticiad.text()
        soyad = self.yoneticibilgiler.yoneticisoyad.text()
        sifre = self.yoneticibilgiler.yoneticiyenisifre.text()

        if kulladi == "" and ad == "" and soyad == "":
            cursor.execute("update yonetici set password = %s where id = %s",(sifre,id))
            self.yoneticibilgiler.statusbar.showMessage("Şifre Başarıyla Güncellendi !")
        elif ad == "" and soyad == "" and sifre == "":
            cursor.execute("update yonetici set username = %s where id = %s",(kulladi,id))
            self.yoneticibilgiler.statusbar.showMessage("Kullanıcı Adı Başarıyla Güncellendi !")
        elif soyad == "" and sifre == "" and kulladi == "":
            cursor.execute("update yonetici set ad = %s where id = %s",(ad,id))
            self.yoneticibilgiler.statusbar.showMessage("Ad Başarıyla Güncellendi !")
        elif kulladi == "" and ad == "" and sifre == "":
            cursor.execute("update yonetici set soyad = %s where id = %s",(soyad,id))
            self.yoneticibilgiler.statusbar.showMessage("Soyad Başarıyla Güncellendi !")
        else:
            cursor.execute("update set yonetici password = %s,username = %s,ad = %s,soyad = %s where id = %s",(sifre,kulladi,ad,soyad,id))
            self.yoneticibilgiler.statusbar.showMessage("Bilgiler Başarıyla Güncellendi !")
            con.commit()
            self.Temizle()
    

    def YoneticiSil(self):
        id = self.yoneticibilgiler.yoneticiid.text()
        query = "delete from yonetici where id = %s"
        cursor.execute(query,(id,))   
        con.commit()
        self.yoneticibilgiler.statusbar.showMessage("Yönetici Başarıyla Silindi !")


    def YoneticiEkle(self):
        kulladi = self.yoneticibilgiler.yoneticikulladi.text()
        ad = self.yoneticibilgiler.yoneticiad.text()
        soyad = self.yoneticibilgiler.yoneticisoyad.text()
        sifre = self.yoneticibilgiler.yoneticimevcutsifre.text()
        query = "Insert into yonetici(ad,soyad,username,password) VALUES(%s,%s,%s,%s)"
        cursor.execute(query,(ad,soyad,kulladi,sifre))
        con.commit()
        self.yoneticibilgiler.statusbar.showMessage("Yönetici Başarıyla Eklendi !")
        self.Temizle()

    

    def YoneticiGetir(self):
        self.yoneticibilgiler.yoneticitablo.clear()
        self.yoneticibilgiler.yoneticitablo.setHorizontalHeaderLabels(("id","Ad","Soyad","Kullanıcı Adı"))
        query = "Select id,ad,soyad,username from yonetici"
        cursor.execute(query)
        for indexSatir,kayitNumarasi in enumerate(cursor):
            for indexSutun,kayitSutun in enumerate(kayitNumarasi):
               self.yoneticibilgiler.yoneticitablo.setItem(indexSatir,indexSutun,QTableWidgetItem(str(kayitSutun)))
    

    def Temizle(self):
        self.yoneticibilgiler.yoneticiid.clear()
        self.yoneticibilgiler.yoneticikulladi.clear()
        self.yoneticibilgiler.yoneticiad.clear()
        self.yoneticibilgiler.yoneticisoyad.clear()
        self.yoneticibilgiler.yoneticimevcutsifre.clear()
        self.yoneticibilgiler.yoneticiyenisifre.clear()

