from random import randint
import os



def play_game():
    pl_name = input("Введите имя вашего игрового персонажа: ")
    pl_hp = 100
    pl_money = 10
    pl_xp = 0
    pl_lvl = 1

    visit_rock(pl_name, pl_hp, pl_money, pl_xp, pl_lvl)



def visit_rock(pl_name, pl_hp, pl_money, pl_xp, pl_lvl):
    os.system("cls")
    show_pl(pl_name, pl_hp, pl_money, pl_xp, pl_lvl)
    print(f"{pl_name} приехал к камню. От камня идут три дороги:")
    print("1 - Играть в кости")
    print("2 - Сражение с разбойником")
    print("3 - Поехать в лавку")
    print("4 - Играть в кости")
    option = input("Введите номер куда вы хотите пойти: ")
    if option == "1":
        visit_casino(pl_name, pl_hp, pl_money, pl_xp, pl_lvl)
    elif option == "2":
        visit_battle(pl_name, pl_hp, pl_money, pl_xp, pl_lvl)
    elif option == "3":
        print("3")
    elif option == "4":
        print("4")
    else:
        visit_rock(pl_name, pl_hp, pl_money, pl_xp, pl_lvl)



def show_pl(pl_name, pl_hp, pl_money, pl_xp, pl_lvl):
    print("Имя", pl_name)
    print("Жизни", pl_hp)
    print("Деньги", pl_money)
    print("Опыт", pl_xp)
    print("Уровень", pl_lvl)


def visit_casino(pl_name, pl_hp, pl_money, pl_xp, pl_lvl):
    os.system("cls")
    show_pl(pl_name, pl_hp, pl_money, pl_xp, pl_lvl)
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
            visit_rock(pl_name, pl_hp, pl_money, pl_xp, pl_lvl)
        else:
            visit_casino(pl_name, pl_hp, pl_money, pl_xp, pl_lvl)

        pl_turn = randint(2, 12)
        en_turn = randint(2, 12)

        print(f"У {pl_name} {pl_money} монет")
        input("Нажмите ENTER чтобы бросить кости")

        print(f"{pl_name} выбросил {pl_turn}")
        print(f"{en_name} выбросил {en_turn}")

        if pl_turn > en_turn:
            pl_money += 1
            print(f"{pl_name} победил у него {pl_money}")
            input("Чтобы продолжить нажмите ENTER")
        elif en_turn > pl_turn:
            pl_money -= 1
            print(f"{pl_name} проиграл у него осталось {pl_money}")
            input("Чтобы продолжить нажмите ENTER")
        else:
            print("Ничья")
            input("Чтобы продолжить нажмите ENTER")








def visit_battle(pl_name, pl_hp, pl_money, pl_xp, pl_lvl):
    os.system("cls")
    show_pl(pl_name, pl_hp, pl_money, pl_xp, pl_lvl)
    en_name = "Боевой Григорий"
    en_hp = 100
    print(f"{pl_name} приехал на арену ")
    print("1 - Сражение с бойцом")
    print("2 - Поехать обратно к камню")
    option = input("Выберите вариант и нажмите ENTER ")
    if option == "1":
        print(f"На арену выходит {en_name}")
        print("Бой начался!!!")
    elif option == "2":
        print(f"{pl_name} уежает с арены ")
        visit_rock(pl_name, pl_hp, pl_money, pl_xp, pl_lvl)
    else:
        visit_battle(pl_name, pl_hp, pl_money, pl_xp, pl_lvl)
    while True:
        os.system("cls")
        input("Чтобы ударить нажмите ENTER")

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
            input("Чтобы продолжить нажмите ENTER")
            break
        elif en_hp <= 0:
            print(f"{pl_name} победил {en_name}")
            print(f"{pl_name} уежает к камню")
            input("Чтобы продолжить нажмите ENTER")
            visit_rock(pl_name, pl_hp, pl_money, pl_xp, pl_lvl)
        else:
            pass
        input("Чтобы продолжить нажмите ENTER")




def visit_shop():
    os.system("cls")
    print("3")



play_game()

