from PyQt5.QtWidgets import *
from doktor_tahliller import Ui_MainWindow
import mysql.connector

con = mysql.connector.connect(user='root',password = '',host = 'localhost',database = 'hastane')
cursor = con.cursor()


class DoktorTahliller(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.tahliller = Ui_MainWindow()
        self.tahliller.setupUi(self)
        self.tahliller.ara.clicked.connect(self.Ara)
        self.tahliller.sil.clicked.connect(self.Sil)
        self.tahliller.gonder.clicked.connect(self.Gonder)
    
    def Gonder(self):
        doktor = self.tahliller.doktoradsoyad.text()
        ad = self.tahliller.hastaadi.text()
        soyad = self.tahliller.hastasoyadi.text()
        tani = self.tahliller.tani.text()
        recete = self.tahliller.recete.text()
        query = "Insert into recete(doktoradsoyad,hastaad,hastasoyad,tani,recete) VALUES(%s,%s,%s,%s,%s)"
        cursor.execute(query,(doktor,ad,soyad,tani,recete))
        con.commit()
        self.tahliller.statusbar.showMessage("Sonuçlar Gönderildi !")
        self.tahliller.doktoradsoyad.clear()
        self.tahliller.hastaadi.clear()
        self.tahliller.hastasoyadi.clear()
        self.tahliller.tani.clear()
        self.tahliller.recete.clear()
    

    def Sil(self):
        id = self.tahliller.testid.text()
        query = "delete from tahlil where testid = %s"
        cursor.execute(query,(id,))
        con.commit()
        self.tahliller.statusbar.showMessage("Test Silindi !")
        self.tahliller.testid.clear()
        self.tahliller.tahliller.clear()


    def Ara(self):
        id = self.tahliller.testid.text()
        query = "select * from tahlil where testid = %s"
        cursor.execute(query,(id,))
        for indexSatir,kayitNumarasi in enumerate(cursor):
            for indexSutun,kayitSutun in enumerate(kayitNumarasi):
               self.tahliller.tahliller.setItem(indexSatir,indexSutun,QTableWidgetItem(str(kayitSutun)))
        self.tahliller.testid.clear()