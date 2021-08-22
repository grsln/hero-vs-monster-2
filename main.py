import random

from battle import Battle
from hero import Hero
from monsters import Monster, MonstersTypes

if __name__ == "__main__":
    random_monster_type = random.choice(list(MonstersTypes.keys()))
    mn = Monster(MonstersTypes[random_monster_type]())
    print(mn.strategy)
    hr = Hero()
    game = Battle(hr, mn)
    game.start()
