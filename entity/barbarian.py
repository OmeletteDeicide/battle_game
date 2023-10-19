from entity.player import Player


class Barbarian(Player):

    def send_damage(self) -> int:
        return 2*(self.Weapon.damage + self.attack)