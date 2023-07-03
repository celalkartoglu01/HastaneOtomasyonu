from PyQt5.QtWidgets import *
from yonetici_klinikler import Ui_MainWindow
import mysql.connector

con = mysql.connector.connect(user='root',password = '',host = 'localhost',database = 'hastane')
cursor = con.cursor()



class YoneticiKlinikler(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.yoneticiklinikler = Ui_MainWindow()
        self.yoneticiklinikler.setupUi(self)
        self.yoneticiklinikler.klinikgetir.clicked.connect(self.KlinikGetir)
        self.yoneticiklinikler.klinikgetir.clicked.connect(self.KlinikAra)
        self.yoneticiklinikler.temizle.clicked.connect(self.Temizle)
        self.yoneticiklinikler.ekle.clicked.connect(self.Ekle)
        self.yoneticiklinikler.sil.clicked.connect(self.Sil)
        self.yoneticiklinikler.guncelle.clicked.connect(self.Guncelle)
    

    def Guncelle(self):
        klinikid = self.yoneticiklinikler.klinikid2.text()
        klinikad = self.yoneticiklinikler.klinikadi.text()
        doktoradsoyad = self.yoneticiklinikler.doktoradisoyadi.text()
        
        if klinikad == "":
            cursor.execute("update klinikler set ad = %s where id = %s",(klinikad,klinikid))
            self.yoneticiklinikler.statusbar.showMessage("Klinik Adı Başarıyla Güncellendi !")
            con.commit()
        elif doktoradsoyad == "":
            cursor.execute("update klinikler set doktor = %s where id = %s",(doktoradsoyad,klinikid))
            self.yoneticiklinikler.statusbar.showMessage("Doktor Adı Soyadı Başarıyla Güncellendi !")
            con.commit()
        else:
            cursor.execute("update klinikler set ad = %s,doktor = %s where id = %s",(klinikad,doktoradsoyad,klinikid))
            self.yoneticiklinikler.statusbar.showMessage("Bilgiler Başarıyla Güncellendi !")
            con.commit()
            self.Temizle()

    
    def Ekle(self):
        klinikad = self.yoneticiklinikler.klinikadi.text()
        doktoradsoyad = self.yoneticiklinikler.doktoradisoyadi.text()
        query = "Insert into klinikler(ad,doktor) VALUES(%s,%s)"
        cursor.execute(query,(klinikad,doktoradsoyad))
        con.commit()
        cursor.close()
        self.yoneticiklinikler.statusbar.showMessage("Başarıyla Eklendi !")
    

    def Sil(self):
        id = self.yoneticiklinikler.klinikid2.text()
        query = "delete from klinikler where id = %s"
        cursor.execute(query,(id,))
        con.commit()
        self.yoneticiklinikler.statusbar.showMessage("Başarıyla Silindi !")

    

    def Temizle(self):
        self.yoneticiklinikler.klinikid.clear()
        self.yoneticiklinikler.klinikadi.clear()
        self.yoneticiklinikler.klinikid2.clear()
        self.yoneticiklinikler.doktoradisoyadi.clear()

    

    def KlinikAra(self):
        self.yoneticiklinikler.klinikler.clear()
        id = self.yoneticiklinikler.klinikid.text()
        self.yoneticiklinikler.klinikler.setHorizontalHeaderLabels(("klinik_id","klinikadi","doktoradisoyadi"))
        query = "Select id,ad,doktor from klinikler where id = %s"
        cursor.execute(query,(id,))
        for indexSatir,kayitNumarasi in enumerate(cursor):
            for indexSutun,kayitSutun in enumerate(kayitNumarasi):
               self.yoneticiklinikler.klinikler.setItem(indexSatir,indexSutun,QTableWidgetItem(str(kayitSutun)))

    

    def KlinikGetir(self):
        self.yoneticiklinikler.klinikler.clear()
        self.yoneticiklinikler.klinikler.setHorizontalHeaderLabels(("klinik_id","klinikadi","doktoradisoyadi"))
        query = "Select id,ad,doktor from klinikler"
        cursor.execute(query)
        for indexSatir,kayitNumarasi in enumerate(cursor):
            for indexSutun,kayitSutun in enumerate(kayitNumarasi):
               self.yoneticiklinikler.klinikler.setItem(indexSatir,indexSutun,QTableWidgetItem(str(kayitSutun)))


        