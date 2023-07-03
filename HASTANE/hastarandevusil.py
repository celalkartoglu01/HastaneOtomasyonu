from PyQt5.QtWidgets import *
from hasta_randevu_sil import Ui_MainWindow
import mysql.connector

con = mysql.connector.connect(user='root',password = '',host = 'localhost',database = 'hastane')
cursor = con.cursor()



class HastaRandevuSil(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.randevusil = Ui_MainWindow()
        self.randevusil.setupUi(self)
        self.randevusil.randevuara.clicked.connect(self.RandevuAra)
        self.randevusil.randevusil.clicked.connect(self.RandevuSil)
    
    def RandevuAra(self):
        id = self.randevusil.hastaid.text()
        query = "select * from randevu where hastaid = %s"
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
        self.randevusil.randevular.clear()
        self.randevusil.hastaid.clear()
        self.randevusil.statusbar.showMessage("Randevunuz Silindi !")