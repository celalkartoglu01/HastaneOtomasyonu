from PyQt5.QtWidgets import *
from ilk_sayfa import Ui_Form
from yonetici_giris import Yonetici
from hastakabulgiris import HastaKabulGiris
from doktorgiris import DoktorGiris
from labgiris import Laboratuvar
from hastagiris import HastaGiris
from kayitol import Kaydol
from iletisimm import Iletisim



class IlkSayfa(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ilksayfaform = Ui_Form()
        self.ilksayfaform.setupUi(self)
        self.yoneticigirisform = Yonetici()
        self.hastakabulgirisform = HastaKabulGiris()
        self.doktorgirisform = DoktorGiris()
        self.labgiris = Laboratuvar()
        self.hastagiris = HastaGiris()
        self.kaydol = Kaydol()
        self.iletisim = Iletisim()
        self.ilksayfaform.btnyonetici.clicked.connect(self.YoneticiGiris)
        self.ilksayfaform.btnhastakabul.clicked.connect(self.HastaKabulGiris)
        self.ilksayfaform.btndoktor.clicked.connect(self.DoktorGiris)
        self.ilksayfaform.btnlaboratuvar.clicked.connect(self.LabGiris)
        self.ilksayfaform.btnhastagiris.clicked.connect(self.HastaGiris)
        self.ilksayfaform.btnkaydol.clicked.connect(self.Kaydol)
        self.ilksayfaform.btniletisim.clicked.connect(self.Iletisim)
    

    def YoneticiGiris(self):
        self.yoneticigirisform.show()
    
    def HastaKabulGiris(self):
        self.hastakabulgirisform.show()

    def DoktorGiris(self):
        self.doktorgirisform.show()
    
    def LabGiris(self):
        self.labgiris.show()
    
    def HastaGiris(self):
        self.hastagiris.show()
    
    def Kaydol(self):
        self.kaydol.show()
    
    def Iletisim(self):
        self.iletisim.show()