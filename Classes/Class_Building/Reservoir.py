from Classes.Class_Building.Building import Building


class Reservoir(Building):
    isSupplied = None

    def __init__(self,positionX,positionY,idi):
        self.isSupplied = False
        super().__init__("well",positionX, positionY, 1 , 0, 15, idi)
