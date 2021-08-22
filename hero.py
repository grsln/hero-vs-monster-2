from character import Character
from monsters import Monster


class Hero(Character):
    """Персонаж Рыцарь."""

    def __init__(self) -> None:
        """Инициализация рыцаря."""
        super().__init__()
        self.hp = 20

    def battle(self, monster: Monster) -> None:
        """Обработка удара монстра."""
        monster_attack = monster.strategy.attack()
        defense = 0
        if isinstance(monster.strategy, type(self.strategy)):
            defense = self.strategy.defense(monster_attack)
        print(f"hero attack:{monster_attack} defense:{defense}")
        self.hp -= monster_attack - defense
