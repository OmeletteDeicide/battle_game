from src.entity.player import Player
from src.entity.weapon import Weapon
from src.utils import magician_choice


class Magician(Player):
    def __init__(self, name: str, pv: int, defense: int, attack: int, weapon: Weapon,magic_attack: int, mana: int):
        self.Weapon = weapon
        self.name = name
        self.pv = pv
        self.defense = defense
        self.attack = attack
        self.magic_attack = magic_attack
        self.mana = mana

    def send_damage(self) -> int:
        choice = magician_choice()
        is_choosing = True
        while is_choosing:
            if int(choice) == 1:
                return self.Weapon.damage + self.attack
            elif int(choice) == 2:
                self.mana -= 10
                return self.Weapon.damage + self.attack + self.magic_attack
            else:
                is_choosing = True
