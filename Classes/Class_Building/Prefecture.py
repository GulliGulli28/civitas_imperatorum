from Classes.Class_Building.Building import Building


class Prefecture(Building):

    def __init__(self,positionX,positionY,idi):
        super().__init__("prefecture", positionX, positionY, 1 , 1, 10, idi)
