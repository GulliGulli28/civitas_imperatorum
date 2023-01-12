import pygame as pg
from settings import HUD_WIDTH

class Hud:

    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.hud_colour = (198, 155, 93, 175)

        # resources hud
        self.resources_surface = pg.Surface((width, height * 0.02), pg.SRCALPHA)
        self.resources_rect = self.resources_surface.get_rect(topleft=(0, 0))
        self.resources_surface.fill(self.hud_colour)

        # right hud
        self.build_surface = pg.Surface((width * 0.106, height))
        self.build_rect = self.build_surface.get_rect(topleft=(self.width - HUD_WIDTH, self.height * 0))
        self.build_surface.fill(self.hud_colour)

        # select hud
        self.select_surface = pg.Surface((width * 0.3, height * 0.2), pg.SRCALPHA)
        self.select_rect = self.select_surface.get_rect(topleft=(self.width - HUD_WIDTH, self.height * 0.79))
        self.select_surface.fill(self.hud_colour)


        self.images = self.load_images()
        self.icons = self.load_icons()
        self.tiles = self.build_hud()
        self.selected_tile = None

    def draw(self, screen):
        images = self.images
        icon_1_width, icon_1_height = images["icon_1"].get_width(), images["icon_1"].get_height()
        # resources hud
        screen.blit(self.resources_surface, (0, 0))

        # build hud
        
        screen.blit(self.build_surface, (self.width - self.build_surface.get_width(), self.resources_surface.get_height()))
        # select hud
        # screen.blit(self.select_surface, (self.width * 0.35, self.height * 0.79))
        
        screen.blit(images["right_hud"], (self.width - HUD_WIDTH, self.height * 0.02))
        screen.blit(images["icon_1"], (self.width - icon_1_width, self.height - icon_1_height))
        screen.blit(images["overlays_case"], (self.width - HUD_WIDTH + 4.5, self.resources_surface.get_height() + 3.5))


        #affichage icons
        for tile in self.tiles:
            screen.blit(tile["icon"],tile["rect"].topleft)
            
        # OVERLAY TEXT
        font = pg.font.Font(None, 34)
        overlays_text = font.render("Overlays", True, (0, 0, 0))
        screen.blit(overlays_text, (self.width-HUD_WIDTH+10, 21))

    def build_hud(self):
        images = self.images
        icons = self.icons
        HUD_WIDTH = images["right_hud"].get_width()
        #button
        tiles = []
        for name, image in icons.items():
            name = name
            if name == "housing":
                pos = [self.width - HUD_WIDTH + 13.5, 295]
            elif name == "clear":
                pos = [self.width - HUD_WIDTH + 63, 295]
            elif name == "road":
                pos = [self.width - HUD_WIDTH + 113, 295]
            elif name == "water":
                pos = [self.width - HUD_WIDTH + 13.5, 330]
            elif name == "government":
                pos = [self.width - HUD_WIDTH + 63.5, 330]
            elif name == "security":
                pos = [self.width - HUD_WIDTH + 113.5, 330]
            img_tmp = image.copy()
            rect    = img_tmp.get_rect(topleft=pos)
            tiles.append(
                {
                    "name" : name,
                    "icon" : img_tmp,
                    "pos"  : pos,
                    "image" : images[name],
                    "rect" : rect
                }
            )

        return tiles
    
    def update(self):
        mouse_pos = pg.mouse.get_pos()
        mouse_state = pg.mouse.get_pressed()
        if mouse_state[2]:
            self.selected_tile = None
        for tile in self.tiles:
            if tile["rect"].collidepoint(mouse_pos):
                if mouse_state[0]:
                    self.selected_tile = tile

    def load_images(self):


        right_hud = pg.image.load("graphics/paneling/right_hud.png").convert_alpha()
        icon_1 = pg.image.load("graphics/paneling/paneling_00020.png").convert_alpha()
        overlays_case = pg.image.load("graphics/paneling/overlays_case.png").convert_alpha()
        
        clear = pg.image.load("graphics/shovel.png").convert_alpha()
        road = pg.image.load("graphics/paneling/road.png").convert_alpha()
        housing = pg.image.load("graphics/housing.png").convert_alpha()
        water = pg.image.load("graphics/water.png").convert_alpha()
        governments = pg.image.load("graphics/government.png").convert_alpha()
        security = pg.image.load("graphics/security.png").convert_alpha()
        images = {
            "right_hud": right_hud,
            "icon_1": icon_1,
            "overlays_case": overlays_case,
            "clear": clear,
            "road": road,
            "housing" : housing,
            "water" : water,
            "government" : governments,
            "security" : security
        }
        return images
    

    def load_icons(self):
        build_housing = pg.image.load("graphics/paneling/build_housing.png").convert_alpha()
        water_structures = pg.image.load("graphics/paneling/water_structures.png").convert_alpha()
        clear = pg.image.load("graphics/paneling/clear.png").convert_alpha()
        road = pg.image.load("graphics/paneling/road.png").convert_alpha()
        government_structures = pg.image.load("graphics/paneling/government_structures.png").convert_alpha()
        security_structures = pg.image.load("graphics/paneling/security_structures.png").convert_alpha()
        icons = {
            "housing": build_housing,
            "water": water_structures, 
            "clear": clear,
            "road": road,
            "government": government_structures,
            "security": security_structures, 
        }
        return icons

    def scale_image(self, image, w=None, h=None):

        if (w == None) and (h == None):
            pass
        elif h == None:
            scale = w / image.get_width()
            h = scale * image.get_height()
            image = pg.transform.scale(image, (int(w), int(h)))

        elif w == None:
            scale = h / image.get_width()
            w = scale * image.get_height()
            image = pg.transform.scale(image, (int(w), int(h)))

        else:
            image = pg.transform.scale(image, (int(w), int(h)))

        return image
