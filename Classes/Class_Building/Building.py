from abc import ABC  # ABC = abstract base class
import hashlib
class Building(ABC):  # hérite de ABC
    condition = None
    positionX = None
    positionY = None
    size = None
    capacity = None
    price = None
    id = None

    def __init__(self, positionX, positionY, size, capacity, price, id):
        self.condition = 0   # état du batiment (en feu, détruit)
        self.positionX = positionX  # position du la map axe x
        self.positionY = positionY  # position de la map axe y
        self.size = size  # taille du batiment (2x2, 3x3, ...)
        self.capacity = capacity  # nombre de personne pouvant rentrer dedans (travailler, habiter)
        self.price = price  # prix du batiment
        self.id = id #id du batiment

        dictionnaire_building={}
        compteur = 0
        type_building=""

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

        def creer_batiment():
            if type=="Farm":
                p=type

bat = Building(10,20,(2,3),2,10,"coucou")
print(bat.positionX)
a=str(type(bat))+"p"
print(a)
        



