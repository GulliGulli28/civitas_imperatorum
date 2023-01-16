from Classes.Class_Building.Building import Building


class Market(Building):

    def __init__(self,positionX,positionY,idi):
        super().__init__("market",positionX,positionY,4,50,50,idi)
