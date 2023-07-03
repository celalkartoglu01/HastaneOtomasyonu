from PyQt5.QtWidgets import *
from kaydol import Ui_MainWindow
import mysql.connector

con = mysql.connector.connect(user='root',password = '',host = 'localhost',database = 'hastane')
cursor = con.cursor()


class Kaydol(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.kaydol = Ui_MainWindow()
        self.kaydol.setupUi(self)
        self.kaydol.kayitol.clicked.connect(self.KayitOl)
    

    def KayitOl(self):
        hastatc = self.kaydol.tc.text()
        hastaadi = self.kaydol.hastaadi.text()
        hastasoyadi = self.kaydol.hastasoyadi.text()
        cinsiyet = self.kaydol.cinsiyet.currentText()
        kangrubu = self.kaydol.kayitkangrubu.currentText()
        dogumyeri = self.kaydol.kayitdogumyeri.currentText()
        dogumtarihi = self.kaydol.dogumtarihi.text()
        babaadi = self.kaydol.babaadi.text()
        anaadi = self.kaydol.anaadi.text()
        cepno = self.kaydol.cepno.text()
        eposta = self.kaydol.eposta.text()
        kulladi = self.kaydol.kullaniciadi.text()
        sifre = self.kaydol.parola.text()
        hastaadres = self.kaydol.adres.text()
        query = "Insert into hasta(tc,ad,soyad,cinsiyet,kangrubu,dogumyeri,dogumtarihi,babaadi,anaadi,cepno,eposta,kulladi,parola,adres) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(query,(hastatc,hastaadi,hastasoyadi,cinsiyet,kangrubu,dogumyeri,dogumtarihi,babaadi,anaadi,cepno,eposta,kulladi,sifre,hastaadres))
        con.commit()
        cursor.close()
        self.kaydol.statusbar.showMessage("Kaydınız Oluşturuldu !")
        self.hide()

