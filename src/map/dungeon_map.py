from __future__ import annotations
import random
from typing import Dict

from src.entity.basicentity import create_enemy, BasicEntity
from src.utils import battle_in_progress


def generate_dungeon_map():
    map_data = {
        (x, y): 'm' for x in range(9) for y in range(9)
    }

    exit_side = random.choice(["top", "bottom", "left", "right"])

    if exit_side == "top":
        exit_position = (random.randint(0, 9 - 1), 0)
    elif exit_side == "bottom":
        exit_position = (random.randint(0, 9 - 1), 9 - 1)
    elif exit_side == "left":
        exit_position = (0, random.randint(0, 9 - 1))
    else:
        exit_position = (9 - 1, random.randint(0, 9 - 1))

    for x in range(9):
        for y in range(9):
            if map_data[(x, y)] == 'm' and (x, y) != exit_position:
                if random.random() < 0.5:
                    map_data[(x, y)] = ' '

    map_data[exit_position] = 'o'
    map_data[4, 4] = 'p'

    return map_data


class DungeonMap:
    def __init__(self, dungeon_map: Dict = generate_dungeon_map()):
        self.map = dungeon_map

    def display_map(self):
        for y in range(9):
            for x in range(9):
                print(self.map[(x, y)], end=' ')
            print()

    def move_player(self, dungeon_map: DungeonMap, player_position: tuple, main_player: BasicEntity) -> tuple[bool, tuple[int, int]]:
        while True:
            dungeon_map.display_map()
            move = input("Où voulez-vous aller ? (Z pour haut, Q pour gauche, S pour bas, D pour droite): ").upper()

            new_position = player_position

            if move == "Z" and player_position[1] > 0:
                new_position = (player_position[0], player_position[1] - 1)
            elif move == "Q" and player_position[0] > 0:
                new_position = (player_position[0] - 1, player_position[1])
            elif move == "S" and player_position[1] < 9 - 1:
                new_position = (player_position[0], player_position[1] + 1)
            elif move == "D" and player_position[0] < 9 - 1:
                new_position = (player_position[0] + 1, player_position[1])
            else:
                print("Saisie incorrecte. Utilisez Z, Q, S ou D pour vous déplacer.")

            if self.map[new_position] == 'm':
                enemy = create_enemy()
                battle_in_progress(main_player, enemy)
                self.map[player_position] = ' '
                self.map[new_position] = 'p'
                return True, new_position

            if self.map[new_position] == 'o':
                self.map[player_position] = ' '
                self.map[new_position] = 'p'
                self.display_map()
                print("Félicitations, vous avez gagné !")
                return False, new_position

            self.map[player_position] = ' '
            self.map[new_position] = 'p'
            return True,new_position
