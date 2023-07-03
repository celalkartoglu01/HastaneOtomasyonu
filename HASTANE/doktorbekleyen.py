from PyQt5.QtWidgets import *
from doktor_bekleyen import Ui_MainWindow
import mysql.connector

con = mysql.connector.connect(user='root',password = '',host = 'localhost',database = 'hastane')
cursor = con.cursor()


class DoktorBekleyen(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.doktorbekleyen = Ui_MainWindow()
        self.doktorbekleyen.setupUi(self)
        self.doktorbekleyen.hastagetir.clicked.connect(self.HastaGetir)
    
    def HastaGetir(self):
        id = self.doktorbekleyen.hastaid.text()
        query = "select id,tc,ad,soyad,muayeneklinik,muayenedoktor from muayene where id = %s"
        cursor.execute(query,(id,))
        for indexSatir,kayitNumarasi in enumerate(cursor):
            for indexSutun,kayitSutun in enumerate(kayitNumarasi):
               self.doktorbekleyen.bekleyenhastalar.setItem(indexSatir,indexSutun,QTableWidgetItem(str(kayitSutun)))
               self.doktorbekleyen.hastaid.clear()