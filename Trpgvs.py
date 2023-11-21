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
        print("2")
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
    input("Чтобы продолжить нажмите ENTER")
    en_name = "Трактирщих Жмых Злой"
    en_money = 10
    while en_money or pl_money <= 0:
        os.system("cls")
        print("1 - продолжить ")
        print("2 - выйти ")
        option = input("Выберите вариант и нажмите ENTER ")
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
        print(f"У {en_name} {en_money} монет")
        input("Нажмите ENTER чтобы бросить кости")

        print(f"{pl_name} выбросил {pl_turn}")
        print(f"{en_name} выбросил {en_turn}")

        if pl_turn > en_turn:
            pl_money += 1
            en_money -= 100
            print(f"{pl_name} победил у него {pl_money}")
            print(f"{en_name} проиграл у него осталось {en_money}")
            input("Чтобы продолжить нажмите ENTER")
        elif en_turn > pl_turn:
            en_money += 1
            pl_money -= 1
            print(f"{en_name} победил у него {en_money}")
            print(f"{pl_name} проиграл у него осталось {pl_money}")
            input("Чтобы продолжить нажмите ENTER")
        else:
            print("Ничья")
            input("Чтобы продолжить нажмите ENTER")








def visit_battle():
    os.system("cls")
    print("2")



def visit_shop():
    os.system("cls")
    print("3")



play_game()

