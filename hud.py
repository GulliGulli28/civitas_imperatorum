import pygame as pg


class Hud:

    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.hud_colour = (198, 155, 93, 175)

        # resources hud
        self.resources_surface = pg.Surface((width, height * 0.02), pg.SRCALPHA)
        self.resources_surface.fill(self.hud_colour)

        # right hud
        self.build_surface = pg.Surface((width * 0.106, height))
        self.build_surface.fill(self.hud_colour)

        # select hud
        self.select_surface = pg.Surface((width * 0.3, height * 0.2), pg.SRCALPHA)
        self.select_surface.fill(self.hud_colour)

        self.images = self.load_images()

    def draw(self, screen):
        images = self.load_images()
        right_hud_width = images["right_hud"].get_width()
        icon_1_width, icon_1_height = images["icon_1"].get_width(), images["icon_1"].get_height()
        # resources hud
        screen.blit(self.resources_surface, (0, 0))

        # build hud
        screen.blit(self.build_surface, (self.width - self.build_surface.get_width(), self.resources_surface.get_height()))

        screen.blit(images["right_hud"], (self.width - right_hud_width, self.height * 0.02))
        screen.blit(images["build_housing"], (self.width - right_hud_width + 13.5, 295))
        screen.blit(images["clear"], (self.width - right_hud_width + 63, 295))
        screen.blit(images["road"], (self.width - right_hud_width + 113, 295))
        screen.blit(images["water_structures"], (self.width - right_hud_width + 13.5, 330))
        screen.blit(images["government_structures"], (self.width - right_hud_width + 63.5, 330))
        screen.blit(images["security_structures"], (self.width - right_hud_width + 113.5, 330))

        screen.blit(images["icon_1"], (self.width - icon_1_width, self.height - icon_1_height))
        screen.blit(images["overlays_case"], (self.width - right_hud_width + 4.5, self.resources_surface.get_height() + 3.5))
        # select hud
        # screen.blit(self.select_surface, (self.width * 0.35, self.height * 0.79))

        # OVERLAY TEXT
        font = pg.font.Font(None, 34)
        overlays_text = font.render("Overlays", True, (0, 0, 0))
        screen.blit(overlays_text, (self.width-right_hud_width+10, 21))
        # for tile in self.tiles:
        # screen.blit(tile["icon"], tile["rect"].topleft)



    def load_images(self):

        block = pg.image.load("graphics/block.png").convert_alpha()
        tree = pg.image.load("graphics/tree.png").convert_alpha()
        rock = pg.image.load("graphics/rock.png").convert_alpha()
        road = pg.image.load("graphics/paneling/road.png").convert_alpha()
        build_housing = pg.image.load("graphics/paneling/build_housing.png")
        water_structures = pg.image.load("graphics/paneling/water_structures.png")
        right_hud = pg.image.load("graphics/paneling/right_hud.png")
        clear = pg.image.load("graphics/paneling/clear.png")
        government_structures = pg.image.load("graphics/paneling/government_structures.png")
        security_structures = pg.image.load("graphics/paneling/security_structures.png")
        icon_1 = pg.image.load("graphics/paneling/paneling_00020.png")
        overlays_case = pg.image.load("graphics/paneling/overlays_case.png")

        images = {
            "block": block, "tree": tree, "rock": rock,
            "road": road, "build_housing": build_housing,
            "water_structures": water_structures, "right_hud": right_hud, "clear": clear,
            "government_structures": government_structures, "icon_1": icon_1,
            "security_structures": security_structures, "overlays_case": overlays_case

        }
        return images

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
