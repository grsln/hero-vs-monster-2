import random

from character import Character
from strategies import ArcherStrategy, MagicianStrategy, Strategy, WarriorStrategy

MonstersTypes = {"warrior": WarriorStrategy, "archer": ArcherStrategy, "magician": MagicianStrategy}


class Monster(Character):
    """Персонаж Чудовище."""

    MAX_HP = 10
    MAX_ATTACK = 10

    def __init__(self, character_strategy: Strategy = WarriorStrategy()):
        """Инициализация чудовища."""
        super().__init__(character_strategy)
        self.hp = random.randrange(1, self.MAX_HP)
        self.attack = random.randrange(1, self.MAX_ATTACK)

    def battle(self, opponent: Character) -> None:
        """Обработка удара противника."""
        self.hp -= opponent.strategy.attack()
