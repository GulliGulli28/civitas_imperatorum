import pygame, cv2
from interface import draw_background

pygame.init()

# création fenêtre
screen_height = 1500
screen_width = 800
#screen = pygame.display.set_mode((screen_height, screen_width))
screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
pygame.display.set_caption('Test Buttons')

# Redimensionnement images
# main_image = cv2.imread("main_image.jpg")
# resized = cv2.resize(main_image, (screen_height, screen_width))
# cv2.imwrite("main_image_r.jpg", resized )


# importation des images dans pygame
#bg = pygame.image.load("main_image_r.jpg")
new_game = pygame.image.load("Picture1.jpg")
load_game = pygame.image.load("Picture2.png")
save_game = pygame.image.load("Picture3.png")

class Image():

    def __init__(self, path_without_extension: object, extension: object) -> object:
        self.path = path_without_extension
        self.extension = extension
        self.image = pygame.image.load(self.path + self.extension)

        #self.rect=self.image.get_rect()

    def resize(self, height, width):
        image = cv2.imread(self.path + self.extension)
        cv2.imwrite(self.path + "_r" + self.extension, cv2.resize(image, (height, width)))
        assert isinstance(self.extension, object)
        self.image = pygame.image.load(self.path + "_r" + self.extension)


bg = Image("C3_sprites/C3/C3title_00001", ".png")


#new_game = Image("new_game", ".png")
#load_game = Image("load_game", ".png")

#click_button = Image("click" ,".png" )
#load_game.resize(400, 200)
load_game=pygame.transform.scale(load_game,(300,50))
load_game_rect=load_game.get_rect()
new_game=pygame.transform.scale(new_game,(300,50))
new_game_rect=new_game.get_rect()
save_game=pygame.transform.scale(save_game,(300,50))
save_game_rect=save_game.get_rect()

"""class Button():
class Button(pygame.sprite.Sprite):

    def __init__(self, x, y, button, scale):
        width = button.image.get_width()
        height = button.image.get_height()
        self.resized = pygame.transform.scale(button.image, (int(width * scale), int(height * scale)))
        self.rect = button.image.get_rect()
        self.rect.topleft = (x,y)
        self.x = x
        self.y = y
        self.clicked = False

    def draw(self, surface):
        action = False
        #position de la souris
        pos = pygame.mouse.get_pos()
        #verifier les conditions du clicked
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False :
                self.clicked = True
                action = True
        self.rect = pygame.Rect(x, y, width*scale, height*scale)

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        # dessin du bouton sur l'écran
        surface.blit(self.resized, (self.rect.x, self.rect.y))

        return action """
#initialiser la variable menu
menu = False
def bouton(panel, mouse):
    if panel.x + 300 > mouse[0] > panel.x and panel.y + 50 > mouse[1] >panel.y:
        return True
    else:
        return False


def menu1():

    global running
    menu = True
    screen.blit(load_game, (600, 500))
    pygame.display.flip()
    load_game_rect.x = 600
    load_game_rect.y = 500
    screen.blit(save_game, (600, 400))
    pygame.display.flip()
    save_game_rect.x = 600
    save_game_rect.y = 400
    screen.blit(new_game, (600, 300))
    pygame.display.flip()
    new_game_rect.x = 600
    new_game_rect.y = 300

    while menu:
        for event1 in pygame.event.get():
            if event1.type == pygame.QUIT:
                menu = False
                running = False
                pygame.quit()
                print("fermeture du jeu")
            elif event1.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if bouton(load_game_rect, mouse):
                    menu = False
                    running = False
                    pygame.quit()
                elif bouton(new_game_rect,mouse):
                    bg = Image("test", ".png")
                    bg.resize(screen_height, screen_width)
                    screen.blit(bg.image, (0, 0))
                    pygame.display.flip()








# création des boutons
#NG_button = Button(400, 200, new_game, 0.5)
#LG_button = Button(400, 400, load_game, 0.5)
#click = Button(1200,700,click_button,0.5)

# Boucle de jeu
running = True
#c = 0
c = 0
menuMode = False
gameMode = False

bg.resize(screen_height, screen_width)
screen.blit(bg.image, (0, 0))
pygame.display.flip()
#pygame.display.flip()
while running:
    #bg.resize(screen_height, screen_width)
    #screen.blit(bg.image, (0, 0))
    #if c==0:
        #screen.blit(bg.image, (0, 0))
        #c = 1
   # pygame.display.flip()
    for event in pygame.event.get():
        if menu == True :
            menu1()
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")
        elif event.type == pygame.MOUSEBUTTONDOWN :
            bg = Image("C3_sprites/C3/0_fired_00001", ".png")
            bg.resize(screen_height, screen_width)
            screen.blit(bg.image, (0, 0))
            pygame.display.flip()
            menu = True
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
            draw_background(screen,screen_width,screen_height)
      # mise à jour de l'interface




