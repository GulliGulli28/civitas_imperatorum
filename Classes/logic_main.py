from Class_Building.mapBuilding import mapBuilding
from Class_Character.mapCharacter import mapCharacter
from Classes.Class_Building import Building
from Classes.Class_Building.Farm import Farm
from Classes.Class_Building.Granary import Granary
from Classes.Class_Building.House import House
from Classes.Class_Building.Road import Road
from Classes.Class_Character.Delivery import Delivery
from Classes.Class_Character.Migrant import Migrant
from Classes.Class_Character.Prefet import Prefet
import time

from Classes.Class_Character.Resident import Resident


class Logic_main:
    def __init__(self, resident, money):
        self.resident = resident
        self.money = money

    map_build = mapBuilding()
    map_char = mapCharacter()

    for i in range(0, 40):
        road = Road(0, i)
        map_build.add_build(road)
        road = Road(5, i)
        map_build.add_build(road)
        road = Road(10, i)
        map_build.add_build(road)
        road = Road(i, 5)
        map_build.add_build(road)
        road = Road(i, 10)
        map_build.add_build(road)
        road = Road(i, 20)
        map_build.add_build(road)
    print(map_build.map)
    print("Voici le graph\n", map_build.graph)
    house = House(1, 1, 1)
    map_build.add_build(house)
    road = Road(40, 45)
    house = House(39, 21, 1)
    map_build.add_build(road)
    map_build.add_build(house)
    farm = Farm("wheat", 1, 6, 3, 1, 1, 1)
    grana = Granary(1, 39, 1, 1, 1, 1)
    for i in range(0, 40):
        for j in range(0, 40):
            if not (map_build.map[i][j] is None):
                if isinstance(map_build.map[i][j], Road):
                    map_build.update_graph((i, j))
    map_build.add_build(grana)
    map_build.add_build(farm)
    map_build.add_build(road)
    migr = Migrant(0, 20, (1, 1))
    map_char.add_character(migr)
    while True:
        for char in map_char.list:
            if isinstance(char, Migrant):
                if char.move():
                    map_char.remove_character(char)
                    print("migrant = ", char.positionX, char.positionY)
                    map_build.map[char.positionX][char.positionY].update_level(1, map_char)
                print(char.positionX + char.positionY)
            elif isinstance(char, Delivery):
                if char.move(map_build):
                    map_char.remove_character(char)
            elif isinstance(char, Resident):
                print("Resident X", char.positionX, "Resident Y", char.positionY)
                char.move(map_build)
            else:
                char.move(map_build)
        for i in range(0, 40):
            for j in range(0, 40):
                if not (map_build.map[i][j] is None):
                    map_build.map[i][j].check_update(map_char, map_build)
        print(char.positionX, char.positionY)
        print(map_char.list)
        print("Food : ", map_build.map[1][39].stock)
        time.sleep(0.33)
    # while 1:
    #     for build_list in map_build.map:
    #         for build in build_list:
    #             if isinstance(build, Building):
    #                 build.check_update()
    #
    #     for char in map_char:
    #         char.mov()
