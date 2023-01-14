from Classes.Class_Building.Building import Building


class Reservoir(Building):
    isSupplied = None

    def __init__(self, positionX, positionY, size, capacity, price, idi):
        self.isSupplied = False
        super().__init__(positionX, positionY, size, capacity, price, idi)
