from Classes.Class_Building.Building import Building


class Granary(Building):
    stockMax = 2600
    stock = None

    def __init__(self, positionX, positionY, size, capacity, price, idi):
        self.stockMax = 2600
        self.stock = 0
        super().__init__(positionX, positionY, size, capacity, price, idi)
