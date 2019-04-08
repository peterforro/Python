from random import randint
from Room import Room


class Castle:

    instance_counter = 0

    def __init__(self):
        Castle.instance_counter += 1
        self.id = Castle.instance_counter
        self.rooms = []
        for i in range(randint(1,10)):
            self.rooms.append(Room())
        

    def get_room_number(self):
        return len(self.rooms)



    def __str__(self):
        return ', '.join([room.id for room in self.rooms])