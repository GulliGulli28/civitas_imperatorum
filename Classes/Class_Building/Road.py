from Classes.Class_Building.Building import Building


class Road(Building):

    def __init__(self, x, y):
        super().__init__("road",x, y, 1, 0, 0, 0)
