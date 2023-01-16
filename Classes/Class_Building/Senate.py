from Classes.Class_Building.Building import Building


class Senate(Building):
    fireProtection = 0
    damageProtection = 0

    def __init__(self,positionX,positionY,idi):
        self.fireProtection = 0
        self.damageProtection = 0
        super().__init__("senate",positionX,positionY,1,10,15,idi)
        self.name = "senate"
