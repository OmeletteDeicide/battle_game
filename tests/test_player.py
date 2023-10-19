from entity.player import Player
from entity.weapon import Weapon


def create_player() -> Player:
    weapon = Weapon("Ache", 15)
    player = Player("Toto", 50, 25, 30, weapon)
    return player


def test_send_damage():
    player_test = create_player()
    assert player_test.send_damage() == 45

def test_take_damage():
    player_test = create_player()
    player_test.take_damage(45)
    assert player_test.pv == 30