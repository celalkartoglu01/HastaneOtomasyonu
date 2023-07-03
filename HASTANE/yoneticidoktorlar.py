from PyQt5.QtWidgets import *
from yonetici_doktorlar import Ui_MainWindow
import mysql.connector

con = mysql.connector.connect(user='root',password = '',host = 'localhost',database = 'hastane')
cursor = con.cursor()


class YoneticiDoktorlar(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.yoneticidoktorlar = Ui_MainWindow()
        self.yoneticidoktorlar.setupUi(self)
        self.yoneticidoktorlar.doktorekle.clicked.connect(self.DoktorEkle)
        self.yoneticidoktorlar.doktortemizle.clicked.connect(self.Temizle)
        self.yoneticidoktorlar.doktorara.clicked.connect(self.DoktorAra)
        self.yoneticidoktorlar.doktorgetir.clicked.connect(self.DoktorGetir)
        self.yoneticidoktorlar.doktorguncelle.clicked.connect(self.DoktorGuncelle)
    


    def DoktorAra(self):
        self.yoneticidoktorlar.yoneticidoktortablo.clear()
        tc = self.yoneticidoktorlar.doktortc.text()
        self.yoneticidoktorlar.yoneticidoktortablo.setHorizontalHeaderLabels(("id","TC","Ad","Soyad","Cinsiyet","Kan grubu","Klinik","Dogum tarihi","E-Posta","Cep no","Kulladi","Adres"))
        cursor.execute("select id,tc,ad,soyad,cinsiyet,kangrubu,klinik,dogumtarihi,eposta,cepno,kulladi,adres from doktor where tc = %s",(tc,))
        for indexSatir,kayitNumarasi in enumerate(cursor):
             for indexSutun,kayitSutun in enumerate(kayitNumarasi):
               self.yoneticidoktorlar.yoneticidoktortablo.setItem(indexSatir,indexSutun,QTableWidgetItem(str(kayitSutun)))
    

    def DoktorGetir(self):
        self.yoneticidoktorlar.yoneticidoktortablo.clear()
        self.yoneticidoktorlar.yoneticidoktortablo.setHorizontalHeaderLabels(("id","TC","Ad","Soyad","Cinsiyet","Kan grubu","Klinik","Dogum tarihi","E-Posta","Cep no","Kulladi","Adres"))
        query = "select id,tc,ad,soyad,cinsiyet,kangrubu,klinik,dogumtarihi,eposta,cepno,kulladi,adres from doktor"
        cursor.execute(query)
        for indexSatir,kayitNumarasi in enumerate(cursor):
            for indexSutun,kayitSutun in enumerate(kayitNumarasi):
               self.yoneticidoktorlar.yoneticidoktortablo.setItem(indexSatir,indexSutun,QTableWidgetItem(str(kayitSutun)))
    

    def DoktorEkle(self):
        tc = self.yoneticidoktorlar.doktortc2.text()
        ad = self.yoneticidoktorlar.doktoradi.text()
        soyad = self.yoneticidoktorlar.doktorsoyadi.text()
        cinsiyet = self.yoneticidoktorlar.cinsiyet.text()
        kangrubu = self.yoneticidoktorlar.kangrubu.text()
        klinik = self.yoneticidoktorlar.doktoryeniklinik.text()
        dogumtarihi = self.yoneticidoktorlar.doktordogumtarih.text()
        eposta = self.yoneticidoktorlar.doktoreposta.text()
        cepno = self.yoneticidoktorlar.cepno.text()
        kulladi = self.yoneticidoktorlar.doktorkulladi.text()
        parola = self.yoneticidoktorlar.yeniparola.text()
        adres = self.yoneticidoktorlar.adres.text()
        query = "Insert into doktor(tc,ad,soyad,cinsiyet,kangrubu,klinik,dogumtarihi,eposta,cepno,kulladi,parola,adres) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(query,(tc,ad,soyad,cinsiyet,kangrubu,klinik,dogumtarihi,eposta,cepno,kulladi,parola,adres))
        con.commit()
        cursor.close()
        self.yoneticidoktorlar.statusbar.showMessage("Doktor Başarıyla Eklendi !")
    

    def DoktorGuncelle(self):
       tc = self.yoneticidoktorlar.doktortc2.text()
       ad = self.yoneticidoktorlar.doktoradi.text()
       soyad = self.yoneticidoktorlar.doktorsoyadi.text()
       cinsiyet = self.yoneticidoktorlar.cinsiyet.text()
       kangrubu = self.yoneticidoktorlar.kangrubu.text()
       klinik = self.yoneticidoktorlar.klinik.text()
       dogumtarihi = self.yoneticidoktorlar.doktordogumtarih.text()
       eposta = self.yoneticidoktorlar.doktoreposta.text()
       cepno = self.yoneticidoktorlar.cepno.text()
       kulladi = self.yoneticidoktorlar.doktorkulladi.text()
       parola = self.yoneticidoktorlar.eskiparola.text()
       adres = self.yoneticidoktorlar.adres.text()
       id = self.yoneticidoktorlar.id.text()

       if tc == "" and ad == "" and soyad == "" and cinsiyet == "" and kangrubu == "" and klinik == "" and dogumtarihi == "" and eposta == "" and cepno == "" and kulladi == "" and parola == "":
            cursor.execute("update doktor set adres = %s where id = %s",(adres,id))
            self.yoneticidoktorlar.statusbar.showMessage("Adres Başarıyla Güncellendi !")
            con.commit()

       elif tc == "" and ad == "" and soyad == "" and cinsiyet == "" and kangrubu == "" and klinik == "" and dogumtarihi == "" and eposta == "" and kulladi == "" and adres == "" and parola == "":
            cursor.execute("update doktor set cepno = %s where id = %s",(cepno,id))
            self.yoneticidoktorlar.statusbar.showMessage("Cep No Başarıyla Güncellendi !")
            con.commit()

       elif tc == "" and ad == "" and soyad == "" and cinsiyet == "" and kangrubu == "" and klinik == "" and dogumtarihi == "" and cepno == "" and adres == "" and kulladi == "" and parola == "":
           cursor.execute("update doktor set eposta = %s where id = %s",(eposta,id))
           con.commit()

       elif tc == "" and ad == "" and soyad == "" and cinsiyet == "" and kangrubu == "" and klinik == "" and dogumtarihi == "" and eposta == "" and cepno == "" and adres == "" and kulladi == "":
            cursor.execute("update doktor set parola = %s where id = %s",(parola,id))
            self.yoneticidoktorlar.statusbar.showMessage("Parola Başarıyla Güncellendi !")
            con.commit()

       elif tc == "" and ad == "" and soyad == "" and cinsiyet == "" and kangrubu == "" and klinik == "" and dogumtarihi == "" and eposta == "" and cepno == "" and adres == "" and parola == "":
            cursor.execute("update doktor set kulladi = %s where id = %s",(kulladi,id))
            self.yoneticidoktorlar.statusbar.showMessage("Kullanıcı Adı Başarıyla Güncellendi !")
            con.commit()

       elif tc == "" and ad == "" and soyad == "" and cinsiyet == "" and kangrubu == "" and dogumtarihi == "" and eposta == "" and kulladi == "" and cepno == "" and adres == "" and parola == "":
            cursor.execute("update doktor set klinik = %s where id = %s",(klinik,id))
            self.yoneticidoktorlar.statusbar.showMessage("Klinik Başarıyla Güncellendi !")
            con.commit()

       elif tc == "" and ad == "" and soyad == "" and cinsiyet == "" and kangrubu == "" and klinik == "" and eposta == "" and kulladi == "" and cepno == "" and adres == "" and parola == "":
            cursor.execute("update doktor set dogumtarihi = %s where id = %s",(dogumtarihi,id))
            self.yoneticidoktorlar.statusbar.showMessage("Doğum Tarihi Başarıyla Güncellendi !")
            con.commit()

       elif tc == "" and ad == "" and soyad == "" and cinsiyet == "" and klinik == "" and dogumtarihi == "" and eposta == "" and kulladi == "" and cepno == "" and adres == "" and parola == "":
        
            cursor.execute("update doktor set kangrubu = %s where id = %s",(kangrubu,id))
            self.yoneticidoktorlar.statusbar.showMessage("Kan Grubu Başarıyla Güncellendi !")
            con.commit()

       elif tc == "" and ad == "" and soyad == "" and kangrubu == "" and klinik == "" and dogumtarihi == "" and eposta == "" and kulladi == "" and cepno == "" and adres == "" and parola == "":
            cursor.execute("update doktor set cinsiyet = %s where id = %s",(cinsiyet,id))
            self.yoneticidoktorlar.statusbar.showMessage("Cinsiyet Başarıyla Güncellendi !")
            con.commit()

       elif tc == "" and ad == "" and cinsiyet == "" and kangrubu == "" and klinik == "" and dogumtarihi == "" and eposta == "" and kulladi == "" and cepno == "" and adres == "" and parola == "":
            cursor.execute("update doktor set soyad = %s where id = %s",(soyad,id))
            self.yoneticidoktorlar.statusbar.showMessage("Soyad Başarıyla Güncellendi !")
            con.commit()

       elif tc == "" and soyad == "" and cinsiyet == "" and kangrubu == "" and klinik == "" and dogumtarihi == "" and eposta == "" and kulladi == "" and cepno == "" and adres == "" and parola:
            cursor.execute("update doktor set ad = %s where id = %s",(ad,id))
            self.yoneticidoktorlar.statusbar.showMessage("Ad Başarıyla Güncellendi !")
            con.commit()

       elif ad == "" and soyad == "" and cinsiyet == "" and kangrubu == "" and klinik == "" and dogumtarihi == "" and eposta == "" and kulladi == "" and cepno == "" and adres == "" and parola == "":
            cursor.execute("update doktor set tc = %s where id = %s",(tc,id))
            self.yoneticidoktorlar.statusbar.showMessage("T.C. Başarıyla Güncellendi !")
            con.commit()

       else:
            cursor.execute("update hasta set tc = %s,ad = %s,soyad = %s,cinsiyet = %s,kangrubu = %s,klinik = %s,dogumtarihi = %s,eposta = %s,kulladi = %s,cepno = %s,adres = %s,parola = %s where id = %s",(tc,ad,soyad,cinsiyet,kangrubu,klinik,dogumtarihi,eposta,kulladi,cepno,adres,parola,id))
            self.yoneticidoktorlar.statusbar.showMessage("Bilgiler Başarıyla Güncellendi !")
            con.commit()
            self.Temizle()
    

    
    def Temizle(self):
        self.yoneticidoktorlar.doktortc.clear()
        self.yoneticidoktorlar.doktortc2.clear()
        self.yoneticidoktorlar.doktoradi.clear()
        self.yoneticidoktorlar.doktorsoyadi.clear()
        self.yoneticidoktorlar.doktoreposta.clear()
        self.yoneticidoktorlar.doktordogumtarih.clear()
        self.yoneticidoktorlar.cepno.clear()
        self.yoneticidoktorlar.eskiparola.clear()
        self.yoneticidoktorlar.yeniparola.clear()
        self.yoneticidoktorlar.adres.clear()
        self.yoneticidoktorlar.id.clear()

