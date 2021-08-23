from backpack_items import Sword


class Strategy:
    """Интерфейс стратегии персонажа."""

    def attack(self) -> int:
        """Функция возвращает силу атаки."""
        pass

    def defense(self, attack_power: int) -> int:
        """Функция возвращает силу защиты от атаки."""
        pass


class WarriorStrategy(Strategy):
    """Стратегия Воин."""

    def attack(self, sword: Sword) -> int:
        """Сила удара воина."""
        return sword.attack

    def defense(self, attack_power: int) -> int:
        """Сила защиты воина."""
        return attack_power // 2


class ArcherStrategy(Strategy):
    """Стратегия Лучник."""

    def attack(self) -> int:
        """Сила атаки лучника."""
        return 2

    def defense(self, attack_power: int) -> int:
        """Сила защиты лучника."""
        return attack_power // 3


class MagicianStrategy(Strategy):
    """Стратегия Маг."""

    def attack(self) -> int:
        """Сила атаки мага."""
        return 1

    def defense(self, attack_power: int) -> int:
        """Сила защиты мага."""
        return attack_power // 4
