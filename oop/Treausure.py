from random import randint

class Treasure:

    def __init__(self):
        self.value = randint(50,100)


    def get_value(self):
        return self.value
