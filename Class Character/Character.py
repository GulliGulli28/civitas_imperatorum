from abc import ABC  # ABC = abstract base class


class Character(ABC):
    health = None
    joy = None
    position = None
    direction = None
    sprite_list = None
    sprite_in_list = 0

    def __init__(self, health, joy, position, direction,sprite_list, sprite_in_list):
        self.joy = joy
        self.health = health
        self.position = position
        self.direction = direction
        self.sprite_list = sprite_list
        self.sprite_in_list = sprite_in_list

    def move(self, newPosition):
        self.position = newPosition
        if self.sprite_in_list == 11:
            self.sprite_in_list = 0
        else:
            self.sprite_in_list+=1
            
            
    def update_health(self, newHealth):
        self.health = newHealth

    def update_joy(self, newJoy):
        self.joy = newJoy

