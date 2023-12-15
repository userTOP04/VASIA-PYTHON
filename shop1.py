import os


def shop() -> bool:
    print(f"{hero[0]} приехал в лавку")
    print("1 - Купить предметы")
    print("2 - Продать предметы")
    print("3 - Выйти из игры")
    option = input("___ ")
    if option == "1":
        print("Купить зелье за лечения за 5 монет")
        print("Купить зелье за ??? за 10 монет")
        if option == "1":
            buy_item(hero, 'зелье лечения', 5)
        elif option == "2":
            buy_item(hero, 'зелье ???', 10)
    elif option == "2":
        pass
    elif option == "0":
        return False
    return True


def buy_item(hero: list, item_name: str, item_price: int) -> None:
    if hero[2] >= item_price:
        hero[5].append(item_name)
        hero[2] -= item_price
    else:
        print(f"У {hero[0]} недостадочно монет")


def show_inv(hero: list) -> None:
    couter = 0
    while couter < len():
        print(f"{hero[5[len]]}")
        idx += 1
        if not hero[5[len]]:
            break
        else:
            pass




hero = ['Вaся', 100, 10, 1, 0, []]
is_game = True
while True:
    print(hero)
    is_game = shop()
    if not is_game:
        break

