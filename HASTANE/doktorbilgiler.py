from PyQt5.QtWidgets import *
from doktor_bilgiler import Ui_MainWindow
import mysql.connector

con = mysql.connector.connect(user='root',password = '',host = 'localhost',database = 'hastane')
cursor = con.cursor()

class DoktorBilgiler(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.doktorbilgiler = Ui_MainWindow()
        self.doktorbilgiler.setupUi(self)
        self.doktorbilgiler.guncelle.clicked.connect(self.Guncelle)
    

    def Guncelle(self):
        id = self.doktorbilgiler.id.text()
        kulladi = self.doktorbilgiler.doktorkulladi.text()
        tc = self.doktorbilgiler.doktortc.text()
        ad = self.doktorbilgiler.doktoradi.text()
        soyad = self.doktorbilgiler.doktorsoyadi.text()
        cinsiyet = self.doktorbilgiler.cinsiyet.text()
        kangrubu = self.doktorbilgiler.kangrubu.text()
        dogumtarihi = self.doktorbilgiler.dogumtarihi.text()
        cepno = self.doktorbilgiler.cepno.text()
        eposta = self.doktorbilgiler.eposta.text()
        parola = self.doktorbilgiler.yeniparola.text()
        adres = self.doktorbilgiler.doktoradres.text()
        klinik = self.doktorbilgiler.doktorklinik.text()

        if kulladi == "" and tc == "" and ad == "" and soyad == "" and cinsiyet == "" and kangrubu == "" and dogumtarihi == "" and cepno == "" and eposta == "" and parola == "" and klinik == "":
            cursor.execute("update doktor set adres = %s where id = %s",(adres,id))
            self.doktorbilgiler.statusbar.showMessage("Adres Başarıyla Güncellendi !")
            con.commit()
        elif kulladi == "" and tc == "" and ad == "" and soyad == "" and cinsiyet == "" and kangrubu == "" and dogumtarihi == "" and cepno == "" and eposta == "" and adres == "" and klinik =="":
            cursor.execute("update doktor set parola = %s where id = %s",(parola,id))
            self.doktorbilgiler.statusbar.showMessage("Parola Başarıyla Güncellendi !")
            con.commit()
        elif kulladi == "" and tc == "" and ad == "" and soyad == "" and cinsiyet=="" and kangrubu == "" and dogumtarihi == "" and cepno == "" and parola == "" and adres == "" and klinik =="":
            cursor.execute("update doktor set eposta = %s where id = %s",(eposta,id))
            self.doktorbilgiler.statusbar.showMessage("E-Posta Başarıyla Güncellendi !")
            con.commit()
        elif kulladi == "" and tc == "" and ad == "" and soyad == "" and cinsiyet == "" and kangrubu == "" and dogumtarihi == "" and eposta == "" and parola == "" and adres == "" and klinik  == "":
            cursor.execute("update doktor set cepno = %s where id = %s",(cepno,id))
            self.doktorbilgiler.statusbar.showMessage("Cep No. Başarıyla Güncellendi !")
            con.commit()
        elif kulladi == "" and tc == "" and ad == "" and soyad == "" and cinsiyet == "" and kangrubu == "" and cepno == "" and eposta == "" and parola == "" and adres == "" and klinik =="":
            cursor.execute("update doktor set dogumtarihi = %s where id = %s",(dogumtarihi,id))
            self.doktorbilgiler.statusbar.showMessage("Doğum Tarihi Başarıyla Güncellendi !")
            con.commit()
        elif kulladi == "" and tc == "" and ad == "" and soyad == "" and cinsiyet == "" and dogumtarihi == "" and cepno == "" and eposta == "" and parola == "" and adres == "" and klinik =="":
            cursor.execute("update doktor set kangrubu = %s where id = %s",(kangrubu,id))
            self.doktorbilgiler.statusbar.showMessage("Kan Grubu Başarıyla Güncellendi !")
            con.commit()
        elif kulladi == "" and tc == "" and ad == "" and soyad == "" and kangrubu == "" and dogumtarihi == "" and cepno == "" and eposta == "" and parola == "" and adres == "" and klinik =="":
            cursor.execute("update doktor set cinsiyet = %s where id = %s",(cinsiyet,id))
            self.doktorbilgiler.statusbar.showMessage("Cinsiyet Başarıyla Güncellendi !")
            con.commit()
        elif kulladi == "" and tc == "" and ad == "" and cinsiyet == "" and kangrubu == "" and dogumtarihi == "" and cepno == "" and eposta == "" and parola == "" and adres == "" and klinik =="":
            cursor.execute("update doktor set soyad = %s where id = %s",(soyad,id))
            self.doktorbilgiler.statusbar.showMessage("Soyad Başarıyla Güncellendi !")
            con.commit()
        elif kulladi == "" and tc == "" and soyad == "" and cinsiyet == "" and kangrubu == "" and dogumtarihi == "" and cepno == "" and eposta == "" and parola == "" and adres == "" and klinik =="":
            cursor.execute("update doktor set ad = %s where id = %s",(ad,id))
            self.doktorbilgiler.statusbar.showMessage("Ad Başarıyla Güncellendi !")
            con.commit()
        elif kulladi == "" and ad == "" and soyad == "" and cinsiyet == "" and kangrubu == "" and dogumtarihi == "" and cepno == "" and eposta == "" and parola == "" and adres == "" and klinik =="":
            cursor.execute("update doktor set tc = %s where id = %s",(tc,id))
            self.doktorbilgiler.statusbar.showMessage("T.C. Başarıyla Güncellendi !")
            con.commit()
        elif tc =="" and ad == "" and soyad == "" and cinsiyet == "" and kangrubu == "" and dogumtarihi == "" and cepno == "" and eposta == "" and parola == "" and adres == "" and klinik =="":
            cursor.execute("update doktor set kulladi = %s where id = %s",(kulladi,id))
            self.doktorbilgiler.statusbar.showMessage("Kullanıcı Adı Başarıyla Güncellendi !")
            con.commit()
        elif kulladi == "" and ad == "" and soyad == "" and cinsiyet == "" and kangrubu == "" and dogumtarihi == "" and cepno == "" and eposta == "" and parola == "" and adres == "" and klinik =="":
            cursor.execute("update doktor set klinik = %s where id = %s",(klinik,id))
            self.doktorbilgiler.statusbar.showMessage("Klinik Adı Başarıyla Güncellendi !")
            con.commit()
        else:
            cursor.execute("update doktor set tc = %s,ad = %s,soyad = %s,cinsiyet = %s,kangrubu = %s,klinik = %s,dogumtarihi =%s,eposta = %s,cepno =%s,kulladi=%s,parola =%s,adres =%s where id = %s",(tc,ad,soyad,cinsiyet,kangrubu,klinik,dogumtarihi,eposta,cepno,kulladi,parola,adres,id))
            self.doktorbilgiler.statusbar.showMessage("Bilgiler Başarıyla Güncellendi !")
            con.commit()
            self.doktorbilgiler.id.clear()
            self.doktorbilgiler.doktorkulladi.clear()
            self.doktorbilgiler.doktortc.clear()
            self.doktorbilgiler.doktoradi.clear()
            self.doktorbilgiler.doktorsoyadi.clear()
            self.doktorbilgiler.cinsiyet.clear()
            self.doktorbilgiler.kangrubu.clear()
            self.doktorbilgiler.dogumtarihi.clear()
            self.doktorbilgiler.cepno.clear()
            self.doktorbilgiler.eposta.clear()
            self.doktorbilgiler.yeniparola.clear()
            self.doktorbilgiler.doktoradres.clear()
            self.doktorbilgiler.doktorklinik.clear()




















         