import time

from Classes.Class_Building.Building import Building


class Farm(Building):
    type_crop = None  # type de culture (blé, raisin, etc)

    def __init__(self, type_crop, positionX, positionY, size, capacity, price, idi):
        self.type_crop = type_crop
        super().__init__(positionX, positionY, size, capacity, price, idi)
        self.last_production_time = time.time()

    def produce(self):
        current_time = time.time()
        if current_time - self.last_production_time >= 30:
            self.last_production_time = current_time
            # Ajout du livreur