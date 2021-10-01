class Strategy:
    """Интерфейс стратегии персонажа."""

    def attack(self) -> int:
        """Функция возвращает силу атаки."""
        pass

    def defense(self, opponent_attack: int) -> int:
        """Функция возвращает силу защиты от атаки."""
        return opponent_attack // 2


class WarriorStrategy(Strategy):
    """Стратегия Воин."""

    def __init__(self, attack: int) -> None:
        """Инициализация стратегии."""
        self.attack_power = attack

    def attack(self) -> int:
        """Сила удара воина."""
        return self.attack_power

    def __repr__(self) -> str:
        """Тип атаки."""
        return "воин"


class ArcherStrategy(Strategy):
    """Стратегия Лучник."""

    def __init__(self, attack: int) -> None:
        """Инициализация стратегии."""
        self.attack_power = attack

    def attack(self) -> int:
        """Сила атаки лучника."""
        return self.attack_power

    def __repr__(self) -> str:
        """Тип атаки."""
        return "лучник"


class MagicianStrategy(Strategy):
    """Стратегия Маг."""

    def __init__(self, attack: int) -> None:
        """Инициализация стратегии."""
        self.attack_power = attack

    def attack(self) -> int:
        """Сила атаки мага."""
        return self.attack_power

    def __repr__(self) -> str:
        """Тип атаки."""
        return "маг"
