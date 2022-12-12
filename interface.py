import pygame
from housing import Building,Test_Building,List_Building,place_building

bg = pygame.image.load("C3_sprites/C3/Land1a_00002.png")

#remplacer votre background en isometric
def draw_background(screen,width,height):
    screen.fill("black")
    i = 0
    j = 0
    length_x = int(width/50)
    length_y = int(height/50)
    for i in range(length_y):
        for j in range(length_x):
            pygame.draw.rect(screen,"Blue",(i*50,j*50,bg_width,bg_height),1)

def draw_house(screen):
    place_building(screen,1,5)
    place_building(screen,3,4)
    for Building in List_Building:
        screen.blit(Building.image,(Building.x*50,Building.y*50))