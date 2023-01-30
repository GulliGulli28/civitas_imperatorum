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




class ScenarioPrefet:
    def __init__(self, resident, money):
        self.resident = resident
        self.money = money

    map_build = mapBuilding()
    map_char = mapCharacter()

    prefet= Prefet(1,0,(0,1))
    map_char.add_character(prefet)
    for i in range(0,40):
        road = Road(1, i)
        map_build.add_build(road)
        house=House(0,i,1,)
        map_build.add_build(house)
        house.is_on_fire = True
        house.fire_risk =0.2

    print("Maisons placés sur toute la ligne 0")
    print("routes créer sur toute la ligne 1")
    print("le prefet est ici",prefet.positionX, prefet.positionY)
    for i in range(0,40):
        print("Le batiment à la position", map_build.map[0][i].positionX, map_build.map[0][i].positionY, "est en feu", map_build.map[0][i].is_on_fire )

    prefet.checkfire(map_build)
    prefet.move(map_build)
    print("le prefet est maintenant ici:",prefet.positionX, prefet.positionY)

    for i in range(0,40):
        print("Le batiment à la position", map_build.map[0][i].positionX, map_build.map[0][i].positionY, "est en feu", map_build.map[0][i].is_on_fire )
