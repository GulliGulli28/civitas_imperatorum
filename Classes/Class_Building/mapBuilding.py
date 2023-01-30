import math
import random
from enum import Enum
from Classes.Class_Building.Building import Building
from Classes.Class_Building.Engineer_post import Engineer_post
from Classes.Class_Building.Farm import Farm
from Classes.Class_Building.Granary import Granary
from Classes.Class_Building.House import House
from Classes.Class_Building.Market import Market
from Classes.Class_Building.Pointeur import Pointeur
from Classes.Class_Building.Prefecture import Prefecture
from Classes.Class_Building.Reservoir import Reservoir
from Classes.Class_Building.Road import Road
from Classes.Class_Building.Senate import Senate


class mapBuilding:
    _instance = None

    def __new__(cls):
        if mapBuilding._instance is None:
            mapBuilding._instance = super().__new__(cls)
        return mapBuilding._instance

    def __init__(self):
        self.sizeX = 50
        self.sizeY = 50
        self.map = [[None for j in range(self.sizeY+1)] for i in range(self.sizeX+1)]
        self.graph = {}
        self.graph_assoc = {}
        self.listGranary = []
        self.resident = 0
        self.unemployed = 0
        for y in range(self.sizeY):
            self.map[25][y] = factory(BUILDING_TYPE.ROAD,25,y,y)
            self.update_graph((25,y))
        
    def update(self):
        for map in self.map:
            for building in map:
                if building is not None:
                    building.check_update(self, map)

    def add_build(self, new_build):
        road_near = False
        if not (isinstance(new_build, Road)):
            for i in range(new_build.size):  # check that there is a road next to the building
                for y in range(new_build.size):
                    pos = self.get_direction(new_build.positionX + i, new_build.positionY + y)
                    print("pos =")
                    if len(pos) > 0 and road_near is False:
                        road_near = True
                        (a, b) = pos[0]
                        print("posX :", new_build.positionX, " posY :", new_build.positionY, " i :", i, " y :", y,
                              " a :", a, " b :", b)
                        new_build.road = (new_build.positionX + i + a, new_build.positionY + y + b)
                    pos = self.get_direction(new_build.positionX + y, new_build.positionY + i)
                    if len(pos) > 0 and road_near is False:
                        road_near = True
                        print(pos[0])
                        (a, b) = pos[0]
                        new_build.road = (new_build.positionX + y + a, new_build.positionY + i + b)
            if not road_near:
                return 0
        if self.map[new_build.positionX][new_build.positionY] is not None: #check if it already has a building
            return 0
        if isinstance(new_build, Granary):
            self.listGranary.append(new_build)
            self.update_graph(new_build.road)
        if isinstance(new_build, Farm):
            self.update_graph(new_build.road)
        self.map[new_build.positionX][new_build.positionY] = new_build
        if new_build.size > 1:
            for i in range(new_build.size):
                i += 1
                p = Pointeur(new_build.positionX, new_build.positionY, new_build.idi)
                for y in range(i):
                    self.map[new_build.positionX + i][new_build.positionY + y] = p
                    self.map[new_build.positionX + y][new_build.positionY + i] = p
                self.map[new_build.positionX + i][new_build.positionY + i] = p
        if isinstance(new_build, Road):
            pos = (new_build.positionX, new_build.positionY)
            self.update_graph(pos)
        elif isinstance(new_build, House):
            # game.add_resident(5)
            pass
    def place_build(self,name,positionX,positionY):
        type = type_of_building(name)
        new_build = factory(type,positionX,positionY,1)
        self.add_build(new_build)

    def remove_build(self,positionX,positionY):
        build = self.map[positionX][positionY]
        if isinstance(build,Granary):
            self.listGranary.remove(build)
        if isinstance(build,House):
            pass
        if isinstance(build,Road):
            pos = (build.positionX,build.positionY)
            self.update_graph_remove(pos)
        self.map[positionX][positionY] = None

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
            direct = self.get_direction(x, y)
            if len(direct) != 0:
                for i in direct:
                    (pos2, distance, last_dir) = self.calculate_distance(pos, i)
                    # print("calculate_distance")
                    # print(pos, pos2, distance)
                    self.graph_assoc[pos] = {pos2, i}
                    self.graph_assoc[pos2] = {pos, last_dir}
                    self.add_dist2graph(pos, pos2, distance)

    def update_graph_remove(self,pos):
        pass

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
            pos = tuple(map(lambda a, b: a + b, pos, i))  # solution d'en dessous
            # pos += i
            distance += 1
            (x, y) = pos
            direct = self.get_direction(x, y)

            if len(direct) == 2:
                direct.remove(tuple(map(lambda a, b: a - b, old_pos, pos)))
                i = direct[0]
            else:
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

    def dijkstra(self, graph, start, end):
        # Initialisation des distances
        distances = {node: math.inf for node in graph}
        distances[start] = 0

        # Initialisation de la liste des noeuds à traiter
        to_visit = set(graph)

        # Initialisation de la liste des précédents
        previous = {node: None for node in graph}

        # Initialisation du coût total
        total_cost = 0
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
                    total_cost += distance

        # Création du chemin en partant de la fin et en suivant les précédents
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = previous[current]

        # Renvoie du chemin inversé (de la fin vers le début)
        return list(reversed(path)), total_cost

    def get_path_between_node(self, node1, node2):
        (x, y) = node1
        direction_possible = self.get_direction(x, y)
        possible_path = []
        for direction in direction_possible:
            possible_path.append(node1 + direction)
            while self.get_direction(possible_path[-1].positionX, possible_path[-1].positionY) == 2 & possible_path(
                    [-1]) != node2:
                possible_path.append(
                    possible_path[-1] + self.get_direction(possible_path[-1].positionX,
                                                           possible_path[-1].positionY).remove())
            if not possible_path(len(possible_path)) == node2:
                possible_path.clear()
            else:
                return possible_path

    def contruct_entire_path(self, dij_path):
        node1 = dij_path[0]
        entire_path = [node1]
        dij_path.remove(node1)
        for node2 in dij_path:
            entire_path.append(self.get_path_between_node(node1, node2))
            node1 = node2
        print(entire_path)
        return entire_path

    # graph = {'A': {'B': 15, 'C': 4}, 'B': {'E': 5}, 'C': {'E': 11, 'D': 2}, 'D': {'E': 3}, 'E': {}}
    # start = 'A'
    # end = 'D'
    # path = dijkstra(graph, start, end)
    # print(f'Le chemin le plus court entre {start} et {end} est {path}')


def type_of_building(name):
    match name:
        case "house":
            return BUILDING_TYPE.HOUSE
        case "farm":
            return BUILDING_TYPE.FARM
        case "well":
            return BUILDING_TYPE.RESERVOIR
        case "market":
            return BUILDING_TYPE.MARKET
        case "prefecture":
            return BUILDING_TYPE.PREFECTURE
        case "senate":
            return BUILDING_TYPE.SENATE
        case "road":
            return BUILDING_TYPE.ROAD
        
                        
def factory(type,positionX,positionY,idi):
    match type:
        case BUILDING_TYPE.HOUSE:
            return House(positionX,positionY,idi)
        case BUILDING_TYPE.FARM:
            return Farm(positionX,positionY,idi,1,1)
        case BUILDING_TYPE.RESERVOIR:
            return Reservoir(positionX,positionY,idi)
        case BUILDING_TYPE.MARKET:
            return Market(positionX,positionY,idi)
        case BUILDING_TYPE.PREFECTURE:
            return Prefecture(positionX,positionY,idi)
        case BUILDING_TYPE.SENATE:
            return Senate(positionX,positionY,idi)
        case BUILDING_TYPE.ROAD:
            return Road(positionX,positionY)

class BUILDING_TYPE(Enum):
    ROAD = 0
    HOUSE = 1
    FARM = 2
    RESERVOIR = 3
    MARKET = 4
    PREFECTURE = 5
    SENATE = 6


'''
truc = mapBuilding()
for i in range(40):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    road = Road(x, y)
    truc.add_build(road)
print(truc.map)
print(truc.graph)
'''
# truc = mapBuilding()
# road1 = (0, 0)
# road2 = (0, 0)
# for i in range(100):
#     x = random.randint(1, 10)
#     y = random.randint(1, 10)
#     if road1 == (0, 0):
#         road1 = (x, y)
#     elif road2 == (0, 0):
#         road2 = (x, y)
#     road = Road(x, y)
#     truc.add_build(road)
# # print(truc.map)
# print(truc.graph)
# path = truc.dijkstra(truc.graph, road1, road2)
# truc.contruct_entire_path(path)
