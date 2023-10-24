from src.entity.barbarian import Barbarian
from src.entity.weapon import Weapon


def create_barbarian() -> Barbarian:
    weapon = Weapon("Ache de barabare", 20)
    barbarian = Barbarian("Toto le barbare", 70, 30, 40, weapon)
    return barbarian


def test_send_damage():
    player_barbarian_test = create_barbarian()
    assert player_barbarian_test.compute_damage() == 120
