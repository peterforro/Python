from random import randint
from Room import Room



class Castle:

    instance_counter = 0

    def __init__(self):
        Castle.instance_counter += 1
        self.__id = Castle.instance_counter
        self.__rooms = []
        for i in range(randint(1,10)):
            self.__rooms.append(Room())
        

    def get_room_number(self):
        return len(self.__rooms)


    def get_room(self, idx):
        return self.__rooms[idx]


    def is_free_rooms(self):
        for room in self.__rooms:
            if room.is_free():
                return True
        return False


    def __str__(self):
        available_rooms = []
        for i,room in enumerate(self.__rooms):
            if room.is_free():
                available_rooms.append(str(i+1))
        return 'Available rooms: ' + ', '.join(available_rooms)