import random


class Apple:
    name = 'apple'
    MAX_LIFE = 10

    def __init__(self):
        self.life = random.randrange(1, self.MAX_LIFE)
