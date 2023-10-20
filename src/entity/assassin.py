from src.entity.player import Player
import secrets

from src.entity.weapon import Weapon
from src.utils import launch_dice_100


class Assassin(Player):
    def __init__(self, name: str, pv: int, defense: int, attack: int, weapon: Weapon):
        self.Weapon = weapon
        self.name = name
        self.pv = pv
        self.defense = defense
        self.attack = attack

    def take_damage(self, damage: int):
        d100 = launch_dice_100()
        if d100 > 33:
            self.pv -= damage - self.defense

