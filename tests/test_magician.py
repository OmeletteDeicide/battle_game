from src.entity.magician import Magician
from src.entity.weapon import Weapon


def create_magician() -> Magician:
    weapon = Weapon("Baton de mage", 11)
    magician = Magician("Toto le magicien", 65, 25, 20, weapon, 25, 30)
    return magician


def test_send_damage():
    magician_test = create_magician()
    assert magician_test.send_damage() == 31
