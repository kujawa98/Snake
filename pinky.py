import pygame

from handlers.event_handler import EventHandler
from entities.snake import Snake
from entities.food import Food
from handlers.collision_handler import CollisionHandler
from scoreboard import Scoreboard
from window import Window

from setup import FPS

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.window = Window(self)

        self.snake = Snake()
        self.food = Food(self.snake)
        self.collision_handler = CollisionHandler(self.snake)
        self.event_handler = EventHandler(self)
        self.scoreboard = Scoreboard()

        self.clock = pygame.time.Clock()

        self.is_running = True
        self.food_sound = pygame.mixer.Sound('sounds/food.wav')
        self.collision_sound = pygame.mixer.Sound('sounds/collision.wav')

    def run(self):
        while self.is_running:
            self.clock.tick(FPS)
            if self.collision_handler.check_collision():
                self.collision_sound.play(2)
                pygame.time.delay(3 * 206)
                break
            if self.collision_handler.food_collision(self.food.location):
                self.food_sound.play()
                self.snake.append_part()
                self.food.generate_food()
                self.scoreboard.update_score()
            self.snake.move()
            self.event_handler.handle_events()
            self.window.update_window()
        self.scoreboard.save_score()


if __name__ == '__main__':
    snk_game = SnakeGame()
    snk_game.run()
