import pygame
from setup import *


class Window:
    def __init__(self, pnk_game):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Pinky')
        self.grid_image = pygame.image.load('imgs/grid_map.png').convert_alpha()
        self.pnk_game = pnk_game

    def update_window(self):
        pygame.draw.rect(self.screen, "#5B84B1FF", (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
        xf = self.pnk_game.food.location[0] * PART_WIDTH + OFFSET_X
        yf = self.pnk_game.food.location[1] * PART_HEIGHT + OFFSET_Y
        pygame.draw.circle(self.screen, "#FC766AFF", (xf + 16, yf + 16), 16)
        self.pnk_game.snake.draw(self.screen)
        self.pnk_game.scoreboard.draw(self.screen)
        self.screen.blit(self.grid_image, (OFFSET_X, OFFSET_Y))
        pygame.display.update()
