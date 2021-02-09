# -*- coding:utf-8 -*-
""" This is a task of prime shields """

import sys
import math
import random
import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_SPACE

WIDTH = 640
HEIGHT = 480
RADIUS = 60
HEX_POS = [(0, 0), (0, -120), (0, 120), (-110, -60), (110, -60), (-110, 60), (110, 60)]

OPEN_COUNT = 0
CHECKED = [False for _ in range(7)]

RED = (255, 0, 0)
YELLOW = (255, 255, 0)
color = [RED, YELLOW]
COLORS = random.choices(color, k=7, weights=[2, 5])
print(COLORS)

class Hexagon:
    def __init__(self):
        self.pointlist = []

    def draw(self, pos, color):
        for i in range(6):
            dx = pos[0] + RADIUS * math.cos((math.radians(i*60)))
            dy = pos[1] + RADIUS * math.sin((math.radians(i*60)))
            self.pointlist.append((dx, dy))
        pygame.draw.polygon(SURFACE, color, self.pointlist)

pygame.init()
SURFACE = pygame.display.set_mode([WIDTH, HEIGHT])
FPSCLOCK = pygame.time.Clock()

def main():
    color = (255, 255, 0)

    tiles = []
    for i in range(7):
        tiles.append(pygame.Rect(int(WIDTH/2+HEX_POS[i][0]-39), int(HEIGHT/2+HEX_POS[i][1]-39), int(78), int(78)))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for tile in tiles:
                    if tile.collidepoint(event.pos):
                        print("Tile was pressed")
                        COLORS[tiles.index(tile)] = RED

        SURFACE.fill((0, 0, 0))

        pygame.draw.circle(SURFACE, (55, 55, 55), (int(WIDTH/2), int(HEIGHT/2)), 220)

        # tile = pygame.Rect(int(WIDTH/2-39), int(HEIGHT/2-39), int(78), int(78))

        hexagons = []
        for i in range(7):
            pygame.draw.rect(SURFACE, (0, 0, 0), tiles[i])
            hexagons.append(Hexagon())
            hexagons[i].draw((WIDTH/2 + HEX_POS[i][0], HEIGHT/2 + HEX_POS[i][1]), COLORS[i])

        pygame.display.update()
        FPSCLOCK.tick(20)

if __name__ == '__main__':
    main()
