from Classes.Class_Character.Worker import Worker
from Classes.Class_Building.mapBuilding import mapBuilding

class Prefet(Worker):
    def __init__(self, positionX, positionY, direction):
        super().__init__(positionX, positionY, direction)


    def anti_johnny(self, mapbuilding):
        for i in mapbuilding.map:
            if isinstance(i, Building):
                if i.is_on_fire:
                    print("damn")

