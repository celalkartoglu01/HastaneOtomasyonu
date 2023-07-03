import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from iletisim import Ui_MainWindow

class Iletisim(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.iletisim = Ui_MainWindow()
        self.iletisim.setupUi(self)