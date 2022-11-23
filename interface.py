import pygame

bg = pygame.image.load("C3_sprites/C3/Land1a_00002.png")
bg_width = bg.get_width()/2
bg_height = bg.get_height()

def draw_background(screen,width,height):
    screen.fill((225,225,225))
    i = 0
    j = 0
    length_x = int(width/bg_width)
    length_y = int(height/bg_height)
    for i in range(length_y):
        for j in range(length_x):
            screen.blit(bg,(int((i-j)*bg_width),(int((i+j)*bg_height/2))))

