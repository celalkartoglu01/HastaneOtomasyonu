from PyQt5.QtWidgets import *
from hasta_randevu import Ui_MainWindow
import mysql.connector

con = mysql.connector.connect(user='root',password = '',host = 'localhost',database = 'hastane')
cursor = con.cursor()


class HastaRandevu(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.hastarandevular = Ui_MainWindow()
        self.hastarandevular.setupUi(self)
        self.hastarandevular.randevuara.clicked.connect(self.RandevuAra)
    
    def RandevuAra(self):
        id = self.hastarandevular.hastaid.text()
        query = "select * from randevu where hastaid = %s"
        cursor.execute(query,(id,))
        for indexSatir,kayitNumarasi in enumerate(cursor):
            for indexSutun,kayitSutun in enumerate(kayitNumarasi):
               self.hastarandevular.randevular.setItem(indexSatir,indexSutun,QTableWidgetItem(str(kayitSutun)))