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

    def get_direction(self, positionX, positionY):  # TODO modifier pour retourner (x, y)
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
                    (pos2, distance) = self.calculate_distance(pos, i)
                    self.add_dist2graph(self, pos, pos2, distance)

    def calculate_distance(self, pos, i):  # TODO vérifier que c'est correct
        """
        Method used to calculate the distance between 2 intersections on the road

        Args:
            pos (int,int): Position of the road just added.
            i (int,int): The value needed to be sum with the position to get the future position

        Returns:
            pos2 (int, int): Position of the second intersection
            distance (int): The distance calculate
        :param pos:
        :param i:
        :return:
        """
        distance = 0
        stop = False
        while not stop:
            old_pos = pos
            pos += i
            distance += 1
            (x, y) = pos
            direct = self.get_direction(x, y)
            if len(direct) == 2:
                direct.remove(old_pos - pos)
                i = direct[1]
            elif len(self.get_direction(x, y)) != 2:
                pos2 = pos
                stop = True
        return pos2, distance

    def add_dist2graph(self, pos1, pos2, distance):
