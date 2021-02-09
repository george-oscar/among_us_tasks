import random

random_list = list(range(1,11))
random.shuffle(random_list)
# print(random_list)

# # def convert_1d_to_2d(l, cols):
# #     return [l[i:i + cols] for i in range(0, len(l), cols)]
# # print(convert_1d_to_2d(random_list, 5))

new_list = [random_list[0:5], random_list[5:10]]

# print(new_list)

#     CHECKED = [[0 for _ in range(5)] for _ in range(2)]
# print(CHECKED)

import sys
import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_SPACE

SIZE = 100
WIDTH = 5
HEIGHT = 2
GRAY = (255, 255, 255)
BLUE = (0, 0, 255)
AQUA = (0, 255, 255)
GREEN = (0, 255, 0)

OPEN_COUNT = 1
CHECKED = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
COLORS = [AQUA for _ in range(10)]

pygame.init()
SURFACE = pygame.display.set_mode([WIDTH*SIZE, HEIGHT*SIZE])
FPSCLOCK = pygame.time.Clock()

def main():
    font = pygame.font.SysFont(None, 72)
    message_clear = font.render("Task Completed!", True, GRAY)
    message_rect = message_clear.get_rect()
    message_rect.center = (WIDTH*SIZE/2, HEIGHT*SIZE/2)

    buttons = []
    for i in range(2):
        for j in range(5):
            buttons.append(pygame.Rect(SIZE*j, SIZE*i, SIZE, SIZE))


    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.collidepoint(event.pos):
                        global OPEN_COUNT
                        index = buttons.index(button)
                        print("num {} was pressed".format(index))
                        if random_list[index] == OPEN_COUNT:
                            COLORS[buttons.index(button)] = GREEN
                            OPEN_COUNT += 1

        SURFACE.fill((0, 0, 0))
        for i in range(10):
            pygame.draw.rect(SURFACE, COLORS[i], buttons[i], 0)
            pygame.draw.rect(SURFACE, BLUE, buttons[i], 2)
        for i in range(2):
            for j in range(5):
                box_number = font.render("{}".format(new_list[i][j]), True, BLUE)
                box_number_rect = box_number.get_rect()
                box_number_rect.center = (SIZE*j+SIZE/2, SIZE*i+SIZE/2)
                SURFACE.blit(box_number, box_number_rect.topleft)

        if OPEN_COUNT > 10:
            SURFACE.blit(message_clear, message_rect.topleft)

        pygame.display.update()
        FPSCLOCK.tick(10)

if __name__ == '__main__':
    main()

