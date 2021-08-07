import pygame
from setup import *


class Window:
    def __init__(self, pnk_game):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Pinky')

        self.pnk_game = pnk_game

    def update_window(self):
        pygame.draw.rect(self.screen, "#5B84B1FF", (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
        xf = self.pnk_game.food.location[0] * PART_WIDTH + OFFSET_X
        yf = self.pnk_game.food.location[1] * PART_HEIGHT + OFFSET_Y
        pygame.draw.circle(self.screen, "#FC766AFF", (xf + 16, yf + 16), 16)
        self.pnk_game.snake.draw(self.screen)
        for j in range(BOARD_HEIGHT):
            for i in range(BOARD_WIDTH):
                xi = i * PART_WIDTH + OFFSET_X
                yi = j * PART_HEIGHT + OFFSET_Y
                pygame.draw.rect(self.screen, "#FC766AFF", (xi, yi, PART_WIDTH, PART_HEIGHT), 2)
        font = pygame.font.SysFont(None, 23)
        txt = font.render("Current score - " + str(self.pnk_game.scoreboard.current), False, BLACK)
        txt2 = font.render("Best score - " + str(self.pnk_game.scoreboard.best), False, BLACK)
        self.screen.blit(txt, (100, 697))
        self.screen.blit(txt2, (400, 697))
        pygame.display.update()
