import random


class Sword:
    name = 'sword'
    MAX_ATTACK = 10

    def __init__(self):
        self.attack = random.randrange(1, self.MAX_ATTACK)

    def update(self, attack):
        self.attack = attack


class Arch:
    name = 'arch'
    MAX_ATTACK = 8

    def __init__(self):
        self.attack = random.randrange(1, self.MAX_ATTACK)

    def update(self, attack):
        self.attack = attack


class Arrows:
    name = 'arrows'
    MAX_ARROWS = 10

    def __init__(self, ):
        self.arrows_count = random.randrange(1, self.MAX_ARROWS)

    def up_count(self, arrows):
        self.arrows_count += arrows

    def down_count(self, arrows):
        self.arrows_count -= arrows


class MagicBook:
    name = 'magic_book'
    MAX_ATTACK = 5

    def __init__(self):
        self.attack = random.randrange(1, self.MAX_ATTACK)


class Totem:
    name = 'totem'


BackpackItems = {"sword": Sword, "arch": Arch, "arrows": Arrows, 'magic_book': MagicBook, 'totem': Totem}
