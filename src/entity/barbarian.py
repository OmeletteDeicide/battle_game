from src.entity.basicentity import BasicEntity


class Barbarian(BasicEntity):

    def compute_damage(self) -> int:
        return 2*(super().compute_damage())
    