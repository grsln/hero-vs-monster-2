from abc import ABC, abstractmethod

from hero import Hero
from monsters import Monster


class Mediator(ABC):
    """
    Интерфейс Посредника предоставляет метод, используемый компонентами для
    уведомления посредника о различных событиях. Посредник может реагировать на
    эти события и передавать исполнение другим компонентам.
    """

    @abstractmethod
    def start(self) -> None:
        pass


# class Game(Mediator):
class Battle(Mediator):
    def __init__(self, hero: Hero, monster: Monster) -> None:
        self._hero = hero
        self._hero.mediator = self
        self._monster = monster
        self._monster.mediator = self

    def start(self):
        while self._hero.hp > 0 and self._monster.hp > 0:
            print("monster hp:", self._monster.hp)
            print("hero hp:", self._hero.hp)
            id_strategy = input("1-воин, 2-лучник, 3-маг, 4-убежать:")
            if id_strategy == '1':
                self._hero.set_sword_strategy()
            elif id_strategy == '2':
                self._hero.set_archer_strategy()
            elif id_strategy == '3':
                self._hero.set_magician_strategy()
            elif id_strategy == '4':
                break
            self._hero.battle(self._monster)
            self._monster.battle(self._hero)


class BaseComponent:
    """
    Базовый Компонент обеспечивает базовую функциональность хранения экземпляра
    посредника внутри объектов компонентов.
    """

    def __init__(self, mediator_arg: Mediator = None) -> None:
        self._mediator = mediator_arg

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator_arg: Mediator) -> None:
        self._mediator = mediator_arg


"""
Конкретные Компоненты реализуют различную функциональность. Они не зависят от
других компонентов. Они также не зависят от каких-либо конкретных классов
посредников.
"""

# class MonsterComponent(Monster, BaseComponent):
#     def do_a(self) -> None:
#         print("Component 1 does A.")
#         self.mediator.notify(self, "A")
#
#     def do_b(self) -> None:
#         print("Component 1 does B.")
#         self.mediator.notify(self, "B")


# class HeroComponent(Hero,BaseComponent):
#     def do_c(self) -> None:
#         print("Component 2 does C.")
#         self.mediator.notify(self, "C")
#
#     def do_d(self) -> None:
#         print("Component 2 does D.")
#         self.mediator.notify(self, "D")


if __name__ == "__main__":
    # Клиентский код.
    c1 = Hero()
    c2 = Monster()
    mediator = Battle(c1, c2)
    mediator.start()
    # print("Client triggers operation A.")
    # c1.do_a()
    #
    # print("\n", end="")
    #
    # print("Client triggers operation D.")
    # c2.do_d()
    #
    # enemy_type_list = ["ogre", "skeleton", "goblin"]
    #
    # for i in range(10):
    #     SPAWNER_TYPE = random.choice(enemy_type_list)
    #
    #     spawner = spawner_to_factory_mapping[SPAWNER_TYPE]()
    #
    #     enemy = spawner.create_monster()
    #     action = enemy.attack()
    #     print(action)
