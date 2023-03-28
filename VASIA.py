class Ciberhero:
    """docstring for ClassName"""
    def __init__(self):
        self.name = "Кибербогатырь"
        self.hp = 100
        self.at = 5
        self.inv = []
        self.dodge = 10




class CiberMag(Ciberhero):
    def __init__(self):
        self.name = "КиберМаг"
        self.hp = 50
        self.at = 20
        self.inv = []
        self.dodge = 12


class Ciberenomy:
    """docstring for ClassName"""
    def __init__(self):
        self.name = "Киберзлодей"
        self.hp = 100
        self.at = 5
        self.inv = []
        self.dodge = 10



pl1 = Ciberhero()
print("Приветствую тебя Кибербогатырь ты попал в свое первое путешествие, хочешь жить и продолжить путешествие ? Тогда принеси мне деньги их ты можешь найти на своей дороге ")
print("Что вы выберете? 1 - Соглоситься и пойти искать монеты, 2 - Отказаться и пытаться убежать от царя")
kay = input()
if kay == "1":
    print("Кибербогатырь согласился и пошел по дороге к своим путешествим, зная что его ждет куча преград")

elif kay == "2":
    print("- Я тебя предупреждал,ответил царь и убил вашего кибербогатыря, Вы открыли плохую концовку")
else:
    print("- Кибер баготырь свахатил меч и убил царя и зажил славной жизнью, Вы открыли секретную концовку")







