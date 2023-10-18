from entity.weapon import Weapon


class Player:
    def __init__(self,name: str, pv: int, defense: int, attack: int, weapon: Weapon):
        self.Weapon = weapon
        self.name = name
        self.pv = pv
        self.defense = defense
        self.attack = attack
