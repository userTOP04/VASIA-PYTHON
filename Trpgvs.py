from random import randint
import os



def play_game():
    pl_name = input("Введите имя вашего игрового персонажа: ")
    pl_hp = 100
    pl_money = 10
    pl_xp = 0
    pl_lvl = 1
    pl_poution = 0

    visit_rock(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_poution)



def visit_rock(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_poution):
    os.system("cls")
    show_pl(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_poution)
    print(f"{pl_name} приехал к камню. От камня идут три дороги:")
    print("1 - Играть в кости")
    print("2 - Сражение с разбойником")
    print("3 - Поехать в лавку")
    print("4 - Выйти из игры")
    option = input("Введите номер куда вы хотите пойти: ")
    if option == "1":
        visit_casino(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_poution)
    elif option == "2":
        visit_battle(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_poution)
    elif option == "3":
        visit_shop(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_poution)
    elif option == "4":
        return
    else:
        visit_rock(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_poution)



def show_pl(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_poution):
    print("Имя", pl_name)
    print("Жизни", pl_hp)
    print("Деньги", pl_money)
    print("Опыт", pl_xp)
    print("Уровень", pl_lvl)
    print("Зелья", pl_poution)


def visit_casino(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_poution):
    os.system("cls")
    show_pl(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_poution)
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
            visit_rock(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_poution)
        else:
            visit_casino(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_poution)

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








def visit_battle(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_poution):
    os.system("cls")
    show_pl(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_poution)
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
        visit_rock(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_poution)
    else:
        visit_battle(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_poution)
    pouse()
    battle(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_poution)


def battle(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_poution):
    en_name = "Боевой Григорий"
    en_hp = 100
    while True:
        os.system("cls")
        print("1 - Ударить врага")
        print("2 - Выпить зелье лечения")
        options = input("Выберете вариант и нажмите ENTER")
        if options == "1":
            pass
        elif options == "2":
            if pl_poution == 0:
                print(f"У {pl_name} нет зелий.(Вы можете купить зелья в магазине)")
                pouse()
            else:
                pl_poution -= 1
                pl_hp += 30
                if pl_hp > 100:
                    pl_hp = 100
                print(f"{pl_name} выпил зелье лечения, теперь у него {pl_hp}")
                pouse()
        pl_at = randint(1, 10)
        en_at = randint(1, 10)

        en_hp -= pl_at
        pl_hp -= en_at

        print(f"{pl_name} ударил {en_name} на {pl_at} ")
        print(f"У {en_name} осталось {en_hp}")
        print(f"{en_name} ударил {pl_name} на {en_at} ")
        print(f"У {pl_name} осталось {pl_hp}")

        if pl_hp <= 0:
            print(f"{pl_name} умер. GAME OVER")
            pouse()
            break
        elif en_hp <= 0:
            print(f"{pl_name} победил {en_name}")
            print(f"{pl_name} уежает к камню")
            pouse()
            visit_rock(pl_name, pl_hp, pl_money, pl_xp, pl_lvl)
        else:
            pass
        pouse()



def visit_shop(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_poution):
    os.system("cls")
    show_pl(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_poution)
    poution_price = 5
    print(f"1 - купить зелье лечения за {poution_price}")
    print("2 - Поехать обратно к камню")
    option = input("Выберите вариант и нажмите ENTER ")
    if option == "1":
        if pl_money < poution_price:
            print(f"У {pl_name} не хватает монет")
            pouse()
            visit_shop(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_poution)
        elif pl_money >= pl_poution:
            pl_money -= poution_price
            pl_poution += 1
            print(f"{pl_name} купил одно зелье лечение")
            pouse()
            visit_shop(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_poution)
    elif option == "2":
        print(f"{pl_name} уходит из трактира")
        visit_rock(pl_name, pl_hp, pl_money, pl_xp, pl_lvl, pl_poution)



def pouse():
    input("Чтобы продолжить нажмите ENTER")


play_game()

