from copy import copy

from setup import *
from anchor_point import AnchorPoint


class Snake:
    def __init__(self):
        self.parts = [AnchorPoint(BOARD_WIDTH // 2, BOARD_WIDTH // 2, DIRECTIONS['up']),
                      AnchorPoint(BOARD_WIDTH // 2, BOARD_WIDTH // 2 + 3, DIRECTIONS['up'])]
        self.head = self.parts[0]
        self.tail = self.parts[-1]
        self.direction_changed = False

    def change_direction(self, new_direction):
        self.head.direction = new_direction
        self.direction_changed = True

    def move(self):
        if self.direction_changed:
            self.append_anchor_point()
            self.direction_changed = False
        self.head.update()
        self.tail.update()
        if self.tail == self.parts[-2]:
            self.tail = self.parts[-2]
            self.parts.pop()

    def append_anchor_point(self):
        self.parts.insert(1, copy(self.head))
