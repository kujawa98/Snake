from setup import *
import pygame


def draw_snake(snake):
    window.fill(BLACK)
    for part in snake.parts:
        pygame.draw.rect(window, WHITE, (part.x * PART_WIDTH, part.y * PART_HEIGHT, PART_WIDTH, PART_HEIGHT))
