from abc import ABC  # ABC = abstract base class
from random import randint

from Classes.Class_Building import mapBuilding
class Character(ABC):
    health = None
    joy = None
    positionX = None
    positionY = None
    direction = None
    sprite_list = None
    sprite_in_list = 0

    def __init__(self, health, joy, positionX, positionY, direction,sprite_list, sprite_in_list):
        self.joy = joy
        self.health = health
        self.positionX = positionX
        self.positionY = positionY
        self.direction = direction
        self.sprite_list = sprite_list
        self.sprite_in_list = sprite_in_list

    def move(self,map):
        #TODO faut-il pas plutôt mettre en paramètre "move(self,map.getPossibleDirection(self.positionX,self.positionY))" ???
        #self.position = newPosition
        if self.sprite_in_list == 11:
            self.sprite_in_list = 0
        else:
            self.sprite_in_list+=1
        liste_direction=["NW", "NE", "SW","SE"]
        if len(mapBuilding.nbr_direction(self.positionX,self.positionY)) ==1:
            self.direction=map.nbr_direction[0]

        elif len(mapBuilding.nbr_direction(self.positionX,self.positionY)) ==2:
            if self.direction not in mapBuilding.nbr_direction:
                self.direction = mapBuilding.nbr_direction(randint(1))
        else:
            if self.direction not in map.nbr_direction:
                self.direction = mapBuilding.nbr_direction(randint(len(mapBuilding.nbr_direction(self.positionX,self.positionY))))
        positions(self)#TODO est-ce que c'est pas plutôt "direction(self)"
        
            

            

            
            
    def update_health(self, newHealth):
        self.health = newHealth

    def update_joy(self, newJoy):
        self.joy = newJoy

    def directions(self):
        if self.direction == "NW":
            self.positionY +=1
        elif self.direction == "NE":
            self.positionY -=1
        elif self.direction == "SW":
            self.positionX-=1
        else:
            self.positionX+=1


    