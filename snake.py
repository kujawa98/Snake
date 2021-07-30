import pygame
from setup import *


class Part:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.rect = pygame.Rect(self.x * PART_WIDTH, self.y * PART_HEIGHT, PART_WIDTH, PART_HEIGHT)

    def draw(self, window):
        pygame.draw.rect(window, self.color,
                         (self.x * PART_WIDTH + OFFSET_X, self.y * PART_HEIGHT + OFFSET_Y, PART_WIDTH, PART_HEIGHT))


class Snake:
    def __init__(self):
        self.parts = [Part(BOARD_WIDTH // 2, j, WHITE) for j in
                      range(BOARD_WIDTH // 2, BOARD_WIDTH // 2 + PARTS_ON_START)]
        self.head = self.parts[0]
        self.tail = self.parts[len(self.parts) - 1]
        self.direction = DIRECTIONS["up"]

    def change_direction(self, new_direction):
        self.direction = new_direction

    def move(self):
        for i in range(len(self.parts) - 1, 0, -1):
            self.parts[i].x = self.parts[i - 1].x
            self.parts[i].y = self.parts[i - 1].y
        self.head.x += self.direction[0]
        self.head.y += self.direction[1]

    def append_part(self):
        xi = self.parts[len(self.parts) - 1].x
        yi = self.parts[len(self.parts) - 1].y
        self.parts.append(Part(xi, yi, WHITE))
        self.tail = self.parts[len(self.parts) - 1]
