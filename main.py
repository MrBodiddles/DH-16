import pygame, sys
from pygame.locals import QUIT

pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Dungeon Heroes 16')

while True:
    clock.tick(60)

    mousePos = pygame.mouse.get_pos()
    mouseButtons = pygame.mouse.get_pressed()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()