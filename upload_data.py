# -*- coding:utf-8 -*-
""" This is a task of upload data """

import sys
import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_SPACE

WIDTH = 640
HEIGHT = 480

RED = (255, 0, 0)
YELLOW = (255, 255, 0)

pygame.init()
SURFACE = pygame.display.set_mode([WIDTH, HEIGHT])
FPSCLOCK = pygame.time.Clock()

def main():
    flag = False
    cnt = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos):
                    print("Tile was pressed")
                    flag = True


        SURFACE.fill((0, 55, 255))

        # pygame.draw.circle(SURFACE, (55, 55, 55), (int(WIDTH/2), int(HEIGHT/2)), 220)

        button = pygame.Rect(int(WIDTH/2-50), int(HEIGHT/2-50), 100, 100)
        pygame.draw.rect(SURFACE, RED, button)

        if flag:
            prg_bg = pygame.Rect(48, 38, 564, 24)
            prg_bar = pygame.Rect(50, 40, int(560*cnt/100), 20)
            pygame.draw.rect(SURFACE, (0, 0, 0), prg_bg, 4)
            pygame.draw.rect(SURFACE, (0, 255, 0), prg_bar)
            if cnt < 100:
                cnt += 1 

        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == '__main__':
    main()
