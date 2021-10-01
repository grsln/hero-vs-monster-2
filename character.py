from strategies import ArcherStrategy, MagicianStrategy, Strategy, WarriorStrategy


class Character:
    """Персонаж с меняющимися стратегиями."""

    def __init__(self, character_strategy: Strategy, attack: int) -> None:
        """Инициализация персонажа."""
        self.attack = attack
        self._strategy = character_strategy

    @property
    def strategy(self) -> Strategy:
        """Ссылка на стратегию."""
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """Установка стратегии."""
        self._strategy = strategy

    def set_sword_strategy(self) -> None:
        """Установка стратегии WarriorStrategy."""
        self._strategy = WarriorStrategy(self.attack)

    def set_archer_strategy(self) -> None:
        """Установка стратегии ArcherStrategy."""
        self._strategy = ArcherStrategy(self.attack)

    def set_magician_strategy(self) -> None:
        """Установка стратегии MagicianStrategy."""
        self._strategy = MagicianStrategy(self.attack)


class HeroCharacter:
    """Персонаж Рыцарь с меняющимися стратегиями."""

    def __init__(self, character_strategy: Strategy) -> None:
        """Инициализация персонажа."""
        self._strategy = character_strategy

    @property
    def strategy(self) -> Strategy:
        """Ссылка на стратегию."""
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """Установка стратегии."""
        self._strategy = strategy

    # def set_sword_strategy(self) -> None:
    #     """Установка стратегии WarriorStrategy."""
    #     self._strategy = HeroWarriorStrategy()
    #
    # def set_archer_strategy(self) -> None:
    #     """Установка стратегии ArcherStrategy."""
    #     self._strategy = HeroArcherStrategy()
    #
    # def set_magician_strategy(self) -> None:
    #     """Установка стратегии MagicianStrategy."""
    #     self._strategy = HeroMagicianStrategy()
