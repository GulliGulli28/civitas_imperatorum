import pygame

List_Building = pygame.sprite.Group()

class Building(pygame.sprite.Sprite): 
    def __init__(self, x, y):
        super().__init__()
        self.condition = 0   # état du batiment (en feu, détruit)
        self.x = x  # position du la map axe x
        self.y = y  # position de la map axe y
        self.size = 1  # taille du batiment (2x2, 3x3, ...)
        self.capacity = 0  # nombre de personne pouvant rentrer dedans (travailler, habiter)
        self.price = 0  # prix du batiment
    
class Test_Building(Building): #pour tester le nouveau fonction
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load("Class Building/Assets/INSACVL.png").convert_alpha()
        
    def scale(self,height,width):
        self.image = pygame.transform.scale(self.image,(height,width))
        self.rect  = self.image.get_rect()
        pygame.sprite.Sprite.add(self,List_Building)

def place_building(surface,x,y):
    house = Test_Building(x,y)
    house.scale(50,50)


