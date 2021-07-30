from random import choice
from setup import BOARD_WIDTH, BOARD_HEIGHT


class Food:
    def __init__(self, snk):
        self.free_spots = [[True for i in range(BOARD_WIDTH)] for j in range(BOARD_HEIGHT)]
        self.fr_spots(snk)

    def fr_spots(self, snk):
        for part in snk.parts:
            self.free_spots[part.y][part.x] = False

    def resolve_spots(self, snk):
        self.free_spots[snk.head.y][snk.head.x] = False
        self.free_spots[snk.tail.y][snk.tail.x] = True

    def generate_food(self):
        free_spots = []
        for j in range(1, BOARD_HEIGHT - 1):
            for i in range(1, BOARD_WIDTH - 1):
                if self.free_spots[j][i]:
                    free_spots.append((i, j))
        return choice(free_spots)
