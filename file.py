import pygame
from pygame.locals import *
import random

pygame.init()

w = 900
h = 900

win = pygame.display.set_mode((w, h))

# ---------- Variables -------
x = w // 2
y = h// 2

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


while True:
