import random

from apple import Apple
from backpack_items import BackpackItems
from battle import Battle, HeroComponent, MonsterComponent
from monsters import MonstersTypes


def monster_step() -> None:
    """Выполнение шага monster(встреча с чудовищем)."""
    random_monster_type = random.choice(list(MonstersTypes.keys()))
    print(random_monster_type)
    random_monster = MonsterComponent(MonstersTypes[random_monster_type]())
    battle = Battle(hero, random_monster)
    battle.start()


def object_step() -> None:
    """Выполнение шага object(обнаружение предмета)."""
    random_backpack_item = BackpackItems[random.choice(list(BackpackItems.keys()))]
    print(random_backpack_item)
    hero.backpack.add_to_backpack(random_backpack_item())


def apple_step() -> None:
    """Выполнение шага apple(обнаружение яблока)."""
    hero.eat_apple(Apple())


if __name__ == "__main__":
    steps = {"monster": monster_step, "object": object_step, "apple": apple_step}
    hero = HeroComponent()
    while hero.hp > 0:
        print(hero.backpack.content)
        steps[random.choice(list(steps.keys()))]()
