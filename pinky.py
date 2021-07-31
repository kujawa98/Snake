import pygame
from setup import *

from event_handler import EventHandler
from snake import Snake
from food import Food
from collision_handler import CollisionHandler


class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Pinky')

        self.snake = Snake()
        self.food = Food(self.snake)
        self.collision_handler = CollisionHandler(self.snake)

        self.clock = pygame.time.Clock()
        self.event_handler = EventHandler(self)

        self.is_running = True
        self.food_generated = False

    def run(self):
        food = self.food.generate_food()
        while self.is_running:
            self.clock.tick(10)
            if self.collision_handler.check_collision():
                self.is_running = False
            if self.collision_handler.food_collision(food):
                self.snake.append_part()
                self.snake.move()
                self.food.resolve_spots(self.snake)
                food = self.food.generate_food()
                self.food_generated = True
            self.food.resolve_spots(self.snake)
            if not self.food_generated:
                self.snake.move()
            self.food_generated = False
            self.event_handler.handle_events()
            self.update_screen(food)

    def update_screen(self, food):
        pygame.draw.rect(self.screen, "#5B84B1FF",
                         (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
        for j in range(BOARD_HEIGHT):
            for i in range(BOARD_WIDTH):
                pygame.draw.rect(self.screen, "#FC766AFF",
                                 (i * PART_WIDTH, j * PART_HEIGHT, PART_WIDTH, PART_HEIGHT), 1)
        pygame.draw.circle(self.screen, "#FC766AFF", (food[0] * PART_WIDTH + OFFSET_X + 16,
                                                      food[1] * PART_HEIGHT + OFFSET_Y + 16), 16)
        for part in self.snake.parts:
            part.draw(self.screen)
        pygame.display.update()


if __name__ == '__main__':
    snk_game = SnakeGame()
    snk_game.run()
