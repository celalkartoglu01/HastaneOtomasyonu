from PyQt5.QtWidgets import *
from lab2 import Ui_MainWindow
import mysql.connector

con = mysql.connector.connect(user='root',password = '',host = 'localhost',database = 'hastane')
cursor = con.cursor()

class Lab2(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.lab2 = Ui_MainWindow()
        self.lab2.setupUi(self)
        self.lab2.ara.clicked.connect(self.Ara)
        self.lab2.testgonder.clicked.connect(self.Gonder)
    
    def Ara(self):
        id = self.lab2.testid.text()
        query = "select * from tahlil where testid = %s"
        cursor.execute(query,(id,))
        for indexSatir,kayitNumarasi in enumerate(cursor):
            for indexSutun,kayitSutun in enumerate(kayitNumarasi):
               self.lab2.testler.setItem(indexSatir,indexSutun,QTableWidgetItem(str(kayitSutun)))
        self.lab2.testid.clear()
    
    def Gonder(self):
        hastaadi = self.lab2.hastaadi.text()
        hastasoyadi = self.lab2.hastasoyadi.text()
        doktor = self.lab2.doktoradi.currentText()
        testadi = self.lab2.testadi.text()
        testsonuc = self.lab2.testsonuc.text()
        query = "Insert into tahlil(testadi,doktoradi,hastaadi,hastasoyadi,aciklama) VALUES(%s,%s,%s,%s,%s)"
        cursor.execute(query,(testadi,doktor,hastaadi,hastasoyadi,testsonuc))
        con.commit()
        self.lab2.statusbar.showMessage("Test Sonucu Gönderildi !")
        self.lab2.hastaadi.clear()
        self.lab2.hastasoyadi.clear()
        self.lab2.testadi.clear()
        self.lab2.testsonuc.clear()
