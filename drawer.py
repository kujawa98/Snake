from setup import *


def draw_snake(snake):
    window.fill(BLACK)
    for i in range(len(snake.parts) - 1, 0, -1):
        if snake.parts[i].direction != snake.parts[i - 1].direction:
            pygame.draw.line(window, WHITE, (snake.parts[i].x * PART_WIDTH, snake.parts[i].y * PART_HEIGHT),
                             (snake.parts[i - 1].x * PART_WIDTH + snake.parts[i].direction[0] // VELOCITY * (
                                     PART_WIDTH // 2 - 1),
                              snake.parts[i - 1].y * PART_HEIGHT + snake.parts[i].direction[1] // VELOCITY * (
                                      PART_HEIGHT // 2 - 1)),
                             PART_WIDTH)
        else:
            pygame.draw.line(window, WHITE, (snake.parts[i].x * PART_WIDTH, snake.parts[i].y * PART_HEIGHT),
                             (snake.parts[i - 1].x * PART_WIDTH - snake.parts[i].direction[0] // VELOCITY,
                              snake.parts[i - 1].y * PART_HEIGHT - snake.parts[i].direction[1] // VELOCITY), PART_WIDTH)
    pygame.display.flip()
