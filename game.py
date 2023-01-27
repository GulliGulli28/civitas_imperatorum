import pygame as pg
import sys
from world import World
from people import people
from settings import TILE_SIZE
from utils import draw_text
from camera import Camera
from hud import Hud



class Game:

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

        #people
        self.people = people(self.world)


    def run(self):
        self.playing = True
        while self.playing:            
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()
            self.music()
            
    def events(self):
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
        self.people.update()

    def draw(self):
        self.world.draw(self.screen,self.camera)
        self.people.draw(self.screen,self.camera)
        self.hud.draw(self.screen)
        draw_text(
            self.screen,
            'fps={}'.format(round(self.clock.get_fps())),
            25,
            (255, 255, 255),
            (10, 10)
        )


              #  p = self.world.world[x][y]["iso_poly"]
               # p = [(x + self.width/2, y + self.height/4) for x, y in p]
                #pg.draw.polygon(self.screen, (255, 0, 0), p, 1)
           

        pg.display.flip()

        
                
    def music(self):
        pass
        '''
            if pg.mixer.music.get_busy():
                pass
            else:
                pg.mixer.music.load("Time_Time.mp3")
                pg.mixer.music.play()
        '''

