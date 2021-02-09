# -*- coding:utf-8 -*-
""" This is a task of unlock manifolds """

import sys
import random
import pygame
from pygame.locals import QUIT

#=== パラメータ設定 ===#
# 画面サイズの設定
WIDTH = 5
HEIGHT = 2
SIZE = 100

# 色の指定
GRAY = (255, 255, 255)
BLUE = (0, 0, 255)
AQUA = (0, 255, 255)
GREEN = (0, 255, 0)

OPEN_COUNT = 1
CHECKED = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
COLORS = [AQUA for _ in range(10)]

# pygameの初期化
pygame.init()
SURFACE = pygame.display.set_mode([WIDTH*SIZE, HEIGHT*SIZE])
FPSCLOCK = pygame.time.Clock()

def main():
    # クリアメッセージの設定
    font = pygame.font.SysFont(None, 72)
    message_clear = font.render("Task Completed!", True, GRAY)
    message_rect = message_clear.get_rect()
    message_rect.center = (WIDTH*SIZE/2, HEIGHT*SIZE/2)

    # タイルに表示する数字の初期化
    random_list = list(range(1,11))
    random.shuffle(random_list)
    new_list = [random_list[0:5], random_list[5:10]]

    # タイルの初期化
    buttons = []
    for i in range(2):
        for j in range(5):
            buttons.append(pygame.Rect(SIZE*j, SIZE*i, SIZE, SIZE))

    while True:
        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 数字の順番に押されているか判定
                for button in buttons:
                    if button.collidepoint(event.pos):
                        global OPEN_COUNT
                        index = buttons.index(button)
                        print("num {} was pressed".format(index))
                        if random_list[index] == OPEN_COUNT:
                            COLORS[buttons.index(button)] = GREEN
                            OPEN_COUNT += 1

        # 背景の描画
        SURFACE.fill((0, 0, 0))
        # タイルの描画
        for i in range(10):
            pygame.draw.rect(SURFACE, COLORS[i], buttons[i], 0)
            pygame.draw.rect(SURFACE, BLUE, buttons[i], 2)
        # 数字の描画
        for i in range(2):
            for j in range(5):
                box_number = font.render("{}".format(new_list[i][j]), True, BLUE)
                box_number_rect = box_number.get_rect()
                box_number_rect.center = (SIZE*j+SIZE/2, SIZE*i+SIZE/2)
                SURFACE.blit(box_number, box_number_rect.topleft)

        # クリアしたらメッセージ表示
        if OPEN_COUNT > 10:
            SURFACE.blit(message_clear, message_rect.topleft)

        pygame.display.update()
        FPSCLOCK.tick(10)

if __name__ == '__main__':
    main()
