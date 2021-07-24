from event_handler import EventHandler
from snake import Snake
from setup import *
from drawer import draw_snake
from collision_checker import *
from food_generator import generate_food


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


class SnakeGame:
    def __init__(self):
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
            draw_snake(self.snake, food)
            self.event_handler.handle_events()
            pygame.display.update()


if __name__ == '__main__':
    snk_game = SnakeGame()
    snk_game.run()
