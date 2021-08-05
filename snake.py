import pygame
from setup import *

from collections import deque


class Part:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.is_fixed = True


class Snake:
    def __init__(self):
        self.parts = [Part(BOARD_WIDTH // 2, j, WHITE) for j in
                      range(BOARD_WIDTH // 2, BOARD_WIDTH // 2 + PARTS_ON_START)]
        self.head = self.parts[0]
        self.head.is_fixed = False
        self.tail = self.parts[-1]
        self.direction = DIRECTIONS["up"]
        self.next_directions = deque()
        self.it_down = 0
        self.it_up = 32
        self.it_right = 0
        self.it_left = 32

    def change_direction(self, new_direction):
        self.next_directions.append(new_direction)

    def move(self):
        if self.direction == DIRECTIONS['down']:
            if self.it_down == 32:
                self.it_down = 0
                self.mov()
            else:
                self.it_down += 1
        elif self.direction == DIRECTIONS['up']:
            if self.it_up == 0:
                self.it_up = 32
                self.mov()
            else:
                self.it_up -= 1
        elif self.direction == DIRECTIONS['right']:
            if self.it_right == 32:
                self.it_right = 0
                self.mov()
            else:
                self.it_right += 1
        elif self.direction == DIRECTIONS['left']:
            if self.it_left == 0:
                self.it_left = 32
                self.mov()
            else:
                self.it_left -= 1

    def mov(self):
        for i in range(len(self.parts) - 1, 0, -1):
            self.parts[i].x = self.parts[i - 1].x
            self.parts[i].y = self.parts[i - 1].y
        if self.next_directions and float(self.head.x).is_integer() and float(self.head.y).is_integer():
            self.direction = self.next_directions.popleft()
        self.head.x += self.direction[0]
        self.head.y += self.direction[1]

    def draw(self, window):
        for part in self.parts:
            x = part.x * PART_WIDTH + OFFSET_X
            y = part.y * PART_HEIGHT + OFFSET_Y
            width = PART_WIDTH
            height = PART_HEIGHT
            if part.is_fixed:
                pass
            elif self.direction == DIRECTIONS['up']:
                y += self.it_up
            elif self.direction == DIRECTIONS['down']:
                height = self.it_down
            elif self.direction == DIRECTIONS['right']:
                width = self.it_right
            elif self.direction == DIRECTIONS['left']:
                x += self.it_left
            pygame.draw.rect(window, part.color, (x, y, width, height))

    def append_part(self):
        xi = self.tail.x
        yi = self.tail.y
        self.parts.append(Part(xi, yi, WHITE))
        self.tail = self.parts[-1]
