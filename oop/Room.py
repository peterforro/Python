from Creature import Creature
from Treausure import Treasure


class Room:
    
    instance_counter = 0

    def __init__(self):
        Room.instance_counter += 1
        self.id = Room.instance_counter
        self.creature = Creature()
        self.treasure = Treasure()

    
    def is_free(self):
        return self.creature.is_alive()
    
    
    def get_treasure_value(self):
        return self.treasure.get_value()


    def __str__(self):
        return self.id


