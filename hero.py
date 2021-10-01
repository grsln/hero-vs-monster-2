from apple import Apple
from backpack import Backpack
from backpack_items import Sword
from character import HeroCharacter
from hero_strategies import HeroArcherStrategy, HeroMagicianStrategy, HeroWarriorStrategy
from monsters import Monster


class Hero(HeroCharacter):
    """Персонаж Рыцарь."""

    HERO_HP = 20
    MONSTER_STATE_STR = "Урон от чудовища:{} защита рыцаря от атаки:{}"
    NO_ARCH_OR_ARROWS_STR = "В рюкзаке нет лука или стрел. Тип атаки:{}"
    NO_MAGIC_BOOK_STR = "В рюкзаке нет книги заклинаний. Тип атаки:{}"
    APPLE_STR = "Рыцарь съел яблоко. Жизнь увеличилась на {}. Всего жизней:{}"

    def __init__(self) -> None:
        """Инициализация рыцаря."""
        self.backpack = Backpack()
        self.backpack.add_to_backpack(Sword())
        warrior_strategy = HeroWarriorStrategy(self.backpack)
        super().__init__(warrior_strategy)
        self.hp = self.HERO_HP

    def eat_apple(self, apple: Apple) -> None:
        """Добавление hp рыцарю."""
        self.hp += apple.life
        print(self.APPLE_STR.format(apple.life, self.hp))

    def battle(self, monster: Monster) -> None:
        """Обработка удара монстра."""
        monster_attack = monster.strategy.attack()
        defense = 0
        if isinstance(monster.strategy, self.strategy.__class__.__bases__):
            defense = self.strategy.defense(monster_attack)
        print(self.MONSTER_STATE_STR.format(monster_attack, defense))
        self.hp -= monster_attack - defense

    def set_sword_strategy(self) -> None:
        """Установка стратегии WarriorStrategy."""
        if "sword" in self.backpack.content:
            self._strategy = HeroWarriorStrategy(self.backpack)

    def set_archer_strategy(self) -> None:
        """Установка стратегии ArcherStrategy."""
        if "arch" in self.backpack.content and "arrows" in self.backpack.content:
            self._strategy = HeroArcherStrategy(self.backpack)
        else:
            print(self.NO_ARCH_OR_ARROWS_STR.format(self.strategy))

    def set_magician_strategy(self) -> None:
        """Установка стратегии MagicianStrategy."""
        if "magic_book" in self.backpack.content:
            self._strategy = HeroMagicianStrategy(self.backpack)
        else:
            print(self.NO_MAGIC_BOOK_STR.format(self.strategy))
