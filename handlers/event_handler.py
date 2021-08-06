import pygame.event
from setup import DIRECTIONS


class EventHandler:
    def __init__(self, snk_game):
        self.snk_game = snk_game

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.snk_game.is_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if self.snk_game.snake.direction != DIRECTIONS["down"]:
                        self.snk_game.snake.change_direction(DIRECTIONS["up"])
                if event.key == pygame.K_DOWN:
                    if self.snk_game.snake.direction != DIRECTIONS["up"]:
                        self.snk_game.snake.change_direction(DIRECTIONS["down"])
                if event.key == pygame.K_LEFT:
                    if self.snk_game.snake.direction != DIRECTIONS["right"]:
                        self.snk_game.snake.change_direction(DIRECTIONS["left"])
                if event.key == pygame.K_RIGHT:
                    if self.snk_game.snake.direction != DIRECTIONS["left"]:
                        self.snk_game.snake.change_direction(DIRECTIONS["right"])
