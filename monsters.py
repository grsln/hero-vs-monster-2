from character import Character


class Monster(Character):
    """Персонаж Чудовище."""

    def __init__(self):
        """Инициализация чудовища."""
        super().__init__()
        self.hp = 100

    def battle(self, opponent: Character) -> None:
        """Обработка удара противника."""
        print(self.strategy)
        self.hp -= opponent.strategy.attack()

# class Monster(ABC):
#     """Абстрактный класс игрового противника."""
#
#     def __init__(self):
#         self.hp = 100
#
#     @abstractmethod
#     def attack(self):
#         """Метод, наличие которого обязательно у всех."""
#         pass
#
#
# class WarriorMonster(Monster):
#
#     def attack(self):
#         return 3
#
#
# class ArcherMonster(Monster):
#
#     def attack(self):
#         return 2
#
#
# class MagicianMonster(Monster):
#
#     def attack(self):
#         return 1
#
#
# class MonsterFactory(ABC):
#     """Абстрактная фабрика игрового противника."""
#
#     @abstractmethod
#     def create_monster(self):
#         """Создание абстрактного продукта."""
#         pass
#
#
# class WarriorMonsterFactory(MonsterFactory):
#     """Конкретная фабрика игрового противника."""
#
#     def create_monster(self):
#         return WarriorMonster()
#
#
# class ArcherMonsterFactory(MonsterFactory):
#     """Конкретная фабрика игрового противника."""
#
#     def create_monster(self):
#         return ArcherMonster()
#
#
# class MagicianMonsterFactory(MonsterFactory):
#     """Конкретная фабрика игрового противника."""
#
#     def create_monster(self):
#         return MagicianMonster()
#
#
# spawner_to_factory_mapping = {
#     "warrior_monster": WarriorMonsterFactory,
#     "archer_monster": ArcherMonsterFactory,
#     "magician_monster": MagicianMonsterFactory
# }
#
# enemy_type_list = ["warrior_monster", "archer_monster", "magician_monster"]
