from copy import deepcopy

from battle import HeroComponent


class Snapshot:
    """Точка восстановления игры."""

    def __init__(self, hero: HeroComponent) -> None:
        """Инициализация точки восстановления игры."""
        self.hero = deepcopy(hero)

    def get_state(self) -> HeroComponent:
        """Функция возвращает сохраненное состояние."""
        return self.hero
