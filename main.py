import pygame, cv2

pygame.init()

# création fenêtre
screen_height = 1080
screen_width = 720
screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption('Test Buttons')

# Redimensionnement images
# main_image = cv2.imread("main_image.jpg")
# resized = cv2.resize(main_image, (screen_height, screen_width))
# cv2.imwrite("main_image_r.jpg", resized )


# importation des images dans pygame
#bg = pygame.image.load("main_image_r.jpg")
#new_game = pygame.image.load("new_game.png")
#load_game = pygame.image.load("load_game.png")


class Image():

    def __init__(self, path_without_extension: object, extension: object) -> object:
        self.path = path_without_extension
        self.extension = extension
        self.image = pygame.image.load(self.path + self.extension)

    def resize(self, height, width):
        image = cv2.imread(self.path + self.extension)
        cv2.imwrite(self.path + "_r" + self.extension, cv2.resize(image, (height, width)))
        assert isinstance(self.extension, object)
        self.image = pygame.image.load(self.path + "_r" + self.extension)


bg = Image("C3_sprites/C3/C3title_00001", ".png")
new_game = Image("new_game", ".png")
load_game = Image("load_game", ".png")


class Button(pygame.sprite.Sprite):

    def __init__(self, x, y, button, scale):
        width = button.image.get_width()
        height = button.image.get_height()
        self.resized = pygame.transform.scale(button.image, (int(width * scale), int(height * scale)))
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, width*scale, height*scale)

    def draw(self):
        # dessin du bouton sur l'écran
        screen.blit(self.resized, (self.x, self.y))


# création des boutons
NG_button = Button(400, 200, new_game, 0.5)
LG_button = Button(400, 400, load_game, 0.5)

# Boucle de jeu
running = True
c = 0
menuMode = False
gameMode = False

bg.resize(screen_height, screen_width)
screen.blit(bg.image, (0, 0))
while running:
    bg.resize(screen_height, screen_width)
    #if c==0:
        #screen.blit(bg.image, (0, 0))
        #c = 1
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0
        elif not menuMode:
            if event.type == pygame.MOUSEBUTTONDOWN:
                menuMode = True
                bg = Image("C3_sprites/C3/0_fired_00001", ".png")
                bg.resize(screen_height, screen_width)
                screen.blit(bg.image, (0, 0))
                NG_button.draw()
                LG_button.draw()
                pygame.display.flip()
        elif  not gameMode:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # 1 = left_click
                pos = pygame.mouse.get_pos()
                if pygame.Rect.collidepoint(LG_button.rect,pos):
                    print("Load game clicked")
                    #faire Load game ici
                if pygame.Rect.collidepoint(NG_button.rect,pos):
                    #print("New game clicked")
                    gameMode = True
        elif gameMode:
            print("now in game mode")
      # mise à jour de l'interface


#création des listes contenant les sprites des charactères
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

pygame.quit()