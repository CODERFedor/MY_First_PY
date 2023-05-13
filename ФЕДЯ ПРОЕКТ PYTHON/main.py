from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QButtonGroup, QGroupBox, QMessageBox, QHBoxLayout, QRadioButton, QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from MODUL import *

#создание окна
prilog = QApplication([])
okno = QWidget()
okno.setWindowTitle("Delivery of brains: the story of the courier")
okno.resize(1000, 700)

settings()

#конец
okno.show()
prilog.exec_()