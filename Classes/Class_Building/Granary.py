from Classes.Class_Building.Building import Building


class Granary(Building):
    stockMax = 2600
    stock = 0

    def __init__(self, positionX, positionY, size, capacity, price, idi):
        super().__init__("granary", positionX, positionY, size, capacity, price, idi)
        self.stockMax = 2600
        self.stock = 0


    def add_food(self, stock):
        self.stock += stock
