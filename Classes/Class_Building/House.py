from Classes.Class_Building.Building import Building

class House(Building):

    def __init__(self, positionX, positionY, idi):
        super().__init__("house",positionX, positionY, 1 , 10, 10, idi)
