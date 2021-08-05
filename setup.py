VELOCITY = 1 / 32  # velocity is given by formula 2^(-n) for natural n
DIRECTIONS = {"up": (0, -VELOCITY), "down": (0, VELOCITY), "left": (-VELOCITY, 0), "right": (VELOCITY, 0)}
BOARD_WIDTH = 17
BOARD_HEIGHT = 20

# window properties
WINDOW_WIDTH, WINDOW_HEIGHT = 624, 720
INNER_WIDTH, INNER_HEIGHT = 544, 640
OFFSET_X = (WINDOW_WIDTH - INNER_WIDTH) // 2
OFFSET_Y = (WINDOW_HEIGHT - INNER_HEIGHT) // 2

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# others
FPS = 60
PART_WIDTH, PART_HEIGHT = 32, 32
PARTS_ON_START = 3
