import random


class Apple:
    """Яблоко, добавляющее hp рыцарю."""

    name = "apple"
    MAX_LIFE = 10

    def __init__(self) -> None:
        """Инициализация яблока."""
        self.life = random.randrange(1, self.MAX_LIFE)
