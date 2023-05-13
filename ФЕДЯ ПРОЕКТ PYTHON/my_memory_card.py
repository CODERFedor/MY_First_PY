from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QButtonGroup, QGroupBox, QMessageBox, QHBoxLayout, QRadioButton, QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import shuffle

#создание класса 
class Vopros():
    def __init__(self, vopros, prav_otvet, neprav_otvet1, neprav_otvet2, neprav_otvet3):
        self.vopros = vopros
        self.prav_otvet = prav_otvet
        self.neprav_otvet1 = neprav_otvet1
        self.neprav_otvet2 = neprav_otvet2
        self.neprav_otvet3 = neprav_otvet3

#создание функций
def hide_V():
    Gruppa_V.hide()
    Gruppa_O.show()
    podtverdi.setText("продолжить")

def hide_O():
    Gruppa_V.show()
    Gruppa_O.hide()
    podtverdi.setText("подтвердить ответ")

    R_Gruppa.setExclusive(False)
    knopka1.setChecked(False)
    knopka2.setChecked(False)
    knopka3.setChecked(False)
    knopka4.setChecked(False)

    R_Gruppa.setExclusive(True)

def test():
    if spis_knop[0].isChecked():
        prav_neprav.setText("Правильно!")
    elif spis_knop[1].isChecked or spis_knop[2].isChecked or spis_knop[3].isChecked:
        prav_neprav.setText("Неправильно!")

    hide_V()      

def ask(v: Vopros):
    shuffle(spis_knop)
    spis_knop[0].setText(v.prav_otvet)
    spis_knop[1].setText(v.neprav_otvet1)
    spis_knop[2].setText(v.neprav_otvet2)
    spis_knop[3].setText(v.neprav_otvet3)    
    vopros.setText(v.vopros)
    otvet.setText(v.prav_otvet)
    hide_O()

def next_q():
    okno.cur_question = okno.cur_question + 1
    if okno.cur_question >= len(spisok):
        okno.cur_question = 0
    v = spisok[okno.cur_question]    
    ask(v)

def clic_OK():
    if podtverdi.text() == "подтвердить ответ":
        test()
    else:
        next_q()    

#создание окна
prilog = QApplication([])
okno = QWidget()
okno.setWindowTitle("опрос на PYTHON разработчика")
okno.cur_question =- 1

#создание экземпляров класса
spisok = []

spisok.append(Vopros("Как вывести спомощью print() стикер 🥀 с помощью текста?", "напиши : rose и :", "напиши : Rose и :", "напиши : роза и :", "напиши : Роза и :"))
spisok.append(Vopros("Загадка на внимательность. Как правильно пишется input()?", "input()", "inpиt()","iпput()","input"))
spisok.append(Vopros("Как называется модуль для рисования?", "turtle","random","Turtle","time"))
spisok.append(Vopros("В каком фильме есть змеи?","Гарри Потер","Черепашки-Ниндзя","Чебурашка","Основатель"))
spisok.append(Vopros("Нужна ли математика python разработчику?","немного","да","нет","1000 - 7"))
spisok.append(Vopros("ХаудиХо плохой программист?","да","нет","он топ","хз"))
spisok.append(Vopros("Удобно ли делать функции для уменьшения и понимания кода?","да","нет","ты чё дебил?","сам дебил"))
spisok.append(Vopros("Функция для создания класса","class","def class","class def","класс"))
spisok.append(Vopros("Вам понравился викторина","Конечно","Обязательно","Он прекрасен","Он прелестен"))
spisok.append(Vopros("Как называется функция для вывода информации?", "print()", "for()", "input()", "len()"))

#группа вопросы
Gruppa_V = QGroupBox("Варианты ответа:")
knopka1 = QRadioButton("print()")
knopka2 = QRadioButton("input()")
knopka3 = QRadioButton("len()")
knopka4 = QRadioButton("for()")

spis_knop = [knopka1, knopka2, knopka3, knopka4]

#лэйауты группы ответов
layoutG = QHBoxLayout()
layoutV1 = QVBoxLayout()
layoutV2 = QVBoxLayout()

#привязка вориантов ответа
layoutV1.addWidget(knopka1)
layoutV1.addWidget(knopka2)
layoutV2.addWidget(knopka3)
layoutV2.addWidget(knopka4)
layoutG.addLayout(layoutV1)
layoutG.addLayout(layoutV2)

#привязка горизонтального лэйаута группы вариантов ответа
Gruppa_V.setLayout(layoutG)

#группа кнопок
R_Gruppa = QButtonGroup()
R_Gruppa.addButton(knopka1)
R_Gruppa.addButton(knopka2)
R_Gruppa.addButton(knopka3)
R_Gruppa.addButton(knopka4)

#группа ответов
Gruppa_O = QGroupBox("Правильный ответ:")
prav_neprav = QLabel("Правильный/неправильный ответ:")
otvet = QLabel("print()")

#лэйауты группы оеветов
layoutV = QVBoxLayout()

Gruppa_O.setLayout(layoutV)

#привязка текста группы 
layoutV.addWidget(prav_neprav)
layoutV.addWidget(otvet)

#вопрос
vopros = QLabel("Как называется функция для вывода информации?")

#копка для подтверждения ответа
podtverdi = QPushButton("подтвердить ответ")

#лэйауты пивязки групы, вопоса, кнопки подтверждения ответа 
layoutG1 = QHBoxLayout()
layoutG2 = QHBoxLayout()
layoutG3 = QHBoxLayout()
layoutV = QVBoxLayout()

#пивязка групы, вопоса, кнопки подтверждения ответа
layoutG1.addWidget(vopros)
layoutG2.addWidget(Gruppa_V)
layoutG2.addWidget(Gruppa_O)
Gruppa_O.hide()
layoutG3.addWidget(podtverdi)
layoutV.addLayout(layoutG1)
layoutV.addLayout(layoutG2)
layoutV.addLayout(layoutG3)

okno.setLayout(layoutV)

#вызывание функции
podtverdi.clicked.connect(clic_OK)

okno.show()
prilog.exec_()           