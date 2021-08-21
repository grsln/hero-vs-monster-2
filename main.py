from game import Battle
from hero import Hero
from monsters import Monster

if __name__ == "__main__":
    mn = Monster()
    hr = Hero()
    game = Battle(hr, mn)
    game.start()
