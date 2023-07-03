from PyQt5.QtWidgets import *
from doktor import Ui_MainWindow
from doktorpaneli import DoktorPaneli
import mysql.connector

con = mysql.connector.connect(user='root',password = '',host = 'localhost',database = 'hastane')
cursor = con.cursor()

class DoktorGiris(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.doktorgiris = Ui_MainWindow()
        self.doktorgiris.setupUi(self)
        self.doktorpaneli = DoktorPaneli()
        self.doktorgiris.btndoktorgiris.clicked.connect(self.DoktorGiris)
    

    def DoktorGiris(self):
        kulladi = self.doktorgiris.lnedoktorkulladi.text()
        sifre = self.doktorgiris.lnedoktorsifre.text()
        query = ("Select * from doktor where kulladi = '"+kulladi+"' and parola = '"+ sifre + "'")
        cursor.execute(query)
        result = cursor.fetchone()
        if result:
            self.hide()
            self.doktorpaneli.show()
            self.doktorgiris.statusbar.showMessage("Başarıyla Giriş Yapıldı !")
            self.doktorgiris.lnedoktorkulladi.clear()
            self.doktorgiris.lnedoktorsifre.clear()
        else:
            self.doktorgiris.statusbar.showMessage("Kullanıcı Adı veya Şifre Hatalı !")
        
