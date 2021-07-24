from random import choice
from setup import BOARD_WIDTH, BOARD_HEIGHT


class Food:
    def __init__(self, snk):
        self.free_spots = [[i, j, True] for i in range(1, BOARD_WIDTH) for j in range(1, BOARD_HEIGHT)]
        self.fr_spots(snk)

    def fr_spots(self, snk):
        for part in snk.parts:
            self.free_spots[BOARD_WIDTH * part.x - 1 + part.y - 1][2] = False

    def resolve_spots(self, snk):
        index = BOARD_WIDTH * snk.head.x + snk.head.y
        if index < BOARD_WIDTH * BOARD_HEIGHT:
            self.free_spots[BOARD_WIDTH * snk.head.x + snk.head.y][2] = False
            self.free_spots[BOARD_WIDTH * snk.tail.x + snk.tail.y][2] = True

    def generate_food(self):
        filtered = filter(lambda x: x[2] == True, self.free_spots)
        return choice(list(filtered))
