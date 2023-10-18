from entity.player import Player
from entity.weapon import Weapon

if __name__ == '__main__':
    weapon1 = Weapon("Poings", 9)
    weapon2 = Weapon("Epee", 12)
    player1 = Player("Simon", 80, 35, 20, weapon1)
    player2 = Player("Renrest", 75, 30, 30, weapon2)
    print(player2.name + player2.Weapon.name)
    print(player1.name + player1.Weapon.name)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
