from setup import *
import pygame


def draw_snake(snake, food):
    window.fill("#FC766AFF")
    draw_chessboard()
    pygame.draw.rect(window, "#FC766AFF",
                     (food[0] * PART_WIDTH,
                      food[1] * PART_HEIGHT, PART_WIDTH, PART_HEIGHT), 0, 16)
    for part in snake.parts:
        color = "#FC766AFF" if part == snake.head else (150, 150, 150)
        pygame.draw.rect(window, color,
                         (part.x * PART_WIDTH, part.y * PART_HEIGHT, PART_WIDTH, PART_HEIGHT))


def draw_chessboard():
    for i in range(BOARD_WIDTH):
        for j in range(BOARD_HEIGHT):
            pygame.draw.rect(window, "#5B84B1FF",
                             (i * PART_WIDTH, j * PART_HEIGHT, PART_WIDTH, PART_HEIGHT))
            pygame.draw.rect(window, "#FC766AFF",
                             (i * PART_WIDTH, j * PART_HEIGHT, PART_WIDTH, PART_HEIGHT), 1, 25)
