import time

from Classes.Class_Building.Building import Building


class Farm(Building):
    type_crop = None  # type de culture (blé, raisin, etc)

    def __init__(self, positionX, positionY, idi,type_crop, last_production_time):
        super.__init__('farm', positionX, positionY, 1 , 10, 15, idi)
        self.last_production_time = time.time(last_production_time)
        self.type_crop = type_crop

    def produce(self):
        current_time = time.time()
        if current_time - self.last_production_time >= 30:
            self.last_production_time = current_time
            # Ajout du livreur