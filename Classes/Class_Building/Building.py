from abc import ABC  # ABC = abstract base class


class Building(ABC):  # hérite de ABC
    condition = None
    positionX = None
    positionY = None
    size = None
    capacity = None
    price = None

    def __init__(self, positionX, positionY, size, capacity, price):
        self.condition = 0   # état du batiment (en feu, détruit)
        self.positionX = positionX  # position du la map axe x
        self.positionY = positionY  # position de la map axe y
        self.size = size  # taille du batiment (2x2, 3x3, ...)
        self.capacity = capacity  # nombre de personne pouvant rentrer dedans (travailler, habiter)
        self.price = price  # prix du batiment
