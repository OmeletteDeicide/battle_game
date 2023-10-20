from src.entity.assassin import Assassin
from src.entity.dungeon_map import DungeonMap
from src.entity.magician import Magician
from src.entity.player import Player
from src.entity.weapon import Weapon
from src.utils import battle_in_progress

if __name__ == '__main__':
    weapon1 = Weapon("Poings", 9)
    weapon2 = Weapon("Epee", 12)
    player1 = Magician("Simon", 80, 35, 31, weapon1, 35, 30)
    player2 = Assassin("Renrest", 75, 30, 34, weapon2)
    print(player2.name + player2.Weapon.name)
    print(player1.name + player1.Weapon.name)
    # battle_in_progress(player1, player2)
    dungeon_map = DungeonMap()
    for y in range(9):
        for x in range(9):
            print(dungeon_map.map[(x, y)], end=' ')
        print()
