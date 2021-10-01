import random
from typing import Any, Dict, Type, Union


class Sword:
    """Меч."""

    name = "sword"
    MAX_ATTACK = 10

    def __init__(self) -> None:
        """Инициализация предмета Меч."""
        self.attack = random.randrange(1, self.MAX_ATTACK)

    def __repr__(self) -> str:
        """Название предмета."""
        return f"Меч(сила атаки:{self.attack})"


class Arch:
    """Лук."""

    name = "arch"
    MAX_ATTACK = 4

    def __init__(self) -> None:
        """Инициализация предмета Лук."""
        self.attack = random.randrange(1, self.MAX_ATTACK)

    def __repr__(self) -> str:
        """Название предмета."""
        return f"Лук(сила атаки:{self.attack})"


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

    def __repr__(self) -> str:
        """Название предмета."""
        return f"Стрелы({self.arrows_count}шт.)"


class MagicBook:
    """Книга заклинаний."""

    name = "magic_book"
    MAX_ATTACK = 5

    def __init__(self) -> None:
        """Инициализация предмета Книга заклинаний."""
        self.attack = random.randrange(1, self.MAX_ATTACK)

    def __repr__(self) -> str:
        """Название предмета."""
        return f"Книга заклинаний(сила атаки:{self.attack})"


class Totem:
    """Тотем."""

    name = "totem"

    def __init__(self, originator: Any) -> None:
        """Инициализация тотема."""
        self._snapshot = None
        self._originator = originator

    def backup(self) -> None:
        """Сохранение игры."""
        self._snapshot = self._originator.save()

    def undo(self) -> None:
        """Восстановление игры."""
        self._originator.restore(self._snapshot)

    def __repr__(self) -> str:
        """Название предмета."""
        return "Тотем"


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
