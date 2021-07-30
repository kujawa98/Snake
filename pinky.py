import pygame
from setup import *

from event_handler import EventHandler
from snake import Snake
from food import Food
from collision_handler import CollisionHandler


class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption('Pinky')

        self.snake = Snake()
        self.food = Food(self.snake)
        self.collision_handler = CollisionHandler(self.snake)

        self.clock = pygame.time.Clock()
        self.event_handler = EventHandler(self)

        self.is_running = True

    def run(self):
        food = self.food.generate_food()
        while self.is_running:
            self.clock.tick(10)
            if self.collision_handler.food_collision(food):
                self.snake.append_part()
                food = self.food.generate_food()
            if self.collision_handler.check_collision():
                self.is_running = False
            self.food.resolve_spots(self.snake)
            self.snake.move()
            self.event_handler.handle_events()
            self.update_screen(food)

    def update_screen(self, food):
        self.screen.fill("#FC766AFF")
        for i in range(BOARD_WIDTH):
            for j in range(BOARD_HEIGHT):
                pygame.draw.rect(self.screen, "#5B84B1FF",
                                 (i * PART_WIDTH + OFFSET_X, j * PART_HEIGHT + OFFSET_Y, PART_WIDTH, PART_HEIGHT))
                pygame.draw.rect(self.screen, "#FC766AFF",
                                 (i * PART_WIDTH + OFFSET_X, j * PART_HEIGHT + OFFSET_Y, PART_WIDTH, PART_HEIGHT), 1,
                                 25)
        pygame.draw.rect(self.screen, "#FC766AFF",
                         (food[0] * PART_WIDTH + OFFSET_X,
                          food[1] * PART_HEIGHT + OFFSET_Y, PART_WIDTH, PART_HEIGHT), 0, 16)
        for part in self.snake.parts:
            part.draw(self.screen)
        pygame.display.update()


if __name__ == '__main__':
    snk_game = SnakeGame()
    snk_game.run()
