from backpack_items import Arch, Arrows, MagicBook, Sword
from strategies import Strategy


class HeroWarriorStrategy(Strategy):
    """Стратегия Воин."""

    def __init__(self, sword: Sword) -> None:
        """Инициализация стратегии."""
        self.sword: Sword = sword

    def attack(self) -> int:
        """Сила удара воина."""
        return self.sword.attack

    def defense(self, attack_power: int) -> int:
        """Сила защиты воина."""
        return attack_power // 2

    def change(self, sword: Sword) -> None:
        """Замена меча."""
        self.sword = sword

    def __repr__(self) -> str:
        """Тип атаки."""
        return "воин"


class HeroArcherStrategy(Strategy):
    """Стратегия Лучник."""

    def __init__(self, arch: Arch, arrows: Arrows) -> None:
        """Инициализация стратегии."""
        self.arch: Arch = arch
        self.arrows: Arrows = arrows

    def attack(self) -> int:
        """Сила атаки лучника."""
        self.arrows.down_count(1)
        return self.arch.attack

    def defense(self, attack_power: int) -> int:
        """Сила защиты лучника."""
        return attack_power // 2

    def change(self, arch: Arch) -> None:
        """Замена лука."""
        self.arch = arch

    def __repr__(self) -> str:
        """Тип атаки."""
        return "лучник"


class HeroMagicianStrategy(Strategy):
    """Стратегия Маг."""

    def __init__(self, magic_book: MagicBook):
        """Инициализация стратегии."""
        self.magic_book: MagicBook = magic_book

    def attack(self) -> int:
        """Сила атаки мага."""
        return self.magic_book.attack

    def defense(self, attack_power: int) -> int:
        """Сила защиты мага."""
        return attack_power // 2

    def change(self, magic_book: MagicBook) -> None:
        """Замена книги."""
        self.magic_book = magic_book

    def __repr__(self) -> str:
        """Тип атаки."""
        return "маг"
