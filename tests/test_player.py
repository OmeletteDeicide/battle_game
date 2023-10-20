from src.entity.player import Player
from src.entity.weapon import Weapon


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

def test_make_attack():
    player_fighter = create_player()
    player_receiver = create_player()
    assert player_receiver.pv == 50
    player_fighter.make_attack(player_receiver)
    assert player_receiver.pv == 30