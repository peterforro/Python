from Creature import Creature
from Treausure import Treasure


class Room:
    
    instance_counter = 0

    def __init__(self):
        Room.instance_counter += 1
        self.__id = Room.instance_counter
        self.__creature = Creature()
        self.__treasure = Treasure()

    
    def is_free(self):
        return self.__creature.is_alive()
    
    
    def get_treasure_value(self):
        return self.__treasure.get_value()


    def get_creature(self):
        return self.__creature


    def __str__(self):
        return self.__id


