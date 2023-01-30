from Classes.Class_Building.Building import Building


class Pointeur(Building):

    def __init__(self, x, y, idi):
        super().__init__("road", x, y, 1, 0, 0, idi)
