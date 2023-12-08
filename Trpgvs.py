from random import randint
import os



def play_game():
    pl_name = input("Введите имя вашего игрового персонажа: ")
    pl_hp = 100
    pl_money = 10
    pl_xp = 0
    pl_lvl = 1
    pl_potions = 0

    visit_rock(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_potions)



def visit_rock(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_potions):
    os.system("cls")
    show_hero(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_potions)
    print(f"{pl_name} приехал к камню. От камня идут три дороги:")
    print("1 - Играть в кости")
    print("2 - Сражение с разбойником")
    print("3 - Поехать в лавку")
    print("4 - Выйти из игры")
    option = input("Введите номер куда вы хотите пойти: ")
    if option == "1":
        visit_casino(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_potions)
    elif option == "2":
        visit_battle(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_potions)
    elif option == "3":
        visit_shop(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_potions)
    elif option == "4":
        return
    else:
        visit_rock(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_potions)



def show_hero(name, hp, money, xp, lvl, poution):
    print("Имя", name)
    print("Жизни", hp)
    print("Деньги", money)
    print("Опыт", xp)
    print("Уровень", lvl)
    print("Зелья", poution)


def visit_casino(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_potions):
    os.system("cls")
    show_hero(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_potions)
    while True:
        en_name = "Трактирщик Василий"
        print("1 - сыграть в кости ")
        print("2 - вернуться к камню ")
        option = input("Выберите вариант и нажмите ENTER ")
        os.system("cls")
        if option == "1":
            pass
        elif option == "2":
            print(f"{pl_name} уходит из трактира")
            visit_rock(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_potions)
        else:
            visit_casino(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_potions)

        pl_turn = randint(2, 12)
        en_turn = randint(2, 12)

        print(f"У {pl_name} {pl_money} монет")
        input("Нажмите ENTER чтобы бросить кости")

        print(f"{pl_name} выбросил {pl_turn}")
        print(f"{en_name} выбросил {en_turn}")

        if pl_turn > en_turn:
            pl_money += 1
            print(f"{pl_name} победил у него {pl_money}")
            pouse()
        elif en_turn > pl_turn:
            pl_money -= 1
            print(f"{pl_name} проиграл у него осталось {pl_money}")
            pouse()
        else:
            print("Ничья")
            pouse()








def visit_battle(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_potions):
    os.system("cls")
    show_hero(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_potions)
    en_name = "Боевой Григорий"
    print(f"{pl_name} приехал на арену ")
    print("1 - Сражение с бойцом")
    print("2 - Поехать обратно к камню")
    option = input("Выберите вариант и нажмите ENTER ")
    if option == "1":
        print(f"На арену выходит {en_name}")
        print("Бой начался!!!")
    elif option == "2":
        print(f"{pl_name} уежает с арены ")
        visit_rock(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_potions)
    else:
        visit_battle(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_potions)
    pouse()
    battle(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_potions)


def battle(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_potions):
    en_name = "Боевой Григорий"
    en_hp = 100
    en_xp = 0
    en_lvl = 1
    en_money = 15
    en_potions = 0
    while True:
        os.system("cls")
        show_hero(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_potions)
        show_hero(en_name, en_hp, en_money, en_xp, en_lvl, en_potions)
        if pl_potions == 0:
            print(f"{pl_name} хочет ударить {en_name}")
            pouse()
        else:
            print("1 - Ударить врага")
            print("2 - Выпить зелье лечения")
            options = input("Выберете вариант и нажмите ENTER ")
            if options == "1":
                en_hp = battle_turn(pl_name, pl_hp, en_name, en_hp)
                pl_hp = battle_turn(en_name, en_hp, pl_name, pl_hp)
            elif options == "2":
                pl_potions -= 1
                pl_hp += 30
                if pl_hp > 100:
                    pl_hp = 100
                print(f"{pl_name} выпил зелье лечения, теперь у него {pl_hp}")
                pouse()
                pl_hp = battle_turn(en_name, en_hp, pl_name, pl_hp)

        if pl_hp <= 0:
            print(f"{pl_name} умер. GAME OVER")
            pouse()
            break
        elif en_hp <= 0:
            print(f"{pl_name} победил {en_name}")
            pouse()
            visit_battle(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_potions)
        else:
            pass
        pouse()


def battle_turn(attacker_name, attacker_hp, defender_name, defender_hp):
    if attacker_hp >= 0:
        attack = randint(0, 10)

        defender_hp -= attack

        print(f"{attacker_name} ударил {defender_name} на {attack} ")

    return defender_hp




def visit_shop(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_potions):
    os.system("cls")
    show_hero(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_potions)
    poution_price = 5
    print(f"1 - купить зелье лечения за {poution_price}")
    print("2 - Поехать обратно к камню")
    option = input("Выберите вариант и нажмите ENTER ")
    if option == "1":
        if pl_money < poution_price:
            print(f"У {pl_name} не хватает монет")
            pouse()
            visit_shop(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_potions)
        elif pl_money >= pl_potions:
            pl_money -= poution_price
            pl_potions += 1
            print(f"{pl_name} купил одно зелье лечение")
            pouse()
            visit_shop(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_potions)
    elif option == "2":
        print(f"{pl_name} уходит из трактира")
        visit_rock(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_potions)



def pouse():
    input("Чтобы продолжить нажмите ENTER")


play_game()

