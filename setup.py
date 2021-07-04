import pygame

DIRECTIONS = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}
BOARD_WIDTH = BOARD_HEIGHT = 17

# screen setup
pygame.init()

# window properties
WINDOW_WIDTH, WINDOW_HEIGHT = 340, 340
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snek')

# colors
BLUE = (65, 105, 225)
WHITE = (255, 255, 255)
LIMON = (147, 246, 0)
BLACK = (0, 0, 0)

# others
FPS = 60
PART_WIDTH, PART_HEIGHT = 20, 20
