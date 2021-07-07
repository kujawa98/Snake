from setup import *
import pygame


def draw_snake(snake, food):
    window.fill(BLACK)
    window.blit(BGC, (0, 0))
    window.blit(IMG, (OFFSET_X, OFFSET_Y))
    window.blit(APPLE, (food[0] * PART_WIDTH + OFFSET_X,
                        food[1] * PART_HEIGHT + OFFSET_Y))
    for part in snake.parts:
        pygame.draw.rect(window, BLACK,
                         (part.x * PART_WIDTH + OFFSET_X, part.y * PART_HEIGHT + OFFSET_Y, PART_WIDTH, PART_HEIGHT))
