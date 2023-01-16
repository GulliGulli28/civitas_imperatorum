from Classes.Class_Building.Building import Building

class Engineer_post(Building):

    def __init__(self,positionX,positionY,idi):
        super().__init__("engineer post",positionX, positionY,1,0,100,idi)
