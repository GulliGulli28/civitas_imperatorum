import pygame as pg
import random
import noise
from settings import TILE_SIZE,HUD_WIDTH
from settings import TILE_SIZE
from Classes.Class_Building.mapBuilding import mapBuilding,BUILDING_TYPE,type_of_building,factory


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
        self.mini_tiles = self.load_mini_image_values()
        self.world = self.create_world()
        self.map_building = mapBuilding()
        self.temp_tile = None

    def update(self, hud, camera):
        grid_pos = self.mouse_to_grid(pg.mouse.get_pos(), camera)
        if self.is_on_panel(hud) or self.is_out_of_map(grid_pos) or hud.selected_tile is None:
            self.temp_tile = None
        else:
            name = hud.selected_tile["name"]
            img = hud.selected_tile["image"].copy()
            img.set_alpha(100)
            render_pos = self.world[grid_pos[0]][grid_pos[1]]["render_pos"]
            iso_poly = self.world[grid_pos[0]][grid_pos[1]]["iso_poly"]
            self.temp_tile = {
                    "tile": name,
                    "image": img,
                    "render_pos": render_pos,
                    "grid": grid_pos,
                    "iso_poly": iso_poly
            }
        if self.temp_tile is not None and pg.mouse.get_pressed()[0]:
            if self.temp_tile["tile"] == "clear":
                self.remove_buiding(self.temp_tile["grid"])
            elif self.is_placeable(grid_pos):
                self.place_building(self.temp_tile["grid"])
            else:
                pass

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

    def draw(self, screen, camera):
        screen.fill((0, 0, 0))
        screen.blit(self.grass_tiles, (camera.scroll.x, camera.scroll.y))

        for x in range(self.grid_length_x):
            for y in range(self.grid_length_y):
                render_pos = self.world[x][y]["render_pos"]
                tile = self.world[x][y]["tile"]
                if self.map_building.map[x][y] is not None:
                        tile = self.map_building.map[x][y].name
                if tile != "":
                    if tile == "road":
                        for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            if not self.is_out_of_map([x + i, y + j]) and self.world[x + i][y + j]["tile"] == "road":
                                tile += str(1)
                            else:
                                tile += str(0)
                    screen.blit(self.tiles[tile],
                                (render_pos[0] + self.grass_tiles.get_width() / 2 + camera.scroll.x,
                                 render_pos[1] - (self.tiles[tile].get_height() - TILE_SIZE) + camera.scroll.y))

        if self.temp_tile is not None:
            render_pos = self.temp_tile["render_pos"]
            grid_pos = self.temp_tile["grid"]
            poly = self.temp_tile["iso_poly"]
            poly = [(x + self.width - TILE_SIZE + camera.scroll.x, y + camera.scroll.y) for x, y in poly]
            screen.blit(self.temp_tile["image"],
                        (render_pos[0] + self.grass_tiles.get_width() / 2 + camera.scroll.x,
                         render_pos[1] - (self.temp_tile["image"].get_height() - TILE_SIZE) + camera.scroll.y))
            if self.temp_tile["tile"] == "clear":
                pg.draw.polygon(screen, (255, 0, 0), poly, 1)
            else:
                if self.is_placeable(self.temp_tile["grid"]) and self.map_building.map[grid_pos[0]][grid_pos[1]] is None:
                    pg.draw.polygon(screen, (0, 255, 0), poly, 1)
                else:
                    pg.draw.polygon(screen, (255, 0, 0), poly, 1)

    def grid_to_world(self, grid_x,
                      grid_y):  # Cette fonction retourne un dictionnaire contenant les coordonnées de chaque tuile

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
        if grid_x == 25:
            tile = "road"

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
        x = iso_y + iso_x / 2
        y = iso_y - iso_x / 2
        return x, y

    def mouse_to_grid(self, mouse_pos, camera):
        (cart_x, cart_y) = self.iso_to_cart(mouse_pos[0] - self.grass_tiles.get_width() / 2 - camera.scroll.x,
                                            mouse_pos[1] - camera.scroll.y)
        x = int(cart_x // TILE_SIZE)
        y = int(cart_y // TILE_SIZE)
        return x, y

    def render_pos_to_poly(self, render_pos):
        (x, y) = render_pos
        iso_poly = [
            (x, y),
            (x + TILE_SIZE, y - TILE_SIZE / 2),
            (x + TILE_SIZE, y + TILE_SIZE),
            (x + TILE_SIZE, y + TILE_SIZE / 2)
        ]
        return iso_poly

    def load_images(self):
        land = pg.image.load("graphics/land.png")
        tree = pg.image.load("graphics/tree.png")
        rock = pg.image.load("graphics/rock.png")

        road_N = pg.image.load("graphics/Land2a_00101.png").convert_alpha()
        road_S = pg.image.load("graphics/Land2a_00105.png").convert_alpha()
        road_W = pg.image.load("graphics/Land2a_00104.png").convert_alpha()
        road_E = pg.image.load("graphics/Land2a_00102.png").convert_alpha()

        road_WE = pg.image.load("graphics/Land2a_00096.png").convert_alpha()
        road_NS = pg.image.load("graphics/Land2a_00095.png").convert_alpha()

        road_ES = pg.image.load("graphics/Land2a_00098.png").convert_alpha()
        road_EN = pg.image.load("graphics/Land2a_00097.png").convert_alpha()
        road_WS = pg.image.load("graphics/Land2a_00099.png").convert_alpha()
        road_WN = pg.image.load("graphics/Land2a_00100.png").convert_alpha()

        road_WEN = pg.image.load("graphics/Land2a_00109.png").convert_alpha()
        road_WES = pg.image.load("graphics/Land2a_00107.png").convert_alpha()
        road_WNS = pg.image.load("graphics/Land2a_00108.png").convert_alpha()
        road_ENS = pg.image.load("graphics/Land2a_00106.png").convert_alpha()

        road_WENS = pg.image.load("graphics/Land2a_00110.png").convert_alpha()

        housing = pg.image.load("graphics/housing.png").convert_alpha()
        well = pg.image.load("graphics/well.png").convert_alpha()
        senate = pg.image.load("graphics/senate.png").convert_alpha()
        security = pg.image.load("graphics/prefecture.png").convert_alpha()

        clear = pg.image.load("graphics/paneling/clear.png").convert_alpha()

        return {"block":land, "tree":tree, "rock": rock,
            "road0000":road_NS,
            "road0001": road_S,"road0010": road_N,"road0100":road_E,"road1000": road_W,
            "road0011": road_NS,"road1100": road_WE,
            "road0101": road_ES,"road0110": road_EN,"road1001":road_WS,"road1010":road_WN,
            "road1110": road_WEN,"road1101":road_WES,"road1011":road_WNS,"road0111":road_ENS,
            "road1111":road_WENS,
            "house" : housing,
            "well" : well,
            "prefecture" : security,
            "senate" : senate,
            "clear" : clear
        }
    
    def load_mini_image_values(self):
        return {"" : (0,255,0),
                "tree"  : (0,255,0),
                "rock"  : (128,128,128),
                "road"  : (255,255,255),
                "house" : (218,165,32)
        }

    def is_out_of_map(self, grid_pos):
        if grid_pos[0] < 0 or grid_pos[0] >= self.grid_length_x or grid_pos[1] < 0 or grid_pos[1] >= self.grid_length_y:
            return True
        elif self.world[grid_pos[0]][grid_pos[1]] is None:
            return True
        else:
            return False

    def is_on_panel(self, hud):
        mouse_is_on_panel = False
        mouse = pg.mouse.get_pos()
        for rect in [hud.resources_rect, hud.build_rect, hud.select_rect]:
            if pg.Rect.collidepoint(rect, mouse):
                mouse_is_on_panel = True
        return mouse_is_on_panel

    def is_placeable(self, grid_pos):
        return self.world[grid_pos[0]][grid_pos[1]]["tile"] == ""

    def place_building(self, grid_pos):
        tile = self.temp_tile["tile"]
        if tile == "road": 
            self.world[grid_pos[0]][grid_pos[1]]["tile"] = "road"
        self.map_building.place_build(tile,grid_pos[0],grid_pos[1])
        self.temp_tile = None

    def remove_buiding(self, grid_pos):
        self.world[grid_pos[0]][grid_pos[1]]["tile"] = ""
        self.map_building.remove_build(grid_pos[0],grid_pos[1])
        self.temp_tile = None


