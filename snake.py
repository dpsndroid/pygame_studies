from tkinter import LEFT
import pygame
from pygame.locals import *


pygame.init() 
tela = pygame.display.set_mode((600,600))
pygame.display.set_caption("Snake")

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

snake = [(200,200), (210,200), (220,200)]
my_direction = LEFT


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    tela.fill((0,0,0))
    for pos in snake:
        tela.blit(pygame.Surface((10,10)), pos)
        

    pygame.display.update()
