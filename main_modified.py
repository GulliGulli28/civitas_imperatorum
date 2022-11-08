import pygame, cv2, pytmx, pyscroll

screen_height = 1080
screen_width = 720

# création fenêtre
screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption('Test Buttons')

# insertion map
tmx_data = pytmx.util_pygame.load_pygame('carte.tmx')
map_data = pyscroll.data.TiledMapData(tmx_data)
map_layer = pyscroll.orthographic.BufferedRenderer(map_data, screen.get_size())
# dessiner le groupe de calques
group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer = 1)

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


class Button():

    def __init__(self, x, y, button, scale):
        width = button.image.get_width()
        height = button.image.get_height()
        self.resized = pygame.transform.scale(button.image, (int(width * scale), int(height * scale)))
        self.x = x
        self.y = y

    def draw(self):
        # dessin du bouton sur l'écran
        screen.blit(self.resized, (self.x, self.y))


new_game = Image("new_game", ".png")
load_game = Image("load_game", ".png")

# création des boutons
NG_button = Button(400, 200, new_game, 0.5)
LG_button = Button(400, 400, load_game, 0.5)


class Game:

    def run(self):

        running = True
        c = 0
        bg = Image("C3_sprites/C3/C3title_00001", ".png")
        bg.resize(screen_height, screen_width)
        #screen.blit(bg.image, (0, 0))
        group.draw(screen)  #affichage carte
        while running:
            bg.resize(screen_height, screen_width)

            # if c==0:
            # screen.blit(bg.image, (0, 0))
            # c = 1
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = 0
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    bg = Image("C3_sprites/C3/0_fired_00001", ".png")
                    bg.resize(screen_height, screen_width)
                    screen.blit(bg.image, (0, 0))
                    NG_button.draw()
                    LG_button.draw()
                    pygame.display.flip()
game = Game()
game.run()

# Redimensionnement images
# main_image = cv2.imread("main_image.jpg")
# resized = cv2.resize(main_image, (screen_height, screen_width))
# cv2.imwrite("main_image_r.jpg", resized )


# importation des images dans pygame
#bg = pygame.image.load("main_image_r.jpg")
#new_game = pygame.image.load("new_game.png")
#load_game = pygame.image.load("load_game.png")








    # Boucle de jeu

          # mise à jour de l'interface

pygame.quit()
