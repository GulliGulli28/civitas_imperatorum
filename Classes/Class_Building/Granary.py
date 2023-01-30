from Classes.Class_Building.Building import Building


class Granary(Building):
    stockMax = 2600
    stock = 0

<<<<<<< HEAD
    def __init__(self,positionX,positionY,idi):
        self.stockMax = 2600
        self.stock = 0
        super().__init__("granary", positionX, positionY, 1 , 5, 20, idi)
=======
    def __init__(self, positionX, positionY, size, capacity, price, idi, road):
        self.stockMax = 2600
        self.stock = 0
        super().__init__(positionX, positionY, size, capacity, price, idi)
        self.road = road

>>>>>>> Quentin/Guillaume

    def add_food(self, stock):
        self.stock += stock
