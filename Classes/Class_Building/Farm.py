import math
import time

from Classes.Class_Building.Building import Building
from Classes.Class_Character.Delivery import Delivery


class Farm(Building):
    type_crop = None  # type de culture (blé, raisin, etc)

    def __init__(self, type_crop, positionX, positionY, size, capacity, price, idi):
        super().__init__("farm", positionX, positionY, size, capacity, price, idi)
        self.type_crop = type_crop
        self.last_production_time = time.time()
        self.productivity = 50

    def check_update(self, map_char, map_build):
        super().check_update(map_char, map_build)
        self.produce(map_char, map_build)

    def produce(self, mapCharacter, mapBuilding):
        """
        Function used to check if the farm need to produce food, if it produces : a Delivery man is created and go to
        the nearest Granary to stock the food.;

        :param mapCharacter: The list of character
        :param mapBuilding: The list of Building
        :return: None
        """
        current_time = time.time()
        best_cost = math.inf
        if current_time - self.last_production_time >= 5:
            self.last_production_time = current_time
            for granary in mapBuilding.listGranary:
                print(granary.road)
                (x, y) = granary.road
                path, cost = mapBuilding.dijkstra(mapBuilding.graph, (self.positionX, self.positionY), (x, y))
                if cost < best_cost:

                    best_cost = cost
                    best_path = path
                    best_gra = granary
            print("The best path is ", best_path)
            pathing = mapBuilding.contruct_entire_path(best_path)
            print("The best entire path is ", pathing)
            (x, y) = self.road
            mapCharacter.add_character(
                Delivery(x, y, pathing, best_gra))

