from Class_Building.mapBuilding import mapBuilding
from Class_Character.mapCharacter import mapCharacter

class logic_main:
    def __init__(self, resident, money):
        self.resident = resident
        self.money = money

    map_build = mapBuilding()
    map_char = mapCharacter()
    while(1):
        for build in map_build.map:
            build.check_update()

        for char in map_char:
            char.mov()

