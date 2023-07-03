from PyQt5.QtWidgets import *
from hastakabul_giris import Ui_MainWindow
import mysql.connector

con = mysql.connector.connect(user='root',password = '',host = 'localhost',database = 'hastane')
cursor = con.cursor()

class HastaKabul(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.hastakabul = Ui_MainWindow()
        self.hastakabul.setupUi(self)
        self.hastakabul.acilkaydet.clicked.connect(self.AcilKaydet)
        self.hastakabul.muayenekaydet.clicked.connect(self.MuayeneKaydet)
    


    def AcilKaydet(self):
        tc = self.hastakabul.hasttatc.text()
        ad = self.hastakabul.hastaadi.text()
        soyad = self.hastakabul.hastasoyad.text()
        cinsiyet = self.hastakabul.hastacinsiyet.currentText()
        kangrubu = self.hastakabul.kangrubu.currentText()
        dogumyeri = self.hastakabul.dogumyeri.currentText()
        dogumtarihi = self.hastakabul.dogumtarihi.text()
        babaadi = self.hastakabul.babadi.text()
        anaadi = self.hastakabul.anaadi.text()
        cepno = self.hastakabul.cepno.text()
        eposta = self.hastakabul.eposta.text()
        adres = self.hastakabul.hastaadres.text()
        durum = self.hastakabul.acildurum.text()
        acilklinik = self.hastakabul.acilklinik.currentText()
        doktor = self.hastakabul.acildoktor.currentText()
        sikayet = self.hastakabul.acilsikayet.text()
        query = "Insert into acilgiris(tc,ad,soyad,cinsiyet,kangrubu,dogumyeri,dogumtarihi,babaadi,anaadi,cepno,eposta,adres,durum,acilklinik,doktor,sikayet) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(query,(tc,ad,soyad,cinsiyet,kangrubu,dogumyeri,dogumtarihi,babaadi,anaadi,cepno,eposta,adres,durum,acilklinik,doktor,sikayet))
        con.commit()
        self.hastakabul.statusbar.showMessage("Acil Kaydı Oluşturuldu !")
        self.Temizle()
    

    def MuayeneKaydet(self):
        tc = self.hastakabul.hasttatc.text()
        ad = self.hastakabul.hastaadi.text()
        soyad = self.hastakabul.hastasoyad.text()
        cinsiyet = self.hastakabul.hastacinsiyet.currentText()
        kangrubu = self.hastakabul.kangrubu.currentText()
        dogumyeri = self.hastakabul.dogumyeri.currentText()
        dogumtarihi = self.hastakabul.dogumtarihi.text()
        babaadi = self.hastakabul.babadi.text()
        anaadi = self.hastakabul.anaadi.text()
        cepno = self.hastakabul.cepno.text()
        eposta = self.hastakabul.eposta.text()
        adres = self.hastakabul.hastaadres.text()
        muayeneklinik = self.hastakabul.muayeneklinik.currentText()
        muayenedoktor = self.hastakabul.muayenedoktor.currentText()
        query = "Insert into muayene(tc,ad,soyad,cinsiyet,kangrubu,dogumyeri,dogumtarihi,babaadi,anaadi,cepno,eposta,adres,muayeneklinik,muayenedoktor) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(query,(tc,ad,soyad,cinsiyet,kangrubu,dogumyeri,dogumtarihi,babaadi,anaadi,cepno,eposta,adres,muayeneklinik,muayenedoktor))
        con.commit()
        self.hastakabul.statusbar.showMessage("Başarıyla Randevu Alındı !")
        self.Temizle()
    


    def Temizle(self):
        self.hastakabul.hasttatc.clear()
        self.hastakabul.hastaadi.clear()
        self.hastakabul.hastasoyad.clear()
        self.hastakabul.dogumtarihi.clear()
        self.hastakabul.babadi.clear()
        self.hastakabul.anaadi.clear()
        self.hastakabul.cepno.clear()
        self.hastakabul.eposta.clear()
        self.hastakabul.hastaadres.clear()
        self.hastakabul.acilsikayet.clear()
        self.hastakabul.acildurum.clear()




