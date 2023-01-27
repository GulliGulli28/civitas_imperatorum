import pygame as pg
from game import Game



def main():

    running = True
    playing = True


    pg.init()

    pg.mixer.init()
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    clock = pg.time.Clock()
    #pg.mixer.music.load("Time_Time.mp3")
    

    # implement menus

    # implement game
    game = Game(screen, clock)

    while running:

        # start menu goes here

        while playing:
            # game loop here
            game.run()


if __name__ == "__main__":
    main()


Dictionnaire_Batiment={}

liste_sprites_NE_resident=[]
liste_sprites_SW_resident=[]
liste_sprites_NW_resident=[]
liste_sprites_SE_resident=[]

liste_sprites_NE_walker=[]
liste_sprites_SW_walker=[]
liste_sprites_NW_walker=[]
liste_sprites_SE_walker=[]




liste_sprites_NE_worker=[]
liste_sprites_SW_worker=[]
liste_sprites_NW_worker=[]
liste_sprites_SE_worker=[]

for i in range(0,12):
    liste_sprites_NE_resident.append("C3_sprites/C3/0_fired_00001"+"png")
    liste_sprites_SW_resident.append("C3_sprites/C3/0_fired_00001"+"png")
    liste_sprites_NW_resident.append("C3_sprites/C3/0_fired_00001"+"png")
    liste_sprites_SE_resident.append("C3_sprites/C3/0_fired_00001"+"png")

    liste_sprites_NE_walker.append("C3_sprites/C3/citizen02_00"+str(615+i*8)+".png")
    liste_sprites_SW_walker.append("C3_sprites/C3/citizen02_00"+str(619+i*8)+".png")
    liste_sprites_NW_walker.append("C3_sprites/C3/citizen02_00"+str(621+i*8)+".png")
    liste_sprites_SE_walker.append("C3_sprites/C3/citizen02_00"+str(617+i*8)+".png")

    liste_sprites_NE_worker.append("C3_sprites/C3/0_fired_00001"+"png")
    liste_sprites_SW_worker.append("C3_sprites/C3/0_fired_00001"+"png")
    liste_sprites_NW_worker.append("C3_sprites/C3/0_fired_00001"+"png")
    liste_sprites_SE_worker.append("C3_sprites/C3/0_fired_00001"+"png")
