import pygame

from event_handler import EventHandler
from snake import Snake
from food import FoodGenerator
from collision_handler import CollisionHandler
from scoreboard import Scoreboard
from window import Window


class SnakeGame:
    def __init__(self):
        pygame.init()
        self.window = Window(self)

        self.snake = Snake()
        self.food_generator = FoodGenerator(self.snake)
        self.collision_handler = CollisionHandler(self.snake)
        self.event_handler = EventHandler(self)
        self.scoreboard = Scoreboard()

        self.clock = pygame.time.Clock()

        self.food = self.food_generator.generate_food()

        self.is_running = True
        self.food_generated = False
        self.food_sound = pygame.mixer.Sound('sounds/food.wav')
        self.collision_sound = pygame.mixer.Sound('sounds/collision.wav')

    def run(self):
        while self.is_running:
            self.clock.tick(10)
            if self.collision_handler.check_collision():
                self.collision_sound.play(2)
                pygame.time.delay(3 * 206)
                break
            if self.collision_handler.food_collision(self.food):
                self.food_sound.play()
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
            self.window.update_screen()
        self.scoreboard.save_score()


if __name__ == '__main__':
    snk_game = SnakeGame()
    snk_game.run()
