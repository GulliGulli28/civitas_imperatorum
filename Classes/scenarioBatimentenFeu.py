from Class_Building.mapBuilding import mapBuilding
from Class_Character.mapCharacter import mapCharacter
from Classes.Class_Building.House import House
from Classes.Class_Building.Road import Road


class ScenarioBatimentenFeu:
    def __init__(self, resident, money):
        self.resident = resident
        self.money = money

    map_build = mapBuilding()
    map_char = mapCharacter()

    Bâtiment = House(0,0,1,1,1,1)
    Bâtiment.fire_risk =0.3
    map_build.add_build(Bâtiment)
    for i in range(0,40):
        road = Road(1,i)
        map_build.add_build(road)
    print(map_build)
    print("Le batiment est en feu: ", Bâtiment.is_on_fire)
    k=1
    while k:
        Bâtiment.update_risk()
        Bâtiment.risque_feu()
        Bâtiment.update_risk()
        print("Le risque de feu de Bâtiment est maintenant: ", Bâtiment.fire_risk)
        print("Le batiment est en feu: ", Bâtiment.is_on_fire)
        if Bâtiment.is_on_fire == True:
            k=0

