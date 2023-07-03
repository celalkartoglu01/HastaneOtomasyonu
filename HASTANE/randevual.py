from PyQt5.QtWidgets import *
from randevu_al import Ui_MainWindow
import mysql.connector

con = mysql.connector.connect(user='root',password = '',host = 'localhost',database = 'hastane')
cursor = con.cursor()


class RandevuAl(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.randevu = Ui_MainWindow()
        self.randevu.setupUi(self)
        self.randevu.randevual.clicked.connect(self.RandevuAl)
    
    def RandevuAl(self):
        id = self.randevu.hastaid.text()
        klinik = self.randevu.randevuklinik.currentText()
        doktor = self.randevu.randevudoktor.currentText()
        tarih = str(self.randevu.tarih.selectedDate().toPyDate())
        saat = self.randevu.saat.currentText()
        query = "Insert into randevu(hastaid,klinik,doktor,tarih,saat) VALUES(%s,%s,%s,%s,%s)"
        cursor.execute(query,(id,klinik,doktor,tarih,saat))
        con.commit()
        self.randevu.statusbar.showMessage("Randevunuz Alındı !")
        self.randevu.hastaid.clear()
        