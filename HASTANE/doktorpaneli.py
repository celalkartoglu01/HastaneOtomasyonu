from PyQt5.QtWidgets import *
from doktor_paneli import Ui_MainWindow
from doktorbilgiler import DoktorBilgiler
from doktorrandevular import DoktorRandevular
from doktorrandevusil import RandevuSil
from doktorbekleyen import DoktorBekleyen
from doktortahliller import DoktorTahliller

class DoktorPaneli(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.doktorpaneli = Ui_MainWindow()
        self.doktorpaneli.setupUi(self)
        self.doktorbilgiler = DoktorBilgiler()
        self.randevular = DoktorRandevular()
        self.randevusil = RandevuSil()
        self.bekleyen = DoktorBekleyen()
        self.tahliller = DoktorTahliller()
        self.doktorpaneli.doktorkullanici.clicked.connect(self.DoktorKullanici)
        self.doktorpaneli.doktorrandevularim.clicked.connect(self.DoktorRandevular)
        self.doktorpaneli.randevusil.clicked.connect(self.RandevuSil)
        self.doktorpaneli.doktorbekleyenhasta.clicked.connect(self.BekleyenHasta)
        self.doktorpaneli.tahlilsonuclari.clicked.connect(self.Tahliller)
    
    def Tahliller(self):
        self.tahliller.show()
    
    def BekleyenHasta(self):
        self.bekleyen.show()
    
    def RandevuSil(self):
        self.randevusil.show()
    
    def DoktorRandevular(self):
        self.randevular.show()
    
    def DoktorKullanici(self):
        self.doktorbilgiler.show()
    
    

       
        

        
   