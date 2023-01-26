from Classes.Class_Building.Building import Building
import random
import time

class House(Building):

    def __init__(self, positionX, positionY, size, capacity, price, idi):
        super().__init__(positionX, positionY, size, capacity, price, idi)
        self.name = "housing"






