from typing import Dict

from backpack_items import Arrows, TypeBackpackItems, UnionBackpackItems


class Backpack:
    """Рюкзак для найденных предметов."""

    def __init__(self) -> None:
        """Инициализация рюкзака."""
        self.content: Dict[str, UnionBackpackItems] = dict()

    def add_to_backpack(self, item: UnionBackpackItems) -> None:
        """Добавление предмета в рюкзак."""
        if isinstance(item, Arrows):
            if item.name in self.content.keys():
                arrows: Arrows = self.content[item.name]
                arrows.up_count(item.arrows_count)
                return
        self.content[item.name] = item

    def remove_from_backpack(self, item: TypeBackpackItems) -> None:
        """Удаление предмета из рюкзака."""
        self.content.pop(item.name)
