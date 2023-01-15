from Classes.Class_Building.Building import Building


class Senate(Building):
    fireProtection = 0
    damageProtection = 0

    def __init__(self):
        self.fireProtection = 0
        self.damageProtection = 0
        super.__init__()
