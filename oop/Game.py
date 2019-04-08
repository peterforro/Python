from Player import Player
from Castle import Castle


class Game:

    def __init__(self):
        self.castles = []
        for i in range(7):
            self.castles.append(Castle())
        self.player = Player(self.castles)




    def game(self):
        while(self.player.get_life != 0):
            self.player.act()