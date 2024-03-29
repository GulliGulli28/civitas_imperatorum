import random
from abc import ABC  # ABC = abstract base class
from random import randint

from Classes.Class_Building.mapBuilding import mapBuilding


class Character(ABC):
    health = None
    joy = None
    positionX = None
    positionY = None
    direction = None
    sprite_list = None
    sprite_in_list = 0

    def __init__(self, health, joy, positionX, positionY, direction, sprite_list, sprite_in_list):
        self.joy = joy
        self.health = health
        self.positionX = positionX
        self.positionY = positionY
        self.direction = direction
        self.sprite_list = sprite_list
        self.sprite_in_list = sprite_in_list

    def move(self, map_build):
        """
        Move a random character

        :param map_build: A instance of actual mapBuilding
        :type map_build: mapBuilding
        :return:
        """

        """
        Use for animation
        if self.sprite_in_list == 11:
            self.sprite_in_list = 0
        else:
            self.sprite_in_list += 1
        """
        direction_possible = map_build.get_direction()(self.positionX, self.positionY)
        if len(direction_possible) < 2:
            direction_possible = random.choice(direction_possible)
        elif len(direction_possible) == 2:
            del direction_possible[self.direction]
        (x, y) = direction_possible
        self.positionX += x
        self.positionY += y
        self.direction = (-x, -y)  # on assigne l'inverse car le personnage avance et on doit supprimer dans le move
        # l'ancienne position

    def update_health(self, newHealth):
        self.health = newHealth

    def update_joy(self, newJoy):
        self.joy = newJoy
