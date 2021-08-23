import random
from typing import Dict, Type, Union


class Sword:
    """Меч."""

    name = "sword"
    MAX_ATTACK = 10

    def __init__(self) -> None:
        """Инициализация предмета Меч."""
        self.attack = random.randrange(1, self.MAX_ATTACK)


class Arch:
    """Лук."""

    name = "arch"
    MAX_ATTACK = 8

    def __init__(self) -> None:
        """Инициализация предмета Лук."""
        self.attack = random.randrange(1, self.MAX_ATTACK)


class Arrows:
    """Стрелы."""

    name = "arrows"
    MAX_ARROWS = 10

    def __init__(self) -> None:
        """Инициализация предмета Стрелы."""
        self.arrows_count = random.randrange(1, self.MAX_ARROWS)

    def up_count(self, arrows: int) -> None:
        """Добавление стрел."""
        self.arrows_count += arrows

    def down_count(self, arrows: int) -> None:
        """Уменьшение количества стрел."""
        self.arrows_count -= arrows


class MagicBook:
    """Книга заклинаний."""

    name = "magic_book"
    MAX_ATTACK = 5

    def __init__(self) -> None:
        """Инициализация предмета Книга заклинаний."""
        self.attack = random.randrange(1, self.MAX_ATTACK)


class Totem:
    """Тотем."""

    name = "totem"


UnionBackpackItems = Union[Sword, Arch, Arrows, MagicBook, Totem]
TypeBackpackItems = Type[UnionBackpackItems]
BackpackItems: Dict[str, TypeBackpackItems] = {
    "sword": Sword,
    "arch": Arch,
    "arrows": Arrows,
    "magic_book": MagicBook,
    "totem": Totem,
}
d = [Sword(), Arch()]
