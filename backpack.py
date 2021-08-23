from backpack_items import Arrows


class Backpack:
    def __init__(self):
        self.content = dict()

    def add_to_backpack(self, item):
        """Добавление предмета в рюкзак."""
        if isinstance(item, Arrows):
            if item.name in self.content:
                self.content[item.name].up_count(item.arrows_count)
                return
        self.content[item.name] = item

    def remove_from_backpack(self, item):
        """Удаление предмета из рюкзака."""
        self.content.pop(item.name)
