import random

from Classes.Class_Building.Building import Building
from Classes.Class_Building.Road import Road
from Classes.Class_Building.Pointeur import Pointeur
from collections import deque
import math


class mapBuilding():
    def __init__(self):
        self.sizeX = 50
        self.sizeY = 50
        self.map = [[None for j in range(self.sizeY)] for i in range(self.sizeX)]
        self.graph = {}
        self.graph_assoc = {}

    def add_build(self, new_build):
        self.map[new_build.positionX][new_build.positionY] = new_build
        if new_build.size > 1:
            for i in range(new_build.size):
                i += 1
                p = Pointeur(new_build)
                for y in range(i):
                    self.map[new_build.positionX + i][new_build.positionY + y] = p
                    self.map[new_build.positionX + y][new_build.positionY + i] = p
                self.map[new_build.positionX + i][new_build.positionY + i] = p
        if isinstance(new_build, Road):
            print("this is a road")
            pos = (new_build.positionX, new_build.positionY)
            self.update_graph(pos)

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
        print(res)
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
            direct = self.get_direction(x, y)
            if len(direct) > 1:
                for i in direct:
                    (pos2, distance, last_dir) = self.calculate_distance(pos, i)
                    self.graph_assoc[pos] = {pos2, i}
                    self.graph_assoc[pos2] = {pos, last_dir}
                    self.add_dist2graph(pos, pos2, distance)

    def calculate_distance(self, pos, i):
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
        return pos2, distance, i

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

    def dijkstra(graph, start, end):
        # Initialisation des distances
        distances = {node: math.inf for node in graph}
        distances[start] = 0

        # Initialisation de la liste des noeuds à traiter
        to_visit = set(graph)

        # Initialisation de la liste des précédents
        previous = {node: None for node in graph}

        # Boucle principale
        while to_visit:
            # Recherche du noeud avec la distance minimale
            current = min(to_visit, key=lambda x: distances[x])

            # Si on a atteint la destination, on arrête la boucle
            if current == end:
                break

            # Suppression du noeud courant de la liste des noeuds à traiter
            to_visit.remove(current)

            # Mise à jour des distances et des précédents des voisins
            for neighbor in graph[current]:
                distance = distances[current] + graph[current][neighbor]
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current

        # Création du chemin en partant de la fin et en suivant les précédents
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = previous[current]

        # Renvoie du chemin inversé (de la fin vers le début)
        return list(reversed(path))

    # graph = {'A':{'B':15,'C':4},'B':{'E':5},'C':{'E':11,'D':2},'D':{'E':3},'E':{}}
    # start = 'A'
    # end = 'D'
    # path = dijkstra(graph, start, end)
    # print(f'Le chemin le plus court entre {start} et {end} est {path}')


truc = mapBuilding()
for i in range(50):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    road = Road(x, y)
    truc.add_build(road)
print(truc.map)
print(truc.graph)
