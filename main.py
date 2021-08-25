import random
from typing import Union

from apple import Apple
from backpack_items import Arch, BackpackItems, MagicBook, Sword, Totem
from battle import Battle, HeroComponent, MonsterComponent
from hero_strategies import HeroArcherStrategy, HeroMagicianStrategy, HeroWarriorStrategy
from snapshot import Snapshot


class Game:
    """Игра Герой и Чудовища 2: волшебный тотем."""

    MONSTERS_FOR_WIN = 10
    VICTORY = "ПОБЕДА!"
    LOSE = "ПОРАЖЕНИЕ! игра окончена"
    PRESS_ENTER = "Нажмите Enter"
    KILL_MONSTERS_STR = "Количество убитых чудовищ:"
    HERO_FIND_STR = "Рыцарь нашел предмет:"
    TAKE_PASS_STR = "Введите 1 или 2 (1 -взять предмет, 2 - пройти мимо):"
    COEFFICIENT_STRATEGY = 1.5

    def __init__(self) -> None:
        """Инициализация игры."""
        self.steps = {"monster": self.monster_step, "object": self.object_step, "apple": self.apple_step}
        self.hero = HeroComponent()

    def start(self) -> None:
        """Запуск игры."""
        while (
            self.hero.hp > 0
            and (self.hero.monster_counter < self.MONSTERS_FOR_WIN)
            or self.hero.hp <= 0
            and self.hero.backpack.content.get("totem")
        ):
            if self.hero.hp <= 0:
                answer = input("Поражение. Воспользоваться тотемом?(1-да, 2-нет):")
                if answer == "1":
                    self.hero.backpack.content.get("totem").undo()
                    if self.hero.backpack.content.get("totem"):
                        self.hero.backpack.content.pop("totem")
                else:
                    break
            print(self.KILL_MONSTERS_STR, self.hero.monster_counter)
            print(self.hero.backpack)
            self.steps[random.choice(list(self.steps.keys()))]()
            # input(PRESS_ENTER)
        if self.hero.hp <= 0 or self.hero.monster_counter < self.MONSTERS_FOR_WIN:
            print(self.LOSE)
        else:
            print(self.VICTORY)

    def monster_step(self) -> None:
        """Выполнение шага monster(встреча с чудовищем)."""
        random_monster = MonsterComponent()
        battle = Battle(self.hero, random_monster)
        battle.start()

    def is_weapon_equal_strategy(self, backpack_item: Union[Sword, Arch, MagicBook]) -> bool:
        """Проверка соответствия оружия стратегии."""
        return (
            isinstance(backpack_item, Sword)
            and isinstance(self.hero.strategy, HeroWarriorStrategy)
            or isinstance(backpack_item, Arch)
            and isinstance(self.hero.strategy, HeroArcherStrategy)
            or isinstance(backpack_item, MagicBook)
            and isinstance(self.hero.strategy, HeroMagicianStrategy)
        )

    def object_step(self) -> None:
        """Выполнение шага object(обнаружение предмета)."""
        random_backpack_type = BackpackItems[random.choice(list(BackpackItems.keys()))]
        print(random_backpack_type, Totem, random_backpack_type != Totem)
        if random_backpack_type != Totem:
            random_backpack_item = random_backpack_type()
            if self.is_weapon_equal_strategy(random_backpack_item):
                random_backpack_item.attack = int(random_backpack_item.attack * self.COEFFICIENT_STRATEGY)
        else:
            random_backpack_item = random_backpack_type(originator=self)
            random_backpack_item.backup()
        print(self.HERO_FIND_STR, random_backpack_item)
        answer = input(self.TAKE_PASS_STR)
        if answer == "1":
            self.hero.backpack.add_to_backpack(random_backpack_item)

    def apple_step(self) -> None:
        """Выполнение шага apple(обнаружение яблока)."""
        self.hero.eat_apple(Apple())

    def save(self) -> Snapshot:
        """Сохранение игры."""
        return Snapshot(self.hero)

    def restore(self, snapshot: Snapshot) -> None:
        """Восстановление сохраненной игры."""
        self.hero = snapshot.get_state()


if __name__ == "__main__":
    game = Game()
    game.start()
    exit(0)
