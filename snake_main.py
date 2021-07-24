import pygame
from random import choice

from setup import *
from collision_checker import *

from event_handler import EventHandler
from snake import Snake


def fspots(snk):
    free_spots = [[i, j, True] for i in range(1, BOARD_WIDTH) for j in range(1, BOARD_HEIGHT)]
    for part in snk.parts:
        free_spots[BOARD_WIDTH * part.x - 1 + part.y - 1][2] = False
    return free_spots


def resolve_spots(snk, free_spots):
    index = BOARD_WIDTH * snk.head.x + snk.head.y
    if index < BOARD_WIDTH * BOARD_HEIGHT:
        free_spots[BOARD_WIDTH * snk.head.x + snk.head.y][2] = False
        free_spots[BOARD_WIDTH * snk.tail.x + snk.tail.y][2] = True


def generate_food(free_spots):
    filtered = filter(lambda x: x[2] == True, free_spots)
    return choice(list(filtered))


class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Pinky')
        self.snake = Snake()

        self.clock = pygame.time.Clock()
        self.event_handler = EventHandler(self)

        self.is_running = True

    def run(self):
        free_spots = fspots(self.snake)
        food = generate_food(free_spots)
        while self.is_running:
            self.clock.tick(10)
            if food_collision(self.snake, food):
                self.snake.append_part()
                food = generate_food(free_spots)
            if check_collision(self.snake):
                self.is_running = False
            self.snake.move()
            resolve_spots(self.snake, free_spots)
            self.event_handler.handle_events()
            self.update_screen(food)

    def update_screen(self, food):
        self.screen.fill("#FC766AFF")
        for i in range(BOARD_WIDTH):
            for j in range(BOARD_HEIGHT):
                pygame.draw.rect(self.screen, "#5B84B1FF",
                                 (i * PART_WIDTH, j * PART_HEIGHT, PART_WIDTH, PART_HEIGHT))
                pygame.draw.rect(self.screen, "#FC766AFF",
                                 (i * PART_WIDTH, j * PART_HEIGHT, PART_WIDTH, PART_HEIGHT), 1, 25)
        pygame.draw.rect(self.screen, "#FC766AFF",
                         (food[0] * PART_WIDTH,
                          food[1] * PART_HEIGHT, PART_WIDTH, PART_HEIGHT), 0, 16)
        for part in self.snake.parts:
            part.draw(self.screen)
        pygame.display.update()


if __name__ == '__main__':
    snk_game = SnakeGame()
    snk_game.run()
