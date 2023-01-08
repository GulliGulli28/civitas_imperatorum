import Building
import Road
import Pointeur  # TODO
from collections import deque


class mapBuilding():
    def __init__(self):
        self.sizeX = 50
        self.sizeY = 50
        self.map = [[None for j in range(self.sizeY)] for i in range(self.sizeX)]
        self.graph = {}

    def add_build(self, new_build):
        self.map[new_build.positionX][new_build.positionY] = Building
        if new_build.size > 1:
            for i in range(new_build.size):
                i += 1
                p = Pointeur()
                for y in range(i):
                    self.map[new_build.positionX + i][new_build.positionY + y] = p
                    self.map[new_build.positionX + y][new_build.positionY + i] = p
                self.map[new_build.positionX + i][new_build.positionY + i] = p

    def get_direction(self, positionX, positionY):  # TODO modifier pour retourner (x, y)
        """
        Method used by a Character to get the possible future direction
        W---N
        |   |
        S---E

        :param positionX: Position on axis X of the Character.
        :type positionX: int
        :param positionY: Position on axis Y of the Character.
        :type positionY: int

        Returns:
            res list<direction>: list of the possible direction.
        """
        res = []
        if isinstance(self.map[positionX][positionY + 1], Road):
            res.append((0, 1))  # NW
        if isinstance(self.map[positionX][positionY - 1], Road):
            res.append((0, -1))  # SE
        if isinstance(self.map[positionX + 1][positionY], Road):
            res.append((1, 0))  # NE
        if isinstance(self.map[positionX - 1][positionY], Road):
            res.append((-1, 0))  # SW
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
        """
        Method used to add the value to the graph in the key pos1 and pos2, if the key is not already in the graph
        the key is added with his value.

        :param pos1: Position 1 of the road just added.
        :type pos1: (int,int)
        :param pos2: Position 2 of the road just added.
        :type pos2: (int,int)
        :param distance: The distance between the 2 positions.
        :type distance: int
        """
        if pos1 not in self.graph:
            self.graph[pos1] = {}
        if pos2 not in self.graph[pos1]:
            self.graph[pos1][pos2] = distance
        if pos2 not in self.graph:
            self.graph[pos2] = {}
        if pos1 not in self.graph[pos2]:
            self.graph[pos2][pos1] = distance

    def dijkstra(self, vertex):
        """
        Algorithm of dijkstra vertex is the point where we start

        Take from :
        https://128mots.com/2020/02/18/implementation-python-de-lalgorithme-de-dijkstra/
        :param vertex: position where we start
        :return: distance: dictionary of key = position and value = distance between the position and the vertex
        """
        queue = deque([vertex])
        distance = {vertex: 0}
        while queue:
            t = queue.popleft()
            for voisin in self.graph[t]:
                queue.append(voisin)
                new_distance = distance[t] + self.graph[t][voisin]
                if voisin not in distance or new_distance < distance[voisin]:
                    distance[voisin] = new_distance
        return distance
