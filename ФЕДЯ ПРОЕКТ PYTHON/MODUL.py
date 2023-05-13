from random import *

#настройки
def settings():
    okno_lose = QMessageBox()
    okno_lose.setWindowTitle("Временно не доступно!!!")
    okno_lose.setText("В данной версии эта функция не доступна")
    okno_lose.exec_()

#информация о игре
def information_about_game():
    okno_lose = QMessageBox()
    okno_lose.setWindowTitle("Об игре")
    okno_lose.setText("Разработчик: Фёдор Ляшенко\nО игре: бескончная и нтересная новелла с интересным визуалом и класной музыкой\nВерсия: 0.6")
    okno_lose.exec_() 

#кубик
def kubik():
    kub = randint(1, 10)           
    life_1 = randint(1, 10)
    life_2 = randint(1, 10)
    life_3 = randint(1, 10)
    while life_1 == life_2 or life_1 == life_3 or life_2 == life_3:
        life_1 = randint(1, 10)
        life_2 = randint(1, 10)
        life_3 = randint(1, 10)

#животное
def have_animal(animal, cat, dog):
    if animal == True and cat == True:
        animal == "кот"
    if animal == True and dog == True:
        animal == "собака"
    if animal == False:
        animal == "отсутствует" 

#сон
def sleep(cat, smert):
    son = randint(10)
    if son == 1 or son == 2:
        fatigue += randint(5, 7)
        son = "Вам всю ночь снились кошмары. ваш усталость поднялась до "
    if son == 10 and cat == False:
        smert = True
        son = "Зомби услышали ваш храп."    

#игровые условия
def game(label, day, hunger, thirst, fatigue, hp, animal):
    if label.text() == "Киньте кубик":
        kubik()
        label.setText("Вам выпало", kub, ", готовы риснуить?")
    if label.text() == "Вы сидите тихо притаив дыхание. Вам страшно. Через несколько часов сидения в раздумиях вы встаёте и осматриваетесь.":
        have_animal()
        label.setText("День:", day,"\nГолод:", hunger,"\nЖажда:", thirst,"\nУсталость:", fatigue,"\nЖизнь:", hp,"\nЖивотное:", animal)
    if label.text() == "Вы обошли дома которые хотели.":
        sleep()
        label.setText(son)