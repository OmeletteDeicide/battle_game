from __future__ import annotations

import random

from src.entity.weapon import Weapon


def create_enemy() -> BasicEntity:
    enemy = BasicEntity("Monstre", random.randint(40, 60), random.randint(15, 30), random.randint(20, 35),
                        Weapon("Griffe en kératine", 7))
    return enemy


class BasicEntity:
    def __init__(self, name: str, pv: int, defense: int, attack: int, weapon: Weapon):
        self.weapon = weapon
        self.name = name
        self.pv = pv
        self.defense = defense
        self.attack = attack
        self.alive = True

    def compute_damage(self) -> int:
        return self.weapon.damage + self.attack

    def take_damage(self, damage: int):
        self.pv -= damage - self.defense

    def make_attack(self, player2: BasicEntity):
        if self.alive:
            damage_send = self.compute_damage()
            player2.take_damage(damage_send)

    def check_aliveness(self):
        if self.pv <= 0:
            self.alive = False
