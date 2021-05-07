class MonsterTroops(object):
    def __init__(self, name, damage, hp, mana, specialized):
        self.name = name
        self.damage = damage
        self.hp = hp
        self.mana = mana
        self.specialized = specialized

toxic_spiders = MonsterTroops("Toxic Spider", 85, 550, 75, "None")
skeloton = MonsterTroops("Skeleton", 45, 120, 55, "None")
elemental_spirits = MonsterTroops("Elemental Spirits", 50, 450, 120, "None")
dragon = MonsterTroops("Dragon", 1000, 250, 150, "Fire Breathe")

class HumanTroops(object):
    def __init__(self, name, damage, hp, mana, specialized):
        self.name = name
        self.damage = damage
        self.hp = hp
        self.mana = mana
        self.specialized = specialized

the_five = HumanTroops("The five", 55, 155, 75, "clone")
one_eye_man = HumanTroops("One Eye Man", 35, 450, 120, "Hooks")
lady_gun = MonsterTroops("Lady Gun", 345, 200, 175, "Blazzing Shot")

monster_troops = [toxic_spiders, skeloton, elemental_spirits, dragon]
human_troops = [the_five, one_eye_man, lady_gun]

print("\nMonster Troops\n")

for monster_troop in monster_troops:
    print("\nTroop Name: ", monster_troop.name, "\n Damage: ", monster_troop.damage, 
    "\n HP: ", monster_troop.hp, " \n Mana: ", monster_troop.mana, 
    "\n Special Abillities: ", monster_troop.specialized)

print("\nHuman Troops\n")

for human_troop in human_troops:
    print("\nTroop Name: ", human_troop.name, "\n Damage: ", human_troop.damage, 
    "\n HP: ", human_troop.hp, "\n Mana: ", human_troop.mana, 
    "\n Special Abillities: ", human_troop.specialized)
