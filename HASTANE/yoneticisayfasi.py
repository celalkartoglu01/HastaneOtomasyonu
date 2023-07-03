from PyQt5.QtWidgets import *
from yonetici_paneli import Ui_MainWindow
from yoneticibilgiler import YoneticiBilgileri
from yoneticihastalar import YoneticiHastalar
from yoneticidoktorlar import YoneticiDoktorlar
from yoneticiklinikler import YoneticiKlinikler

class YoneticiPaneli(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.yoneticipanel = Ui_MainWindow()
        self.yoneticipanel.setupUi(self)
        self.yoneticibilgiler = YoneticiBilgileri()
        self.yoneticihastalarr = YoneticiHastalar()
        self.yoneticidoktorlar = YoneticiDoktorlar()
        self.yoneticiklinikler = YoneticiKlinikler()
        self.yoneticipanel.btnyonetici.clicked.connect(self.YoneticiBilgileri)
        self.yoneticipanel.yoneticihastalar1.clicked.connect(self.YoneticiHastalarr)
        self.yoneticipanel.yoneticidoktorlar.clicked.connect(self.YoneticiDoktorlar)
        self.yoneticipanel.yoneticiklinikler.clicked.connect(self.YoneticiKlinikler)
    

    def YoneticiKlinikler(self):
        self.yoneticiklinikler.show()
    
    def YoneticiDoktorlar(self):
        self.yoneticidoktorlar.show()
    
    def YoneticiHastalarr(self):
        self.yoneticihastalarr.show()
    
    def YoneticiBilgileri(self):
        self.yoneticibilgiler.show()