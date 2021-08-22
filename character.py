from strategies import ArcherStrategy, MagicianStrategy, Strategy, WarriorStrategy


class Character:
    """Персонаж с меняющимися стратегиями."""

    def __init__(self, character_strategy: Strategy = WarriorStrategy()) -> None:
        """Инициализация персонажа."""
        self._strategy = character_strategy

    @property
    def strategy(self) -> Strategy:
        """Ссылку на стратегию."""
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """Установка стратегии."""
        self._strategy = strategy

    def set_sword_strategy(self):
        """Установка стратегии WarriorStrategy."""
        self._strategy = WarriorStrategy()

    def set_archer_strategy(self):
        """Установка стратегии ArcherStrategy."""
        self._strategy = ArcherStrategy()

    def set_magician_strategy(self):
        """Установка стратегии MagicianStrategy."""
        self._strategy = MagicianStrategy()
