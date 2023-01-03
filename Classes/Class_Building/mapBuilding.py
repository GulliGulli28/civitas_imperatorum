import Building
import Road
import Pointeur


class mapBuilding():
    def __init__(self):
        self.sizeX = 50
        self.sizeY = 50
        self.map = [[None for j in range(self.sizeY)] for i in range(self.sizeX)]
        self.graph = {}

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

    def update_graph(self, pos):
        """
        Method used to update the graph of the road with the intersection.

        Args:
            pos (int,int): Position of the road just added.

        Returns:
            graph the graph updated
        """
        if len(self.graph) < 1:
            self.graph = {pos: {}}
        else:
            (x, y) = pos
            direct = self.get_direction(self, x, y)
            if len(direct) > 1:
                for i in range(1, direct):
                    distance = self.calcule_distance(pos, i)  # TODO résoudre ce mystère
                    self.add_dist2graph(self, pos, distance)

    def calcule_distance(self, pos, i):
        distance = 0
        stop = False
        while stop == False:
            old_pos = pos
            pos += i
            distance += 1
            (x, y) = pos
            if len(self.get_direction(x,y))==2:
                #normal
            elif len(self.get_direction(x,y))!=2:
                #fin de route

        return distance



