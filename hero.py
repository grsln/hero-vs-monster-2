from character import Character
from monsters import Monster


class Hero(Character):
    """Персонаж Рыцарь."""

    def __init__(self) -> None:
        """Инициализация рыцаря."""
        super().__init__()
        self.hp = 100

    def battle(self, monster: Monster) -> None:
        """Обработка удара монстра."""
        defense = isinstance(monster.strategy, type(self.strategy))
        print('Защита', defense)
        self.hp -= monster.strategy.attack() - self.strategy.defense()
