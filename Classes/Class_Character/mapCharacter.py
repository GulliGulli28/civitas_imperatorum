from enum import Enum
from Classes.Class_Building.mapBuilding import mapBuilding
from Classes.Class_Character.Character import Character
from Classes.Class_Character.Resident import Resident
from Classes.Class_Character.Walker import Walker
from Classes.Class_Character.Worker import Worker
from Classes.Class_Character.Migrant import Migrant
from Classes.Class_Character.Delivery import Delivery
from Classes.Class_Character.Prefet import Prefet


class mapCharacter:

    def __init__(self):
        self.list = []

    def update(self,mapBuilding):
        for map in mapBuilding.map:
            for building in map:
                if building is not None:
                    pass
        for character in self.list:
            if character.is_there:
                print("destination reached")
                self.remove_character(character)
            character.update()

    def new_character(self,name,positionX,positionY, dest):
        type = type_of_character(name)
        new_character = factory(type,positionX,positionY,dest)
        self.add_character(new_character)
        
    def add_character(self, character):
        self.list.append(character)

    def remove_character(self, character):
        self.list.remove(character)

def type_of_character(name):
    match name:
        case "migrant":
            return CHARACTER_TYPE.MIGRANT
        case "walker":
            return CHARACTER_TYPE.WALKER
        case "resident":
            return CHARACTER_TYPE.RESIDENT
        case "walker":
            return CHARACTER_TYPE.WALKER
        case "prefet":
            return CHARACTER_TYPE.PREFET
        case "worker":
            return CHARACTER_TYPE.WORKER
        case "delivery":
            return CHARACTER_TYPE.DELIVERY
        
                        
def factory(type,positionX,positionY,dest):
    match type:
        case CHARACTER_TYPE.MIGRANT:
            return Migrant(positionX,positionY,dest)
        case CHARACTER_TYPE.WALKER:
            return Walker(positionX,positionY,dest)
        case CHARACTER_TYPE.RESIDENT:
            return Resident(positionX,positionY,dest)
        case CHARACTER_TYPE.WORKER:
            return Worker(positionX,positionY,dest)
        case CHARACTER_TYPE.PREFET:
            return Prefet(positionX,positionY,dest)
        case CHARACTER_TYPE.DELIVERY:
            return Delivery(positionX,positionY,dest)

class CHARACTER_TYPE(Enum):
    MIGRANT = 1
    WALKER = 2
    RESIDENT = 3
    DELIVERY = 4
    PREFET = 5
    WORKER = 6
