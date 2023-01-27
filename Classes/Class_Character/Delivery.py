from Classes.Class_Character.Character import Character


class Delivery(Character):

    def __init__(self, positionX, positionY, direction,  origin, dest):
        super().__init__(positionX, positionY, direction)
        self.origin = origin
        self.dest = dest

    def move(self, map_build, origin, dest):
        pass
