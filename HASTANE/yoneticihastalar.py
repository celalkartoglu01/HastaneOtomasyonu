from PyQt5.QtWidgets import *
from yonetici_hastalar import Ui_MainWindow
import mysql.connector

con = mysql.connector.connect(user='root',password = '',host = 'localhost',database = 'hastane')
cursor = con.cursor()


class YoneticiHastalar(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.yoneticihasta = Ui_MainWindow()
        self.yoneticihasta.setupUi(self)
        self.yoneticihasta.hastagetir.clicked.connect(self.HastaGetir)
        self.yoneticihasta.hastaara.clicked.connect(self.HastaAra)
        self.yoneticihasta.hastatemizle.clicked.connect(self.Temizle)
        self.yoneticihasta.hastaguncelle.clicked.connect(self.HastaGuncelle)
    

    def HastaGuncelle(self):
        tc = self.yoneticihasta.hastatc2.text()
        ad = self.yoneticihasta.hastaadi.text()
        soyad = self.yoneticihasta.hastasoyadi.text()
        cinsiyet = self.yoneticihasta.cinsiyet.text()
        kangrubu = self.yoneticihasta.kangrubu.text()
        dogumyeri = self.yoneticihasta.dogumyeri.text()
        dogumtarihi = self.yoneticihasta.dogumtarihi.text()
        babaadi = self.yoneticihasta.babaadi.text()
        anaadi = self.yoneticihasta.anaadi.text()
        cepno = self.yoneticihasta.cepno.text()
        adres = self.yoneticihasta.adres.text()
        id = self.yoneticihasta.id.text()

        if tc == "" and ad == "" and soyad == "" and cinsiyet == "" and kangrubu == "" and dogumyeri == "" and dogumtarihi == "" and babaadi == "" and anaadi == "" and cepno == "":
            cursor.execute("update hasta set adres = %s where id = %s",(adres,id))
            self.yoneticihasta.statusbar.showMessage("Adres Başarıyla Güncellendi !")
            con.commit()

        elif tc == "" and ad == "" and soyad == "" and cinsiyet == "" and kangrubu == "" and dogumyeri == "" and dogumtarihi == "" and babaadi == "" and anaadi == "" and adres == "":
            cursor.execute("update hasta set cepno = %s where id = %s",(cepno,id))
            self.yoneticihasta.statusbar.showMessage("Cep No Başarıyla Güncellendi !")
            con.commit()

        elif tc == "" and ad == "" and soyad == "" and cinsiyet == "" and kangrubu == "" and dogumyeri == "" and dogumtarihi == "" and babaadi == "" and cepno == "" and adres == "":
            cursor.execute("update hasta set anaadi = %s where id = %s",(anaadi,id))
            self.yoneticihasta.statusbar.showMessage("Anne Adı Başarıyla Güncellendi !")
            con.commit()

        elif tc == "" and ad == "" and soyad == "" and cinsiyet == "" and kangrubu == "" and dogumyeri == "" and dogumtarihi == "" and anaadi == "" and cepno == "" and adres == "":
            cursor.execute("update hasta set babaadi = %s where id = %s",(babaadi,id))
            self.yoneticihasta.statusbar.showMessage("Baba Adı Başarıyla Güncellendi !")
            con.commit()

        elif tc == "" and ad == "" and soyad == "" and cinsiyet == "" and kangrubu == "" and dogumyeri == "" and babaadi == "" and anaadi == "" and cepno == "" and adres == "":
            cursor.execute("update hasta set dogumtarihi = %s where id = %s",(dogumtarihi,id))
            self.yoneticihasta.statusbar.showMessage("Doğum Tarihi Başarıyla Güncellendi !")
            con.commit()

        elif tc == "" and ad == "" and soyad == "" and cinsiyet == "" and kangrubu == "" and dogumtarihi == "" and babaadi == "" and anaadi == "" and cepno == "" and adres == "":
            cursor.execute("update hasta set dogumyeri = %s where id = %s",(dogumyeri,id))
            self.yoneticihasta.statusbar.showMessage("Doğum Yeri Başarıyla Güncellendi !")
            con.commit()

        elif tc == "" and ad == "" and soyad == "" and cinsiyet == "" and dogumyeri == "" and dogumtarihi == "" and babaadi == "" and anaadi == "" and cepno == "" and adres == "":
            cursor.execute("update hasta set kangrubu = %s where id = %s",(kangrubu,id))
            self.yoneticihasta.statusbar.showMessage("Kan Grubu Başarıyla Güncellendi !")
            con.commit()

        elif tc == "" and ad == "" and soyad == "" and kangrubu == "" and dogumyeri == "" and dogumtarihi == "" and babaadi == "" and anaadi == "" and cepno == "" and adres == "":
            cursor.execute("update hasta set cinsiyet = %s where id = %s",(cinsiyet,id))
            self.yoneticihasta.statusbar.showMessage("Cinsiyet Başarıyla Güncellendi !")
            con.commit()

        elif tc == "" and ad == "" and cinsiyet == "" and kangrubu == "" and dogumyeri == "" and dogumtarihi == "" and babaadi == "" and anaadi == "" and cepno == "" and adres == "":
            cursor.execute("update hasta set soyad = %s where id = %s",(soyad,id))
            self.yoneticihasta.statusbar.showMessage("Soyad Başarıyla Güncellendi !")
            con.commit()

        elif tc == "" and soyad == "" and cinsiyet == "" and kangrubu == "" and dogumyeri == "" and dogumtarihi == "" and babaadi == "" and anaadi == "" and cepno == "" and adres == "":
            cursor.execute("update hasta set ad = %s where id = %s",(ad,id))
            self.yoneticihasta.statusbar.showMessage("Ad Başarıyla Güncellendi !")
            con.commit()

        elif ad == "" and soyad == "" and cinsiyet == "" and kangrubu == "" and dogumyeri == "" and dogumtarihi == "" and babaadi == "" and anaadi == "" and cepno == "" and adres == "":
            cursor.execute("update hasta set tc = %s where id = %s",(tc,id))
            self.yoneticihasta.statusbar.showMessage("T.C. Başarıyla Güncellendi !")
            con.commit()

        else:
            cursor.execute("update hasta set tc = %s,ad = %s,soyad = %s,cinsiyet = %s,kangrubu = %s,dogumyeri = %s,dogumtarihi = %s,babaadi = %s,anaadi = %s,cepno = %s,adres = %s where id = %s",(tc,ad,soyad,cinsiyet,kangrubu,dogumyeri,dogumtarihi,babaadi,anaadi,cepno,adres,id))
            self.yoneticihasta.statusbar.showMessage("Bilgiler Başarıyla Güncellendi !")
            con.commit()
            self.Temizle()


    def Temizle(self):
        self.yoneticihasta.hastatc.clear()
        self.yoneticihasta.hastatc2.clear()
        self.yoneticihasta.hastaadi.clear()
        self.yoneticihasta.hastasoyadi.clear()
        self.yoneticihasta.cinsiyet.clear()
        self.yoneticihasta.kangrubu.clear()
        self.yoneticihasta.dogumyeri.clear()
        self.yoneticihasta.dogumtarihi.clear()
        self.yoneticihasta.babaadi.clear()
        self.yoneticihasta.anaadi.clear()
        self.yoneticihasta.cepno.clear()
        self.yoneticihasta.adres.clear()
        self.yoneticihasta.id.clear()

    
    def HastaAra(self):
        self.yoneticihasta.yoneticihastatablo.clear()
        tc = self.yoneticihasta.hastatc.text()
        self.yoneticihasta.yoneticihastatablo.setHorizontalHeaderLabels(("id","TC","Ad","Soyad","Cinsiyet","Kan grubu","Dogum yeri","Dogum tarihi","Baba adi","Ana adi","Cep no","E posta","Kulladi","Adres"))
        cursor.execute("select id,tc,ad,soyad,cinsiyet,kangrubu,dogumyeri,dogumtarihi,babaadi,anaadi,cepno,eposta,kulladi,adres from hasta where tc = %s",(tc,))
        for indexSatir,kayitNumarasi in enumerate(cursor):
             for indexSutun,kayitSutun in enumerate(kayitNumarasi):
               self.yoneticihasta.yoneticihastatablo.setItem(indexSatir,indexSutun,QTableWidgetItem(str(kayitSutun)))
    

    def HastaGetir(self):
        self.yoneticihasta.yoneticihastatablo.clear()
        self.yoneticihasta.yoneticihastatablo.setHorizontalHeaderLabels(("id","TC","Ad","Soyad","Cinsiyet","Kan grubu","Dogum yeri","Dogum tarihi","Baba adi","Ana adi","Cep no","E posta","Kulladi","Adres"))
        query = "Select id,tc,ad,soyad,cinsiyet,kangrubu,dogumyeri,dogumtarihi,babaadi,anaadi,cepno,eposta,kulladi,adres from hasta"
        cursor.execute(query)
        for indexSatir,kayitNumarasi in enumerate(cursor):
            for indexSutun,kayitSutun in enumerate(kayitNumarasi):
               self.yoneticihasta.yoneticihastatablo.setItem(indexSatir,indexSutun,QTableWidgetItem(str(kayitSutun)))
