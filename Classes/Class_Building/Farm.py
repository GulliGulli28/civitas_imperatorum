import time

from Classes.Class_Building.Building import Building
from Classes.Class_Character.Delivery import Delivery


class Farm(Building):
    type_crop = None  # type de culture (blé, raisin, etc)

    def __init__(self, type_crop, positionX, positionY, size, capacity, price, idi):
        self.type_crop = type_crop
        super().__init__(positionX, positionY, size, capacity, price, idi)
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
        if current_time - self.last_production_time >= 30:
            self.last_production_time = current_time
            for granary in mapBuilding.listGranary:
                cost, path = mapBuilding.dijkstra(mapBuilding.map, (self.positionX, self.positionY), (granary.positionX, granary.positionY))
                if path < best_path | best_path is None:
                    best_path = path
                    best_gra = granary
            pathing = mapBuilding.contruct_entire_path(best_path)
            (x, y) = (self.road.positionX, self.road.positionY)
            mapCharacter.add_character(
                Delivery(x, y, self.direction, pathing))
            best_gra.add_food(self.productivity)
