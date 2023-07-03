from PyQt5.QtWidgets import *
from hasta_paneli import Ui_MainWindow
from hastabilgiler import HastaBilgiler
from hastarandevu import HastaRandevu
from hastarandevusil import HastaRandevuSil
from randevual import RandevuAl
from hastarecete import HastaRecete

class HastaPaneli(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.hastapaneli = Ui_MainWindow()
        self.hastapaneli.setupUi(self)
        self.hastabilgi = HastaBilgiler()
        self.hastarandevular = HastaRandevu()
        self.randevusil = HastaRandevuSil()
        self.hastarandevual = RandevuAl()
        self.hastareceteler = HastaRecete()
        self.hastapaneli.hastakullanici.clicked.connect(self.HastaKullanici)
        self.hastapaneli.randevularim.clicked.connect(self.Randevularim)
        self.hastapaneli.randevual.clicked.connect(self.RandevuAl)
        self.hastapaneli.randevusil.clicked.connect(self.RandevuSil)
        self.hastapaneli.recetelerim.clicked.connect(self.Recetelerim)
    

    def HastaKullanici(self):
        self.hastabilgi.show()
    
    def Randevularim(self):
        self.hastarandevular.show()
    
    def RandevuAl(self):
        self.hastarandevual.show()
    
    def RandevuSil(self):
        self.randevusil.show()
    
    def Recetelerim(self):
        self.hastareceteler.show()
