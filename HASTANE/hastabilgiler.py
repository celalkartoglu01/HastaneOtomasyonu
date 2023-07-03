from PyQt5.QtWidgets import *
from hasta_bilgiler import Ui_MainWindow
import mysql.connector

con = mysql.connector.connect(user='root',password = '',host = 'localhost',database = 'hastane')
cursor = con.cursor()


class HastaBilgiler(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.hastabilgileri = Ui_MainWindow()
        self.hastabilgileri.setupUi(self)
        self.hastabilgileri.guncelle.clicked.connect(self.Guncelle)
    
    def Guncelle(self):
        id = self.hastabilgileri.id.text()
        kulladi = self.hastabilgileri.hastakulladi.text()
        tc = self.hastabilgileri.hastatc.text()
        ad = self.hastabilgileri.hastaadi.text()
        cinsiyet = self.hastabilgileri.cinsiyet.text()
        kangrubu = self.hastabilgileri.kangrubu.text()
        dogumtarihi = self.hastabilgileri.dogumtarihi.text()
        cepno = self.hastabilgileri.cepno.text()
        eposta = self.hastabilgileri.eposta.text()
        parola1 = self.hastabilgileri.yeniparola.text()
        adres = self.hastabilgileri.hastaadres.text()
        dogumyerii = self.hastabilgileri.dogumyeri.text()
        soyad = self.hastabilgileri.hastasoyadi.text()

        if kulladi == "" and ad == "" and cinsiyet ==  "" and kangrubu == "" and dogumtarihi == "" and cepno == "" and eposta == "" and parola1 == "" and tc == "" and dogumyerii == "" and soyad == "":
            cursor.execute("update hasta set adres = %s where id = %s",(adres,id))
            self.hastabilgileri.statusbar.showMessage("Adres Başarıyla Güncellendi !")
            con.commit()
        elif kulladi == "" and ad == "" and cinsiyet ==  "" and kangrubu == "" and dogumtarihi == "" and cepno == "" and eposta == "" and adres == "" and tc == "" and dogumyerii == "" and soyad == "":
            cursor.execute("update hasta set parola = %s where id = %s",(parola1,id))
            self.hastabilgileri.statusbar.showMessage("Parola Başarıyla Güncellendi !")
            con.commit()
        elif kulladi == "" and ad == "" and cinsiyet ==  "" and kangrubu == "" and dogumtarihi == "" and cepno == "" and parola1 == "" and adres == "" and tc == "" and dogumyerii == "" and soyad == "":
            cursor.execute("update hasta set eposta = %s where id = %s",(eposta,id))
            self.hastabilgileri.statusbar.showMessage("E-Posta Başarıyla Güncellendi !")
            con.commit()
        elif kulladi == "" and ad == "" and cinsiyet ==  "" and kangrubu == "" and dogumtarihi == "" and eposta == "" and parola1 == "" and adres == "" and tc == "" and dogumyerii == "" and soyad =="":
            cursor.execute("update hasta set cepno = %s where id = %s",(cepno,id))
            self.hastabilgileri.statusbar.showMessage("Cep No. Başarıyla Güncellendi !")
            con.commit()
        elif kulladi == "" and ad == "" and cinsiyet ==  "" and kangrubu == "" and cepno == "" and eposta == "" and parola1 == "" and adres == "" and tc == "" and dogumyerii =="" and soyad =="":
            cursor.execute("update hasta set dogumtarihi = %s where id = %s",(dogumtarihi,id))
            self.hastabilgileri.statusbar.showMessage("Doğum Tarihi Başarıyla Güncellendi !")
            con.commit()
        elif kulladi == "" and ad == "" and cinsiyet ==  "" and dogumtarihi == "" and cepno == "" and eposta == "" and parola1 == "" and adres == "" and tc == "" and dogumyerii == "" and soyad == "":
            cursor.execute("update hasta set kangrubu = %s where id = %s",(kangrubu,id))
            self.hastabilgileri.statusbar.showMessage("Kan Grubu Başarıyla Güncellendi !")
            con.commit()
        elif kulladi == "" and ad == "" and kangrubu ==  "" and dogumtarihi == "" and cepno == "" and eposta == "" and parola1 == "" and adres == "" and tc == "" and dogumyerii == "" and soyad == "":
            cursor.execute("update hasta set cinsiyet = %s where id = %s",(cinsiyet,id))
            self.hastabilgileri.statusbar.showMessage("Cinsiyet Başarıyla Güncellendi !")
            con.commit()
        elif kulladi == "" and cinsiyet == "" and kangrubu ==  "" and dogumtarihi == "" and cepno == "" and eposta == "" and parola1 == "" and adres == "" and tc == "" and dogumyerii == "" and soyad == "":
            cursor.execute("update hasta set ad = %s where id = %s",(ad,id))
            self.hastabilgileri.statusbar.showMessage("Ad Başarıyla Güncellendi !")
            con.commit()
        elif kulladi == "" and cinsiyet == "" and kangrubu ==  "" and dogumtarihi == "" and cepno == "" and eposta == "" and parola1 == "" and adres == "" and ad == "" and dogumyerii == "" and soyad == "":
            cursor.execute("update hasta set tc = %s where id = %s",(tc,id))
            self.hastabilgileri.statusbar.showMessage("TC Başarıyla Güncellendi !")
            con.commit()
        elif tc == "" and cinsiyet == "" and kangrubu == "" and dogumtarihi == "" and cepno == "" and eposta == "" and parola1 == "" and adres == "" and ad == "" and kulladi == "" and soyad == "":
            cursor.execute("update hasta set dogumyeri = %s where id = %s",(dogumyerii,id))
            self.hastabilgileri.statusbar.showMessage("Doğum Yeri Başarıyla Güncellendi !")
            con.commit()
        elif tc == "" and cinsiyet == "" and kangrubu == "" and dogumtarihi == "" and cepno == "" and eposta == "" and parola1 == "" and adres == "" and ad == "" and dogumyerii == "" and soyad == "":
            cursor.execute("update hasta set kulladi = %s where id = %s",(kulladi,id))
            self.hastabilgileri.statusbar.showMessage("Kullanıcı Adı Başarıyla Güncellendi !")
            con.commit()
        elif tc == "" and cinsiyet == "" and kangrubu == "" and dogumtarihi == "" and cepno == "" and eposta == "" and parola1 == "" and adres == "" and ad == "" and dogumyerii == "" and kulladi == "":
            cursor.execute("update hasta set soyad = %s where id = %s",(soyad,id))
            self.hastabilgileri.statusbar.showMessage("Soyad Başarıyla Güncellendi !")
            con.commit()
        else:
            cursor.execute("update hasta set tc = %s,ad = %s,soyad = %s,cinsiyet = %s,kangrubu = %s,dogumyeri = %s,dogumtarihi = %s,cepno = %s,eposta = %s,parola = %s,adres = %s,kulladi = %s where id = %s",(tc,ad,soyad,cinsiyet,kangrubu,dogumyerii,dogumtarihi,cepno,eposta,parola1,adres,kulladi,id))
            self.hastabilgileri.statusbar.showMessage("Bilgiler Başarıyla Güncellendi !")
            con.commit()

