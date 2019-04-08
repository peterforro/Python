from random import randint


class Creature:

    BLUFFING_LIMIT = 30

    def __init__(self):
        self.alive = True


    def is_alive(self):
        return self.is_alive


    def fight(self):
        self.alive = False


    def bluffing(self):
        if randint(1,100) <= Creature.BLUFFING_LIMIT:
            self.alive = False

    