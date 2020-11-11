import pygame
from pygame.locals import *

pygame.init()

w = 900
h = 900

win = pygame.display.set_mode((w, h))

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

Color_List = [white, blue, black, red, green]
win.fill(white)
pygame.display.update()

while True:
    pass
