from Classes.Class_Building.Building import Building


class Prefecture(Building):

    def __init__(self, positionX, positionY, size, capacity, price, idi):
        super().__init__(positionX, positionY, size, capacity, price, idi)
