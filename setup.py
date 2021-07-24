import pygame

VELOCITY = 0.5  # must be given by formula 2^(-n) for natural n
DIRECTIONS = {"up": (0, -VELOCITY), "down": (0, VELOCITY), "left": (-VELOCITY, 0), "right": (VELOCITY, 0)}
BOARD_WIDTH = 17
BOARD_HEIGHT = 20

# screen setup
pygame.init()

# window properties
WINDOW_WIDTH, WINDOW_HEIGHT = 340, 400
INNER_WIDTH, INNER_HEIGHT = 544, 640
OFFSET_X = (WINDOW_WIDTH - INNER_WIDTH) // 2
OFFSET_Y = (WINDOW_HEIGHT - INNER_HEIGHT) // 2
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snek')

# colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# others
FPS = 60
PART_WIDTH, PART_HEIGHT = 20, 20
PARTS_ON_START = 3
