from setup import *
import pygame


def draw_snake(snake, food):
    window.fill(BLACK)
    pygame.draw.line(window, WHITE, [OFFSET_X, OFFSET_Y], [OFFSET_X, OFFSET_Y + INNER_HEIGHT])
    pygame.draw.line(window, WHITE, [OFFSET_X + INNER_WIDTH, OFFSET_Y],
                     [OFFSET_X + INNER_WIDTH, OFFSET_Y + INNER_HEIGHT])
    pygame.draw.line(window, WHITE, [OFFSET_X, OFFSET_Y + INNER_HEIGHT],
                     [OFFSET_X + INNER_WIDTH, OFFSET_Y + INNER_HEIGHT])
    pygame.draw.line(window, WHITE, [OFFSET_X, OFFSET_Y],
                     [OFFSET_X + INNER_WIDTH, OFFSET_Y])
    for part in snake.parts:
        pygame.draw.rect(window, WHITE,
                         (part.x * PART_WIDTH + OFFSET_X, part.y * PART_HEIGHT+OFFSET_Y, PART_WIDTH, PART_HEIGHT))
    draw_food(food)


def draw_food(food):
    pygame.draw.rect(window, LIMON,
                     (food[0] * PART_WIDTH + OFFSET_X, food[1] * PART_HEIGHT+OFFSET_Y, PART_WIDTH, PART_HEIGHT))
