import random

from character import Character, HeroCharacter
from strategies import ArcherStrategy, MagicianStrategy, WarriorStrategy

MonstersTypes = {"warrior": WarriorStrategy, "archer": ArcherStrategy, "magician": MagicianStrategy}


class Monster(Character):
    """Персонаж Чудовище."""

    MAX_HP = 10
    MAX_ATTACK = 10

    def __init__(self) -> None:
        """Инициализация чудовища."""
        self.hp = random.randrange(1, self.MAX_HP)
        self.attack = random.randrange(1, self.MAX_ATTACK)
        random_monster_type = random.choice(list(MonstersTypes.keys()))
        character_strategy = MonstersTypes[random_monster_type](self.attack)
        super().__init__(character_strategy, self.attack)

    def battle(self, opponent: HeroCharacter) -> None:
        """Обработка удара противника."""
        self.hp -= opponent.strategy.attack()
