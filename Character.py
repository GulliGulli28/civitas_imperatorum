from abc import ABC  # ABC = abstract base class
import Class\ Building.mapBuilding


class Character(ABC):
    health = None
    joy = None
    positionX = None
    positionY = None
    def __init__(self, health, joy, positionX, positionY):
        self.joy = joy
        self.health = health
        self.positionX = positionX
        self.positionY = positionY

    def move(self, mapBuilding):
        self.positionX = newPositionX
        self.positionY = newPositionY

    def update_health(self, newHealth):
        self.health = newHealth

    def update_joy(self, newJoy):
        self.joy = newJoy
