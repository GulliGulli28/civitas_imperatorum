import random
import time

from Classes.Class_Building.Building import Building
from Classes.Class_Character.Resident import Resident


class House(Building):

    def __init__(self, positionX, positionY, idi):
        super().__init__("house",positionX, positionY, 1 , 10, 10, idi)
        

    def update_level(self, level, map_char):
        self.level += level
        c = Resident(self.road[0], self.road[1], (0, 0))
        map_char.add_character(c)





