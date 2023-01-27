import pygame as pg
import sys
from world import World
from settings import TILE_SIZE
from utils import draw_text
from camera import Camera
from hud import Hud
import cv2
#pg.font.init()
#pg.display.init()

class Image():

    def __init__(self, path_without_extension: object, extension: object) -> object:
        self.path = path_without_extension
        self.extension = extension
        self.pg = pg
        self.image = self.pg.image.load(self.path + self.extension)

        #self.rect=self.image.get_rect()

    def resize(self, height, width):
        image = cv2.imread(self.path + self.extension)
        cv2.imwrite(self.path + "_r" + self.extension, cv2.resize(image, (height, width)))
        assert isinstance(self.extension, object)
        self.image = pg.image.load(self.path + "_r" + self.extension)



class Game:
    #pg.font.init()
    new_game = pg.image.load("graphics/paneling/Picture1.png")
    load_game = pg.image.load("graphics/paneling/Picture2.png")
    save_game = pg.image.load("graphics/paneling/Picture3.png")
    #cadre = pg.image.load("graphics/paneling/paneling_00015.png")

    #load_game = pg.transform.scale(load_game, (300, 50))
    #load_game_rect = load_game.get_rect()
    #new_game = pg.transform.scale(new_game, (300, 50))
    #new_game_rect = new_game.get_rect()
    #save_game = pg.transform.scale(save_game, (300, 50))
    #save_game_rect = save_game.get_rect()
    #cadre = pg.transform.scale(cadre, (50, 80))
    #cadre_rect = cadre.get_rect()
    #bg = pg.image.load("C3_sprites/C3/C3title_00001.png")
    screen_height = 1500
    screen_width = 800
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()

        # world
        self.world = World(50,50 , self.width, self.height)

        # camera
        self.camera = Camera(self.width, self.height)

        # hud
        self.hud = Hud(self.width, self.height)


    def run(self):
        #pg.init()
        self.playing = True
        while self.playing:            
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()

    def events(self):
        mouse_pos = pg.mouse.get_pos()
        mouse_pressed = pg.mouse.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()

    def update(self):
        self.camera.update()
        self.hud.update()
        self.world.update(self.hud,self.camera)



    def draw(self):
        self.screen.fill((0, 0, 0))

        self.screen.blit(self.world.grass_tiles, (self.camera.scroll.x, self.camera.scroll.y))

        for x in range(self.world.grid_length_x):
            for y in range(self.world.grid_length_y):

                # sq = self.world.world[x][y]["cart_rect"]
                # rect = pg.Rect(sq[0][0], sq[0][1], TILE_SIZE, TILE_SIZE)
                # pg.draw.rect(self.screen, (0, 0, 255), rect, 1)

                render_pos =  self.world.world[x][y]["render_pos"]
                #self.screen.blit(self.world.tiles["block"], (render_pos[0] + self.width/2, render_pos[1] + self.height/4))

                tile = self.world.world[x][y]["tile"]

                if tile != "":
                    self.screen.blit(self.world.tiles[tile],
                                    (render_pos[0] + self.world.grass_tiles.get_width()/2 + self.camera.scroll.x,
                                     render_pos[1] - (self.world.tiles[tile].get_height() - TILE_SIZE) + self.camera.scroll.y))

                # p = self.world.world[x][y]["iso_poly"]
                # p = [(x + self.width/2, y + self.height/4) for x, y in p]
                # pg.draw.polygon(self.screen, (255, 0, 0), p, 1)

        self.world.draw(self.screen,self.camera)
        self.hud.draw(self.screen)
        draw_text(
            self.screen,
            'fps={}'.format(round(self.clock.get_fps())),
            25,
            (255, 255, 255),
            (10, 10)
        )

        pg.display.flip()

    def menu(self):
        #cadre = Image("graphics/paneling/paneling_00015.png", ".png")
        #pg.font.init()
        cadre = pg.image.load("graphics/paneling/paneling_00015.png")
        running=True
        load_game = pg.transform.scale(self.load_game, (300, 300))
        load_game_rect = load_game.get_rect()
        new_game = pg.transform.scale(self.new_game, (300, 50))
        new_game_rect = new_game.get_rect()
        save_game = pg.transform.scale(self.save_game, (300, 60))
        save_game_rect = save_game.get_rect()
        cadre = pg.transform.scale(cadre, (325, 35))
        cadre_rect = cadre.get_rect()
        load_game_rect.x = 600
        load_game_rect.y = 400
        save_game_rect.x = 600
        save_game_rect.y = 350
        new_game_rect.x = 600
        new_game_rect.y = 300
        cadre_rect.x = 600
        cadre_rect.y = 50
        bg = Image("C3_sprites/C3/C3title_00001", ".png")
        pg.display.flip()
        menu = False

        def bouton(panel, mouse):

            if panel.x + 300 > mouse[0] > panel.x and panel.y + 50 > mouse[1] > panel.y:
                return True
            else:
                return False

        def menu1():

           # global running
            menu = True

            self.screen.blit(cadre, (596, 295))
            pg.display.flip()

            self.screen.blit(cadre, (596, 345))
            pg.display.flip()

            self.screen.blit(cadre, (596, 395))
            pg.display.flip()

            self.screen.blit(self.load_game, (600, 400))

            pg.display.flip()
          #  self.load_game_rect.x = 600
           # self.load_game_rect.y = 500
            self.screen.blit(self.save_game, (600, 350))
            pg.display.flip()
        #    self.save_game_rect.x = 600
         #   self.save_game_rect.y = 400
            self.screen.blit(self.new_game, (600, 300))
            pg.display.flip()
 #           self.new_game_rect.x = 600
  #          self.new_game_rect.y = 300
            #self.screen.blit(self.cadre, (600, 300))
            #pg.display.flip()
            #pg.init()
            while menu:

                for event1 in pg.event.get():
                    if event1.type == pg.QUIT:
                        menu = False
                        self.running = False
                        pg.quit()
                        print("fermeture du jeu")
                    elif event1.type == pg.MOUSEBUTTONDOWN:
                        mouse = pg.mouse.get_pos()
                        if bouton(load_game_rect,mouse):
                            menu = False
                            self.running = False
                            pg.quit()
                            print("fermeture du jeu")
                        elif bouton(new_game_rect, mouse):
                            while self.playing:
                                self.clock.tick(60)
                                self.events()
                                self.update()
                                self.draw()
                           # bg = self.Image("test", ".png")
                            #bg.resize(self.screen_height, self.screen_width)

                            #self.screen.blit(bg.image, (0, 0))
                            #pg.display.flip()

        bg.resize(self.screen_height, self.screen_width)
        self.screen.blit(bg.image, (0, 0))
        pg.display.flip()
        #pg.init()
        #pg.display.init()
        while running:
                # bg.resize(screen_height, screen_width)
                # screen.blit(bg.image, (0, 0))
                # if c==0:
                # screen.blit(bg.image, (0, 0))
                # c = 1
                # pygame.display.flip()
               # pg.init()
                for event in pg.event.get():
                    if menu == True:
                        menu1()
                    if event.type == pg.QUIT:
                        running = False
                        pg.quit()
                        print("fermeture du jeu")
                    elif event.type == pg.MOUSEBUTTONDOWN:
                        #bg = pg.image.load("C3_sprites/C3/0_fired_00001.png")
                        bg = Image("graphics/background/background1", ".png")
                        bg.resize(self.screen_height, self.screen_width)
                        self.screen.blit(bg.image, (0, 0))
                        pg.display.flip()
                        menu = True
