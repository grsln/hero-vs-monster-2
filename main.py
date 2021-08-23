import random

from backpack_items import BackpackItems
from battle import Battle, HeroComponent, MonsterComponent
from monsters import MonstersTypes

if __name__ == "__main__":
    hr = HeroComponent()
    while hr.hp > 0:
        print(hr.backpack.content)
        if random.randint(1, 2) == 1:
            random_backpack_item = BackpackItems[random.choice(list(BackpackItems.keys()))]()
            print(random_backpack_item)
            if random_backpack_item not in hr.backpack.content:
                hr.backpack.add_to_backpack(random_backpack_item)
        else:
            random_monster_type = random.choice(list(MonstersTypes.keys()))
            print(random_monster_type)
            mn = MonsterComponent(MonstersTypes[random_monster_type]())
            game = Battle(hr, mn)
            game.start()
