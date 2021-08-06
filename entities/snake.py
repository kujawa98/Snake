import pygame

from entities.anchor_point import AnchorPoint
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
        self.tail = self.parts[-1]
        self.direction = DIRECTIONS["up"]
        self.tail_direction = DIRECTIONS["up"]
        self.next_directions = deque()
        self.anchor_points = deque()

        self.it = 0

    def change_direction(self, new_direction):
        self.next_directions.append(new_direction)

    def move(self):
        if self.it == 32:
            self.it = 0
            for i in range(len(self.parts) - 1, 0, -1):
                self.parts[i].x = self.parts[i - 1].x
                self.parts[i].y = self.parts[i - 1].y
            if self.anchor_points and self.tail.x == self.anchor_points[0].x and self.tail.y == self.anchor_points[0].y:
                self.tail_direction = self.anchor_points.popleft().direction
            if self.next_directions and float(self.head.x).is_integer() and float(self.head.y).is_integer():
                self.direction = self.next_directions.popleft()
                self.anchor_points.append(AnchorPoint(self.head.x, self.head.y, self.direction))
            self.head.x += self.direction[0]
            self.head.y += self.direction[1]
        else:
            self.it += 1

    def draw(self, window):
        for part in self.parts:
            x = part.x * PART_WIDTH + OFFSET_X
            y = part.y * PART_HEIGHT + OFFSET_Y
            if part == self.head:
                off = self.it - 32
                if self.direction == DIRECTIONS['up']:
                    y -= off
                elif self.direction == DIRECTIONS['down']:
                    y += off
                elif self.direction == DIRECTIONS['right']:
                    x += off
                elif self.direction == DIRECTIONS['left']:
                    x -= off
            if part == self.tail:
                off = self.it
                if self.tail_direction == DIRECTIONS['up']:
                    y -= off
                elif self.tail_direction == DIRECTIONS['down']:
                    y += off
                elif self.tail_direction == DIRECTIONS['right']:
                    x += off
                elif self.tail_direction == DIRECTIONS['left']:
                    x -= off
            pygame.draw.rect(window, part.color, (x, y, PART_WIDTH, PART_HEIGHT))

    def append_part(self):
        xi = self.tail.x
        yi = self.tail.y
        self.parts.append(Part(xi, yi, WHITE))
        self.tail = self.parts[-1]
