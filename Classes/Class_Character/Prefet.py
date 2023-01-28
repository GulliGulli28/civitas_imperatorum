from Classes.Class_Building.Building import Building
from Classes.Class_Character.Worker import Worker
from Classes.Class_Building.mapBuilding import mapBuilding

class Prefet(Worker):
    def __init__(self, positionX, positionY, direction):
        super().__init__(positionX, positionY, direction)


    def checkfire(self, mapbuilding):
        for i in range(mapbuilding.sizeX):
            for j in range(mapbuilding.sizeY):
                if isinstance(mapbuilding.map[i][j], Building):
                    if abs(self.positionX - mapbuilding.map[i][j].positionX)<=3 and abs(self.positionY - mapbuilding.map[i][j].positionY)<=3:
                        mapbuilding.map[i][j].is_on_fire =False
                        mapbuilding.map[i][j].fire_risk =0
                    else:
                        self.move(mapbuilding)

