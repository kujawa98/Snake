import pygame

DIRECTIONS = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}
BOARD_WIDTH = 17
BOARD_HEIGHT = 20

# screen setup
pygame.init()

# window properties
WINDOW_WIDTH, WINDOW_HEIGHT = 1024, 1024
INNER_WIDTH, INNER_HEIGHT = 544, 640
OFFSET_X = (WINDOW_WIDTH - INNER_WIDTH) // 2
OFFSET_Y = (WINDOW_HEIGHT - INNER_HEIGHT) // 2
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snek')

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# others
FPS = 60
PART_WIDTH, PART_HEIGHT = 32, 32
PARTS_ON_START = 3
APPLE = pygame.image.load("assets/apple.png")
