from setup import *
import pygame


def draw_snake(snake, food):
    window.fill(BLACK)
    for part in snake.parts:
        pygame.draw.rect(window, WHITE, (part.x * PART_WIDTH, part.y * PART_HEIGHT, PART_WIDTH, PART_HEIGHT))
    draw_food(food)


def draw_food(food):
    pygame.draw.rect(window, LIMON, (food[0] * PART_WIDTH, food[1] * PART_HEIGHT, PART_WIDTH, PART_HEIGHT))
