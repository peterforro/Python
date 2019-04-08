class Player:

    def __init__(self, castles):
        self.life = 10
        self.castles = castles


    def get_life(self):
        return self.life



    def act(self):
        castle_id = int(input(f'Select Castle! (1-{len(self.castles)}): '))
        castle = self.castles[castle_id-1]
        room_id = input(f'Select Room! (1-{castle.get_room_number()}): ')

