from __future__ import annotations
from src.entity.weapon import Weapon


class Player:
    def __init__(self, name: str, pv: int, defense: int, attack: int, weapon: Weapon):
        self.Weapon = weapon
        self.name = name
        self.pv = pv
        self.defense = defense
        self.attack = attack
        self.alive = True

    def send_damage(self) -> int:
        return self.Weapon.damage + self.attack

    def take_damage(self, damage: int):
        self.pv -= damage - self.defense

    def make_attack(self, player2: Player):
        if self.pv > 0:
            damage_send = self.send_damage()
            player2.take_damage(damage_send)
