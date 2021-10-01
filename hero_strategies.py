from backpack import Backpack
from strategies import ArcherStrategy, MagicianStrategy, WarriorStrategy


class HeroWarriorStrategy(WarriorStrategy):
    """Стратегия Воин."""

    def __init__(self, backpack: Backpack) -> None:
        """Инициализация стратегии."""
        self._backpack: Backpack = backpack
        super().__init__(self._backpack.content["sword"].attack)

    def attack(self) -> int:
        """Сила удара воина."""
        if self._backpack.content.get("sword"):
            return self._backpack.content["sword"].attack
        return 0

    def defense(self, opponent_attack: int) -> int:
        """Сила защиты воина."""
        return opponent_attack // 2

    def __repr__(self) -> str:
        """Тип атаки."""
        return "воин"


class HeroArcherStrategy(ArcherStrategy):
    """Стратегия Лучник."""

    def __init__(self, backpack: Backpack) -> None:
        """Инициализация стратегии."""
        self._backpack: Backpack = backpack
        super().__init__(self._backpack.content["arch"].attack)

    # def __init__(self, arch: Arch, arrows: Arrows) -> None:
    #     """Инициализация стратегии."""
    #     self.arch: Arch = arch
    #     self.arrows: Arrows = arrows
    #     super().__init__(self.arch.attack)

    def attack(self) -> int:
        """Сила атаки лучника."""
        if self._backpack.content.get("arch") and self._backpack.content.get("arrows"):
            if self._backpack.content["arrows"].arrows_count <= 0:
                return 0
            self._backpack.content["arrows"].down_count(1)
        return self._backpack.content["arch"].attack

    # def defense(self, opponent_attack: int) -> int:
    #     """Сила защиты лучника."""
    #     return opponent_attack // 2

    # def __repr__(self) -> str:
    #     """Тип атаки."""
    #     return "лучник"


class HeroMagicianStrategy(MagicianStrategy):
    """Стратегия Маг."""

    def __init__(self, backpack: Backpack) -> None:
        """Инициализация стратегии."""
        self._backpack: Backpack = backpack
        super().__init__(self._backpack.content["magic_book"].attack)

    def attack(self) -> int:
        """Сила атаки мага."""
        if self._backpack.content.get("magic_book"):
            return self._backpack.content["magic_book"].attack
        return 0

    def defense(self, opponent_attack: int) -> int:
        """Сила защиты мага."""
        return opponent_attack // 2

    # def __repr__(self) -> str:
    #     """Тип атаки."""
    #     return "маг"
