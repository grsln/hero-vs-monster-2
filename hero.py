from backpack import Backpack
from character import Character
from monsters import Monster
from strategies import ArcherStrategy, MagicianStrategy, WarriorStrategy

class


class Hero(Character):
    """Персонаж Рыцарь."""

    HERO_HP = 20
    MONSTER_STATE_STR = "monster attack:{} defense:{}"
    NO_ARCH_OR_ARROWS_STR = "В рюкзаке нет лука или стрел."

    def __init__(self) -> None:
        """Инициализация рыцаря."""
        super().__init__()
        self.hp = self.HERO_HP
        self.backpack = Backpack()

    def add_hp(self, hp):
        self.hp += hp

    def battle(self, monster: Monster) -> None:
        """Обработка удара монстра."""
        monster_attack = monster.strategy.attack()
        defense = 0
        if isinstance(monster.strategy, type(self.strategy)):
            defense = self.strategy.defense(monster_attack)
        print(self.MONSTER_STATE_STR.format(monster_attack, defense))
        self.hp -= monster_attack - defense

    def set_sword_strategy(self) -> None:
        """Установка стратегии WarriorStrategy."""
        if 'sword' in self.backpack.content:
            self._strategy = WarriorStrategy()

    def set_archer_strategy(self) -> None:
        """Установка стратегии ArcherStrategy."""
        if 'arch' in self.backpack.content and 'arrows' in self.backpack.content:
            self._strategy = ArcherStrategy()
        else:
            print(self.NO_ARCH_OR_ARROWS_STR)

    def set_magician_strategy(self) -> None:
        """Установка стратегии MagicianStrategy."""
        if 'magic_book' in self.backpack.content:
            self._strategy = MagicianStrategy()
