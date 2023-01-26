from Class_Building.mapBuilding import mapBuilding
from Class_Character.mapCharacter import mapCharacter
from Classes.Class_Building import Building
from Classes.Class_Building.House import House
from Classes.Class_Building.Road import Road
from Classes.Class_Character.Migrant import Migrant


class logic_main:
    def __init__(self, resident, money):
        self.resident = resident
        self.money = money

    map_build = mapBuilding()
    map_char = mapCharacter()
    for i in range(0, 40):
        road = Road(0, i)
        map_build.add_build(road)
    print(map_build.map)
    house = House(1, 1, 1, 1, 1, 1)
    map_build.add_build(house)
    migr = Migrant(0, 0, (0, 1))
    map_char.add_character(migr)
    while 1:
        for char in map_char.list:
            if isinstance(char, Migrant):
                if char.move():
                    map_char.remove_character(char)
                print(char.positionX + char.positionY)

            else:
                char.move()
        print(map_char.list)
    # while 1:
    #     for build_list in map_build.map:
    #         for build in build_list:
    #             if isinstance(build, Building):
    #                 build.check_update()
    #
    #     for char in map_char:
    #         char.mov()
