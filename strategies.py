from abc import ABC, abstractmethod


class Strategy(ABC):
    """
    Интерфейс Стратегии объявляет операции, общие для всех поддерживаемых версий
    некоторого алгоритма.

    Контекст использует этот интерфейс для вызова алгоритма, определённого
    Конкретными Стратегиями.
    """

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defense(self, attack_power: int) -> int:
        pass


"""
Конкретные Стратегии реализуют алгоритм, следуя базовому интерфейсу Стратегии.
Этот интерфейс делает их взаимозаменяемыми в Контексте.
"""


class WarriorStrategy(Strategy):
    def attack(self) -> int:
        return 5

    def defense(self, attack_power: int) -> int:
        return attack_power // 2


class ArcherStrategy(Strategy):
    def attack(self) -> int:
        return 2

    def defense(self, attack_power: int) -> int:
        return attack_power // 3


class MagicianStrategy(Strategy):
    def attack(self) -> int:
        return 1

    def defense(self, attack_power: int) -> int:
        return attack_power // 4
