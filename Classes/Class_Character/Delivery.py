from Classes.Class_Character.Character import Character
from Classes.Class_Character.mapCharacter import mapCharacter


class Delivery(Character):

    def __init__(self, positionX, positionY, direction, origin, dest):
        super().__init__(positionX, positionY, direction)
        self.origin = origin
        self.dest = dest

    def move(self, map_build):
        if len(self.dest) > 0:
            (x, y) = self.dest[0]
            self.positionX = x
            self.positionY = y
            return False
        else:
            map_build.map[self.positionX][self.positionY].add_food(50)
            return True
