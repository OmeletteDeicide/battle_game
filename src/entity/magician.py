from src.entity.basicentity import BasicEntity
from src.entity.weapon import Weapon
from src.gameplay import magician_choice


class Magician(BasicEntity):
    def __init__(self, name: str, pv: int, defense: int, attack: int, weapon: Weapon, jinx: int, mana: int):
        super().__init__(name, pv, defense, attack, weapon)
        self.jinx = jinx
        self.mana = mana

    def compute_damage(self) -> int:
        choice = magician_choice()
        if choice == 1:
            return super().compute_damage()
        return self.magic_attack()

    def magic_attack(self):
        if self.mana > 10:
            self.mana -= 10
            return self.attack + self.jinx
