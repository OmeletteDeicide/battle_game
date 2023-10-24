import secrets


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
    print("Comment voulez-vous ataquer ?\n1-Attaquer avec l'arme\n2-Lancer une boule de feu")
    choice = choice_made()
    return int(choice)


def choice_made():
    choice = input("\n")
    return int(choice)
