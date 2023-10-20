import random
from typing import Dict


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
                if random.random() < 0.5:  # 50% de chance d'être "e"
                    map_data[(x, y)] = 'e'

    map_data[exit_position] = 'o'  # 'o' pour la sortie

    return map_data


class DungeonMap:
    def __init__(self, dungeon_map: Dict = generate_dungeon_map()):
        self.map = dungeon_map

