import secrets

from src.entity.player import Player


def launch_dice_100() -> int:
    print("Le dé est jeté !")
    d100 = secrets.randbelow(100) + 1
    print(f"Vous avez obtenu : {d100}")
    if d100 <= 33:
        print("Vous esquivez le coup !")
    else:
        print("Dommage.")
    return d100


def magician_choice() -> int:
    choice = input("Voulez vous  :\n1-Attaquer\n2-Lancer un sort")
    return int(choice)


def battle_in_progress(player1: Player, player2: Player):
    print(f"{player1.name} pv : {player1.pv} et {player2.name} pv : {player2.pv} entre en phase de combat.")
    while player1.pv > 0 and player2.pv > 0:
        if player1.pv > 0:
            print(f"{player1.name} attaque")
            player1.make_attack(player2)
            print(f"{player2.name}, pv : {player2.pv}\n")
        if player2.pv > 0:
            print(f"{player2.name} attaque")
            player2.make_attack(player1)
            print(f"{player1.name}, pv : {player1.pv}\n")
