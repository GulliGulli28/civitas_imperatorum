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


class Logic_main:
    def __init__(self, resident, money):
        self.resident = resident
        self.money = money

    map_build = mapBuilding()
    map_char = mapCharacter()
    drhouse = House(1, 2, 1, 1, 1, 1)
    drhouse.fire_risk = 0.01
    Percy_Weasley = Prefet(1, 1, (0, 1))
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
    house = House(1, 1, 1, 1, 1, 1)
    map_build.add_build(house)
    road = Road(40, 45)
    house = House(40, 46, 1, 1, 1, 1)
    farm = Farm("wheat", 1, 6, 3, 1, 1, (0, 6))
    grana = Granary(41, 6, 2, 1, 1, (41, 6))
    map_build.add_build(grana)
    map_build.add_build(farm)
    map_build.add_build(road)
    migr = Migrant(0, 20, (40, 46))
    map_char.add_character(migr)
    false = True
    while false:
        drhouse.risque_feu()
        drhouse.update_risk()
        print(drhouse.is_on_fire)
        for char in map_char.list:
            if isinstance(char, Migrant):
                if char.move():
                    map_char.remove_character(char)
                print(char.positionX + char.positionY)
            elif isinstance(char, Delivery):
                if char.move():
                    map_char.remove_character(char)
            else:
                char.move()
        for i in range(0, 40):
            for j in range(0, 40):
                if not(map_build.map[i][j] is None):
                    map_build.map[i][j].check_update(map_char, map_build)
        print(char.positionX, char.positionY)
        print(map_char.list)
        Percy_Weasley.anti_johnny(map_build)
        time.sleep(1)
    # while 1:
    #     for build_list in map_build.map:
    #         for build in build_list:
    #             if isinstance(build, Building):
    #                 build.check_update()
    #
    #     for char in map_char:
    #         char.mov()
