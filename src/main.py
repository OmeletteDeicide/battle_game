from src.map.dungeon_map import DungeonMap
from src.utils import chose_class


def game_loop():
    player_position = (4, 4)
    dungeon_map = DungeonMap()
    print("Vous vous réveillez en plein milieu d'un donjon.\n")
    main_player = chose_class()
    is_continuing = True
    while is_continuing:
        is_continuing, player_position = dungeon_map.move_player(dungeon_map, player_position, main_player)


if __name__ == '__main__':
    game_loop()
