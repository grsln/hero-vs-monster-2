import random

from game import Battle
from hero import Hero
from monsters import Monster, MonstersTypes

if __name__ == "__main__":
    random_monster_type = random.choice(list(MonstersTypes))
    random_monster_class = random_monster_type.value[0]
    print(random_monster_class)
    mn = Monster(random_monster_class())
    print(mn.strategy)
    hr = Hero()
    game = Battle(hr, mn)
    game.start()
