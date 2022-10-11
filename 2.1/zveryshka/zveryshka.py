class Monster_bag(object):
    def __init__(self, name, kushaty=3, skuka=3):
        self.name = name
        self.kushaty = kushaty
        self.skuka = skuka
    @property
    def mood(self):
        global m
        sostoanye = self.skuka + self.kushaty
        if sostoanye == 9 or sostoanye >= 12:
            m = "Счастливо"
        elif sostoanye == 6 or sostoanye == 3:
            m = "Нормально"
        elif sostoanye == 0 or sostoanye == -3:
            m = "Плохо"
        elif sostoanye <= 6:
            m = "Ужасно"
        print(sostoanye)
        return m
    def speack(self):
        print("\n Я ", self.name, "и Я себя чувствую ", self.mood)
    def feed(self, food=3):
        print("Спасибо")
        self.kushaty += food
    def play(self, fun=3):
        print("Ееееееееей")
        self.skuka += fun
    def ignor(self, food=3, fun=3):
        print("Мне скучно!")
        self.skuka -= fun
        self.kushaty -= food
def main():
    monster_name = input("Имя питомца:  ")
    print("Имя: ", monster_name)
    monster = Monster_bag(monster_name)
    choice = None
    while choice != 0:
        print('_______________________________ \n 0 - Выход \n 1 - Послушать питомца (Узнать состояние) \n 2 - Покормить \n 3 - Играть \n 4 - Игнорить')
        choice = input("Пожалуйста, введите свой выбор:  ")
        if choice == "0":
            print("Пока!")
            break
        elif choice == "1":
            monster.speack()
        elif choice == "2":
            monster.feed()
        elif choice == "3":
            monster.play()
        elif choice == "4":
            monster.ignor()
        else:
            print('Нету такого выбора')
main()