from PyQt5.QtWidgets import *
from hasta_recete import Ui_MainWindow
import mysql.connector

con = mysql.connector.connect(user='root',password = '',host = 'localhost',database = 'hastane')
cursor = con.cursor()


class HastaRecete(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.hastareceteler = Ui_MainWindow()
        self.hastareceteler.setupUi(self)
        self.hastareceteler.ara.clicked.connect(self.Ara)
        self.hastareceteler.receteyazdir.clicked.connect(self.Yazdir)
    

    def Ara(self):
        ad = self.hastareceteler.hastaad.text()
        query = "select * from recete where hastaad = %s"
        cursor.execute(query,(ad,))
        for indexSatir,kayitNumarasi in enumerate(cursor):
            for indexSutun,kayitSutun in enumerate(kayitNumarasi):
               self.hastareceteler.tahliller.setItem(indexSatir,indexSutun,QTableWidgetItem(str(kayitSutun)))

    def Yazdir(self):
        secilen = self.hastareceteler.tahliller.selectedItems()
        yazdirilacak = secilen[0].text()
        self.hastareceteler.statusbar.showMessage("Reçeteniz : " + str(yazdirilacak))