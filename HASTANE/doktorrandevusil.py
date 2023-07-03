from PyQt5.QtWidgets import *
from doktor_randevu_sil import Ui_MainWindow
import mysql.connector

con = mysql.connector.connect(user='root',password = '',host = 'localhost',database = 'hastane')
cursor = con.cursor()


class RandevuSil(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.randevusil = Ui_MainWindow()
        self.randevusil.setupUi(self)
        self.randevusil.hastaara.clicked.connect(self.HastaAra)
        self.randevusil.randevusil.clicked.connect(self.RandevuSil)
    
    def HastaAra(self):
        id = self.randevusil.hastaid.text()
        query = "select * from randevu where hastaid =%s"
        cursor.execute(query,(id,))
        for indexSatir,kayitNumarasi in enumerate(cursor):
            for indexSutun,kayitSutun in enumerate(kayitNumarasi):
               self.randevusil.randevular.setItem(indexSatir,indexSutun,QTableWidgetItem(str(kayitSutun)))
               self.randevusil.hastaid.clear()
    
    def RandevuSil(self):
        id = self.randevusil.hastaid.text()
        query = "delete from randevu where hastaid = %s"
        cursor.execute(query,(id,))
        con.commit()
        self.randevusil.statusbar.showMessage("Randevu Silindi !")
        self.randevusil.hastaid.clear()
        self.randevusil.randevular.clear()
