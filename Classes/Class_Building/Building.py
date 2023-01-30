import time
from abc import ABC  # ABC = abstract base class
import hashlib
from enum import Enum
import random


class Building(ABC):  # hérite de ABC
    condition = None
    positionX = None
    positionY = None
    size = None
    capacity = None
    price = None
    idi = None
    fire_risk = None
    destruction_risk = None

    def __init__(self, name, positionX, positionY, size, capacity, price, idi):
        self.name = name
        self.condition = 0  # état du batiment (en feu, détruit)
        self.positionX = positionX  # position du la map axe x
        self.positionY = positionY  # position de la map axe y
        self.size = size  # taille du batiment (2x2, 3x3, ...)
        self.capacity = capacity  # nombre de personne pouvant rentrer dedans (travailler, habiter)
        self.price = price  # prix du batiment
        self.idi = idi  # id du batiment
        self.fire_risk = 0
        self.destruction_risk = 0
        self.last_update = time.time()
        self.level = 0
        self.is_new = True
        self.is_on_fire = False
        # dictionnaire_building = {}
        # compteur = 0
        # type_building = ""

        """def creer_batiment(self):
            global compteur
            x,y = pygame.mouse.get_pos()
            for batiment in dictionnaire_batiment:
                if x>= dictionnaire_batiment[batiment]["x"] and x<= dictionnaire_batiment[batiment]["longueur"] and y>= dictionnaire_batiment[batiment]["y"] and y<= dictionnaire_batiment[batiment]["largeur"]:
                    return "il existe deja un batiment à cette endroit"
            
            p= str(type(self)) + str(compteur)
            dictionnaire_batiment[str(self.id)]={
            "x":x,
            "y":y,
            "etat": "neuf",
            "longueur":self.size[0],
            "largeur":self.size[1]
            }
            return dictionnaire_batiment"""

    def update_risk(self):
        self.fire_risk += 0.01
        self.destruction_risk += 1

    def risque_feu(self):
        if self.is_on_fire:
            print("le batiment est en feu")
        else:
            x= random.random()*100
            if x<self.fire_risk*100:
                self.is_on_fire = True
                print("le batiment est maintenant en feu")
            else:
                print("Toujours debout")
    def check_update(self):
        current_time = time.time()
        if self.is_new:
            self.is_new = False
        if current_time - self.last_update >= 30:
            self.last_update = current_time
            self.update_risk()
            self.risque_feu()

    def update_level(self, level):
        self.level += level
