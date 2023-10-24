from src.entity.assassin import Assassin
from src.entity.barbarian import Barbarian
from src.gameplay import choice_made
from src.entity.magician import Magician
from src.entity.basicentity import BasicEntity
from src.entity.weapon import Weapon


def battle_in_progress(player1: BasicEntity, player2: BasicEntity):
    print(f"{player1.name} pv : {player1.pv} et {player2.name} pv : {player2.pv} entre en phase de combat.")
    while player1.alive and player2.alive:
        print(f"{player1.name} attaque")
        player1.make_attack(player2)
        player2.check_aliveness()
        print(f"{player2.name}, pv : {player2.pv}\n")
        if player2.alive:
            print(f"{player2.name} attaque")
            player2.make_attack(player1)
            player1.check_aliveness()
            print(f"{player1.name}, pv : {player1.pv}\n")
    if not player1.alive:
        print("Vous êtes mort !")


def _chose_weapon() -> Weapon:
    while True:
        print("Quelle arme voulez-vous jouer ?\n1-Épée\n2-Double dague\n3-Bâton\n")
        weapon_choice = choice_made()
        if weapon_choice == 1:
            return Weapon("Épée", 12)
        elif weapon_choice == 2:
            return Weapon("Double dague", 12)
        elif weapon_choice == 3:
            return Weapon("Bâton", 12)
        else:
            print("Veuillez entrée un choix valide !\n")


def chose_class() -> BasicEntity:
    name_choice = input("Quelle est votre nom ?")
    weapon = _chose_weapon()
    while True:
        print("Quelle classe choisissez vous ?\n1-Barbare\n2-Magicien\n3-Voleur\n")
        class_choice = choice_made()
        if int(class_choice) == 1:
            return Barbarian(name_choice, 80, 35, 30, weapon)
        elif int(class_choice) == 2:
            return Magician(name_choice, 65, 30, 25, weapon, 40, 40)
        elif int(class_choice) == 3:
            return Assassin(name_choice, 72, 25, 40, weapon)
        else:
            print("Veuillez entrée un choix valide !\n")
