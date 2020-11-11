import pygame
from pygame.locals import *
import random
import sys

pygame.init()

w = 1368
h = 750

win = pygame.display.set_mode((w, h))

# ---------- Variables -------
x = w // 2
y = h // 2

# ---------- Variables -------

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

win.fill(white)
pygame.display.update()


def draw():
    win.fill(white)
    pygame.draw.rect(win, black, (x, y, 20, 20))
    pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        else:
            draw()
