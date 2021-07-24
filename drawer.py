from setup import *


def draw_snake(snake):
    window.fill(BLACK)
    for i in range(len(snake.parts) - 1, 0, -1):
        pygame.draw.line(window, WHITE, (snake.parts[i].x * PART_WIDTH, snake.parts[i].y * PART_HEIGHT),
                         (snake.parts[i - 1].x * PART_WIDTH - snake.parts[i].direction[0] // VELOCITY,
                          snake.parts[i - 1].y * PART_HEIGHT - snake.parts[i].direction[1] // VELOCITY), 1)
    pygame.display.flip()
