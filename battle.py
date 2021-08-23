from abc import ABC, abstractmethod
from typing import Optional

from hero import Hero
from monsters import Monster


class Mediator(ABC):
    """Посредник для боя между рыцарем и чудовищем."""

    @abstractmethod
    def start(self) -> None:
        """Запуск боя."""
        pass


class BaseComponent:
    """Базовый Компонент обеспечивает хранение экземпляра посредника внутри объектов."""

    def __init__(self, mediator_arg: Mediator = None) -> None:
        """Инициализация посредника."""
        self._mediator = mediator_arg

    @property
    def mediator(self) -> Optional[Mediator]:
        """Ссылка на посредника."""
        return self._mediator

    @mediator.setter
    def mediator(self, mediator_arg: Mediator) -> None:
        """Установка посредника."""
        self._mediator = mediator_arg


class HeroComponent(Hero, BaseComponent):
    """Класс Hero для взаимодействия с посредником."""

    pass


class MonsterComponent(Monster, BaseComponent):
    """Класс Monster для взаимодействия с посредником."""

    pass


class Battle(Mediator):
    """Посредник для боя между рыцарем и чудовищем."""

    def __init__(self, hero: HeroComponent, monster: MonsterComponent) -> None:
        """Инициализация боя."""
        self._hero = hero
        self._hero.mediator = self
        self._monster = monster
        self._monster.mediator = self

    def start(self) -> None:
        """Запуск боя."""
        while self._hero.hp > 0 and self._monster.hp > 0:
            print("monster hp:", self._monster.hp)
            print("hero hp:", self._hero.hp)
            id_strategy = input("Выберите тип атаки(1-воин, 2-лучник, 3-маг, 4-убежать):")
            if id_strategy == "1":
                self._hero.set_sword_strategy()
            elif id_strategy == "2":
                self._hero.set_archer_strategy()
            elif id_strategy == "3":
                self._hero.set_magician_strategy()
            elif id_strategy == "4":
                break
            self._hero.battle(self._monster)
            self._monster.battle(self._hero)
