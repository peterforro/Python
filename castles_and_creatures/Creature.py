from random import randint


class Creature:

    BLUFFING_LIMIT = 30

    def __init__(self):
        self.__alive = True


    def is_alive(self):
        return self.__alive


    def fight(self):
        self.__alive = False


    def bluffing(self):
        if randint(1,100) <= Creature.BLUFFING_LIMIT:
            self.__alive = False
            return True
        return False
    