from entity.player import Player
import secrets

from entity.weapon import Weapon


class Assassin(Player):
    def __init__(self, name: str, pv: int, defense: int, attack: int, weapon: Weapon):
        self.Weapon = weapon
        self.name = name
        self.pv = pv
        self.defense = defense
        self.attack = attack
    def take_damage(self, damage: int):
        print("Le dé est jeté !")
        d100 = secrets.randbelow(100) + 1
        print(f"Vous avez obtenu : {d100}")
        if d100 <= 33:
            print(f"{self.name} a esquivé le coup !")
            print(f"PV actuel de {self.name} : {self.pv}")
        else:
            print("Vous prenez le coup de plein fouet !")
            self.pv -= damage - self.defense
            print(f"PV actuel de {self.name} : {self.pv}")