from entity.player import Player
from entity.weapon import Weapon


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
        choice = input("Voulez vous  :\n1-Attaquer\n2-Lancer un sort")
        is_chosing = True
        while is_chosing:
            if int(choice) == 1:
                return self.Weapon.damage + self.attack
            elif int(choice) == 2:
                self.mana -= 10
                return self.Weapon.damage + self.attack + self.magic_attack
            else:
                is_chosing = True
    def choice_of_attack(self):
        pass

