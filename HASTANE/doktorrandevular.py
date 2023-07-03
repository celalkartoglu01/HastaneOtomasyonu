from PyQt5.QtWidgets import *
from doktor_randevular import Ui_MainWindow
import mysql.connector

con = mysql.connector.connect(user='root',password = '',host = 'localhost',database = 'hastane')
cursor = con.cursor()


class DoktorRandevular(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.doktorrandevular = Ui_MainWindow()
        self.doktorrandevular.setupUi(self)
        self.doktorrandevular.randevuara.clicked.connect(self.Ara)

    def Ara(self):
        ad = self.doktorrandevular.doktoradi.text()
        query = "select * from randevu where doktor = %s"
        cursor.execute(query,(ad,))
        for indexSatir,kayitNumarasi in enumerate(cursor):
            for indexSutun,kayitSutun in enumerate(kayitNumarasi):
               self.doktorrandevular.randevular.setItem(indexSatir,indexSutun,QTableWidgetItem(str(kayitSutun)))