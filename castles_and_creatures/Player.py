
class Player:


    def __init__(self, castles):
        self.__life = 10
        self.__treasure = 0
        self.__castles = castles



    def get_life(self):
        return self.__life



    def select_castle(self, castles):
        try:
            castle_id = int(input(f'Select Castle! (1-{len(castles)}): '))
            return self.__castles[castle_id-1]
        except Exception:
            self.select_castle(castles)



    def select_room(self, castle):
        try:
            print(castle)
            room_id = int(input(f'Select Room! (1-{castle.get_room_number()}): '))
            return castle.get_room(room_id - 1)
        except Exception:
           self.select_room(castle)



    def fight(self, room):
        room.get_creature().fight()
        self.__life -= 1
        self.__treasure += room.get_treasure_value()
        print(f'You killed the monster! HP={self.__life}')



    def bluff(self, room):
        if room.get_creature().bluffing():
            print('Successful bluff!')
            self.__treasure += room.get_treasure_value()
        else:
            print('Next time Bro!')



    def interact_room(self, room):
        if room.is_free():
            option = int(input('Fight or Bluff? (1-2): '))
            if option == 1:
                self.fight(room)
            elif option == 2:
                self.bluff(room)    



    def act(self):
        castle = self.select_castle(self.__castles)
        room = self.select_room(castle)
        self.interact_room(room)        

