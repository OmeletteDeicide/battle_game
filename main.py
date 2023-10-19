from entity.assassin import Assassin
from entity.barbarian import Barbarian
from entity.magician import Magician
from entity.player import Player
from entity.weapon import Weapon

if __name__ == '__main__':
    weapon1 = Weapon("Poings", 9)
    weapon2 = Weapon("Epee", 12)
    player1 = Magician("Simon", 80, 35, 31, weapon1, 40, 30)
    player2 = Assassin("Renrest", 75, 30, 34, weapon2)
    print(player2.name + player2.Weapon.name)
    print(player1.name + player1.Weapon.name)