from Player import Player
from Castle import Castle
from os import system


class Game:


    def __init__(self):
        self.__turn_counter = 0
        self.__castles = []
        for i in range(7):
            self.__castles.append(Castle())
        self.player = Player(self.__castles)


    def game(self):
        system('clear')
        while(self.player.get_life != 0):
            self.__turn_counter += 1
            print(f'----------------- TURN: {self.__turn_counter} -----------------')
            self.player.act()
            print('\n')