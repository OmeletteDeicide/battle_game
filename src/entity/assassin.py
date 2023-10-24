from src.entity.basicentity import BasicEntity
from src.gameplay import launch_dice_100


class Assassin(BasicEntity):

    def take_damage(self, damage: int):
        d100 = launch_dice_100()
        if d100 > 33:
            self.pv -= damage - self.defense

