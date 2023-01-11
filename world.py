import pygame as pg
import random
import noise
from settings import TILE_SIZE


class World:

    def __init__(self, grid_length_x, grid_length_y, width, height):
        self.grid_length_x = grid_length_x
        self.grid_length_y = grid_length_y
        self.width = width
        self.height = height

        self.perlin_scale = grid_length_x / 2

        self.grass_tiles = pg.Surface(
            (grid_length_x * TILE_SIZE * 2, grid_length_y * TILE_SIZE + 2 * TILE_SIZE)).convert_alpha()
        self.tiles = self.load_images()
        self.world = self.create_world()
        
        self.temp_tile = None

    
    def update(self,hud,camera):
        if hud.selected_tile is not None: 
            name = hud.selected_tile["name"]
            img = hud.selected_tile["image"].copy()
            img.set_alpha(100)
            (pos_x,pos_y) = pg.mouse.get_pos()
            (x,y)   = self.mouse_to_grid(pos_x,pos_y,camera)
            if self.is_placeable(hud,(x,y)):
                if x <= self.grid_length_x and y <= self.grid_length_y:
                    render_pos = self.world[x][y]["render_pos"]
                    iso_poly   = self.world[x][y]["iso_poly"]
                    self.temp_tile = {
                        "tile" : name,
                        "image": img,
                        "render_pos": render_pos,
                        "iso_poly": iso_poly
                        }
                if pg.mouse.get_pressed()[0]:
                    self.world[x][y]["tile"] = self.temp_tile["tile"]
                    self.temp_tile = None
        if hud.selected_tile is None:
            self.temp_tile = None
        



    def create_world(self):

        world = []

        for grid_x in range(self.grid_length_x):
            world.append([])
            for grid_y in range(self.grid_length_y):
                world_tile = self.grid_to_world(grid_x, grid_y)  # dictionnaire
                world[grid_x].append(world_tile)

                render_pos = world_tile["render_pos"]
                self.grass_tiles.blit(self.tiles["block"],
                                      (render_pos[0] + self.grass_tiles.get_width() / 2, render_pos[1]))

        return world
    
    def draw(self,screen,camera):
        screen.fill((0, 0, 0))
        screen.blit(self.grass_tiles, (camera.scroll.x, camera.scroll.y))

        for x in range(self.grid_length_x):
            for y in range(self.grid_length_y):

                #sq = self.world.world[x][y]["cart_rect"]
                #rect = pg.Rect(sq[0][0], sq[0][1], TILE_SIZE, TILE_SIZE)
                #pg.draw.rect(self.screen, (0, 0, 255), rect, 1)
                render_pos= self.world[x][y]["render_pos"]

                tile = self.world[x][y]["tile"]
                if tile != "":
                    screen.blit(self.tiles[tile],
                                    (render_pos[0] + self.grass_tiles.get_width()/2 + camera.scroll.x,
                                     render_pos[1] - (self.tiles[tile].get_height() - TILE_SIZE) + camera.scroll.y))

                # p = self.world.world[x][y]["iso_poly"]
                # p = [(x + self.width/2, y + self.height/4) for x, y in p]
                # pg.draw.polygon(self.screen, (255, 0, 0), p, 1)
        if self.temp_tile is not None:
            render_pos = self.temp_tile["render_pos"]    
            screen.blit(self.temp_tile["image"],
                                (render_pos[0] + self.grass_tiles.get_width()/2 + camera.scroll.x,
                                render_pos[1] - (self.temp_tile["image"].get_height() - TILE_SIZE) + camera.scroll.y))


    def grid_to_world(self, grid_x, grid_y):  # Cette fonction retourne un dictionnaire contenant les coordonnées de chaque tuile

        rect = [
            (grid_x * TILE_SIZE, grid_y * TILE_SIZE),
            (grid_x * TILE_SIZE + TILE_SIZE, grid_y * TILE_SIZE),
            (grid_x * TILE_SIZE + TILE_SIZE, grid_y * TILE_SIZE + TILE_SIZE),
            (grid_x * TILE_SIZE, grid_y * TILE_SIZE + TILE_SIZE)
        ]

        iso_poly = [self.cart_to_iso(x, y) for x, y in rect]

        minx = min([x for x, y in iso_poly])
        miny = min([y for x, y in iso_poly])

        r = random.randint(1, 100)
        perlin = 100 * noise.pnoise2(grid_x / self.perlin_scale, grid_y / self.perlin_scale)

        if (perlin >= 15) or (perlin <= -35):
            tile = "tree"
        else:
            if r == 1:
                tile = "tree"
            elif r == 2:
                tile = "rock"
            else:
                tile = ""

        out = {
            "grid": [grid_x, grid_y],
            "cart_rect": rect,
            "iso_poly": iso_poly,
            "render_pos": [minx, miny],
            "tile": tile
        }

        return out

    def cart_to_iso(self, x, y):
        iso_x = x - y
        iso_y = (x + y) / 2
        return iso_x, iso_y

    def iso_to_cart(self, iso_x, iso_y):
        x = iso_y + iso_x/2
        y = iso_y - iso_x/2
        return x, y

    def mouse_to_grid(self, x, y, camera):
        (cart_x, cart_y)= self.iso_to_cart(x - self.grass_tiles.get_width()/2 - camera.scroll.x, y - camera.scroll.y)
        x = int(cart_x // TILE_SIZE)
        y = int(cart_y // TILE_SIZE)
        return x,y

    def load_images(self):
        land= pg.image.load("graphics/land.png")
        tree= pg.image.load("graphics/tree.png")
        rock=pg.image.load("graphics/rock.png")

        road = pg.image.load("graphics/paneling/road.png").convert_alpha()
        housing = pg.image.load("graphics/housing.png").convert_alpha()
        water = pg.image.load("graphics/water.png").convert_alpha()
        governments = pg.image.load("graphics/government.png").convert_alpha()
        security = pg.image.load("graphics/security.png").convert_alpha()

        return {"block":land, "tree":tree, "rock": rock,
            "road": road,
            "housing" : housing,
            "water" : water,
            "government" : governments,
            "security" : security
        }

    def is_placeable(self,hud, grid_pos):
        mouse_is_off_panel = True
        mouse = pg.mouse.get_pos()
        for rect in [hud.resources_rect, hud.build_rect, hud.select_rect]:
            if pg.Rect.collidepoint(rect,mouse):
                mouse_is_off_panel = False
        return mouse_is_off_panel

    def create_batiment():
        x,y = pygame.mouse.get_pos()



        