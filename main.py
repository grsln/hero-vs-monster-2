import random

from battle import Battle, HeroComponent, MonsterComponent
from monsters import MonstersTypes

if __name__ == "__main__":
    random_monster_type = random.choice(list(MonstersTypes.keys()))
    mn = MonsterComponent(MonstersTypes[random_monster_type]())
    print(mn.strategy)
    hr = HeroComponent()
    game = Battle(hr, mn)
    game.start()
