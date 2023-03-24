class CyberHero:
    def __init__(self, name, force, hp, dodge, luck, xp, inventory):
        print("Кибер баготырь", name, "создан")
        self.name = name
        self.force = force
        self.hp = hp
        self.dodge = dodge
        self.luck = luck
        self.xp = xp
        self.inventory = inventory


hero1 = CyberHero(name="VASIA",force=10,hp=100,dodge=10,luck=1,xp=0,inventory=[])
hero2 = CyberHero(name="VASIA",force=10,hp=100,dodge=10,luck=1,xp=0,inventory=[])

def combat_turn(name, force, hp):
    if hp > 0:
        hp -= force
        print(hero1.name, "ударил", hero2.name, "на", hero1.force, "жизней!")

def start_fight(name, force, hp) -> None:
    while hero1.hp > 0 and hero2.hp > 0:
            combat_turn(hero1, hero2)
            combat_turn(hero2, hero1)
            print("")
            print(hero1.hp)
            print(hero2.hp)

