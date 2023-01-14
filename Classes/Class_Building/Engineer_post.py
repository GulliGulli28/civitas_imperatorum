from Classes.Class_Building.Building import Building


class Engineer_post(Building):

    def __init__(self, positionX, positionY, size, capacity, price, idi):
        super().__init__(positionX, positionY, size, capacity, price, idi)
