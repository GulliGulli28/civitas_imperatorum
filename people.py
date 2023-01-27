import pygame as pg
from Classes.Class_Building.mapBuilding import mapBuilding
from Classes.Class_Character.mapCharacter import mapCharacter

class people:
    def __init__(self,world):
        self.world = world
        self.mapBuilding = mapBuilding()
        self.mapCharacter = mapCharacter()
        self.image = self.load_images()

    def update(self):
        self.mapBuilding.update()
        for map in self.mapBuilding.map:
            for building in map:
                if building is not None and building.is_new and building.name != "road":
                    print("new building")
                    dest = (building.positionX ,building.positionY)
                    self.mapCharacter.new_character("migrant",0,0,dest)
        self.mapCharacter.update(self.mapBuilding)
        
    def draw(self, screen, camera):
        for character in self.mapCharacter.list:
            print("I'm walking")
            print((str)(character.positionX ) + " , " + (str)(character.positionY))
            render_pos = self.world.cart_to_iso(character.positionX,character.positionY)
            print(render_pos)
            screen.blit(self.image[character.name], 
                                        (render_pos[0] + self.world.grass_tiles.get_width()/2 + camera.scroll.x,
                                        render_pos[1] + camera.scroll.y))

    def load_images(self):
        migrant = pg.image.load("walker/citizen02_00615.png").convert_alpha()

        return {
            "migrant" : migrant
        }