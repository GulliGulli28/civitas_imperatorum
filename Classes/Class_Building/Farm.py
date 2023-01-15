import time

from Classes.Class_Building.Building import Building
from Classes.Class_Character.Delivery import Delivery


class Farm(Building):
    type_crop = None  # type de culture (blé, raisin, etc)

    def __init__(self, type_crop, positionX, positionY, size, capacity, price, idi, road):
        self.type_crop = type_crop
        super().__init__(positionX, positionY, size, capacity, price, idi)
        self.last_production_time = time.time()
        self.road = road
        self.productivity = 50

    def check_update(self):
        super().check_update()
        self.produce()

    def produce(self, mapCharacter, mapBuilding):
        current_time = time.time()
        if current_time - self.last_production_time >= 30:
            self.last_production_time = current_time
            for granary in mapBuilding.listGranary:
                cost, path = mapBuilding.dijkstra(mapBuilding.map, (self.positionX, self.positionY), (granary.positionX, granary.positionY))
                if path < best_path | best_path is None:
                    best_path = path
                    best_gra = granary
            mapCharacter.add_character(
                Delivery(self.positionX, self.positionY, self.direction, (self.positionX, self.positionY),
                         (granary.positionX, granary.positionY)))
            best_gra.add_food(self.productivity)
