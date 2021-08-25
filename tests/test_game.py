import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from apple import Apple
from backpack_items import Sword, Totem
from battle import Battle, HeroComponent, MonsterComponent
from hero_strategies import HeroWarriorStrategy
from main import Game


class TestHeroComponent:
    def test_first_strategy(self):
        hero = HeroComponent()
        assert hero.strategy.__class__ == HeroWarriorStrategy

    def test_hero_monster_counter(self):
        hero = HeroComponent()
        assert hero.monster_counter == 0

    def test_hero_kill_monster(self):
        hero = HeroComponent()
        hero.kill_monster()
        assert hero.monster_counter == 1


class TestBattle:
    def test_battle(self, monkeypatch):
        hero = HeroComponent()
        monster = MonsterComponent()
        battle = Battle(hero, monster)
        monkeypatch.setattr('builtins.input', lambda _: "4")
        battle.start()
        assert hero.monster_counter == 0


class TestMemento:
    def test_snapshot(self):
        game = Game()
        game.hero.backpack.add_to_backpack(Sword())
        totem = Totem(originator=game)
        totem.backup()
        game.hero.backpack.add_to_backpack(totem)
        game.hero.hp = 9
        del totem
        game.hero.backpack.content['totem'].undo()
        assert game.hero.hp == 20


class TestApple:
    def test_apple(self):
        apple = Apple()
        assert 0 < apple.life < apple.MAX_LIFE
