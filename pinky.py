import pygame

from setup import *

from event_handler import EventHandler
from snake import Snake
from food import FoodGenerator
from collision_handler import CollisionHandler
from scoreboard import Scoreboard


class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Pinky')

        self.snake = Snake()
        self.food_generator = FoodGenerator(self.snake)
        self.collision_handler = CollisionHandler(self.snake)
        self.event_handler = EventHandler(self)
        self.scoreboard = Scoreboard()

        self.clock = pygame.time.Clock()

        self.food = self.food_generator.generate_food()

        self.is_running = True
        self.food_generated = False

    def run(self):
        while self.is_running:
            self.clock.tick(10)
            if self.collision_handler.check_collision():
                self.is_running = False
            if self.collision_handler.food_collision(self.food):
                self.snake.append_part()
                self.food = self.food_generator.generate_food()
                self.food_generated = True
                self.scoreboard.update_score()
            if not self.food_generated:
                self.food_generator.free_spots[self.snake.tail.y][self.snake.tail.x] = True
            self.snake.move()
            self.food_generator.free_spots[self.snake.head.y][self.snake.head.x] = False
            self.food_generated = False
            self.event_handler.handle_events()
            self.update_screen()
        self.scoreboard.save_score()

    def update_screen(self):
        pygame.draw.rect(self.screen, "#5B84B1FF", (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
        for j in range(BOARD_HEIGHT):
            for i in range(BOARD_WIDTH):
                xi = i * PART_WIDTH + OFFSET_X
                yi = j * PART_HEIGHT + OFFSET_Y
                pygame.draw.rect(self.screen, "#FC766AFF", (xi, yi, PART_WIDTH, PART_HEIGHT), 1)
        xf = self.food[0] * PART_WIDTH + OFFSET_X
        yf = self.food[1] * PART_HEIGHT + OFFSET_Y
        pygame.draw.circle(self.screen, "#FC766AFF", (xf + 16, yf + 16), 16)
        for part in self.snake.parts:
            part.draw(self.screen)
        font = pygame.font.SysFont(None, 23)
        txt = font.render("Current score - " + str(self.scoreboard.current), False, BLACK)
        txt2 = font.render("Best score - " + str(self.scoreboard.best), False, BLACK)
        self.screen.blit(txt, (200, 697))
        self.screen.blit(txt2, (400, 697))
        pygame.display.update()


if __name__ == '__main__':
    snk_game = SnakeGame()
    snk_game.run()
