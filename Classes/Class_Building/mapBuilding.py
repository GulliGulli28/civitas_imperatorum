import Building
import Road


class mapBuilding():
    def __init__(self):
        self.sizeX = 50
        self.sizeY = 50
        self.map = [[None for j in range(self.sizeY)] for i in range(self.sizeX)]

    def add_build(self, newbuild):
        self.map[newbuild.positionX][newbuild.positionY] = Building
        if newbuild.size > 1:
            for i in range(newbuild.size):
                i += 1
                p = Pointeur()
                for y in range(i):
                    self.map[newbuild.positionX + i][newbuild.positionY + y] = p
                    self.map[newbuild.positionX + y][newbuild.positionY + i] = p
                self.map[newbuild.positionX + i][newbuild.positionY + i] = p

    def get_direction(self, positionX, positionY):
        """
        Method used by a Character to get the possible future direction

        Args:
            positionX (int): Position on axis X of the Character.
            positionY (int): Position on axis Y of the Character.

        Returns:
            res list<direction>: list of the possible direction.
        """
        res = []
        if isinstance(self.map[positionX][positionY + 1], Road):
            res.append("NW")
        if isinstance(self.map[positionX][positionY - 1], Road):
            res.append("SE")
        if isinstance(self.map[positionX + 1][positionY], Road):
            res.append("NE")
        if isinstance(self.map[positionX - 1][positionY], Road):
            res.append("SW")
        return res
