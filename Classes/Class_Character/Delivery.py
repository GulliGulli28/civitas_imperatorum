from Classes.Class_Character.Character import Character
from Classes.Class_Character.mapCharacter import mapCharacter


class Delivery(Character):

    def __init__(self, positionX, positionY, dest, gra):
        super().__init__(positionX, positionY, (0, 0))
        self.dest = dest
        self.gra = gra

    def move(self, map_build):
        print("path finding :", self.dest)
        if len(self.dest) > 0:
            (x, y) = self.dest[0]
            self.positionX = x
            self.positionY = y
            del self.dest[0]
            return False
        else:
            print("JE SUIS ARRIVÉ A DESTINATION !!!!! OUAIS !!!!!")
            map_build.map[self.gra.positionX][self.gra.positionY].add_food(50)
            return True
