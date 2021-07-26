from setup import *


def draw_snake(snake):
    window.fill(BLACK)
    for i in range(len(snake.parts) - 1, 0, -1):
        if snake.parts[i - 1] != snake.head:
            x_pocz = snake.parts[i].x * PART_WIDTH + 1 if snake.parts[i].x < snake.parts[i - 1].x else snake.parts[
                                                                                                           i].x * PART_WIDTH
            y_pocz = snake.parts[i].y * PART_HEIGHT + 1 if snake.parts[i].y < snake.parts[i - 1].y else snake.parts[
                                                                                                            i].y * PART_HEIGHT
            x_konc = snake.parts[i - 1].x * PART_WIDTH
            y_konc = snake.parts[i - 1].y * PART_HEIGHT
            if snake.parts[i].x == snake.parts[i - 1].x:
                y_konc = snake.parts[i - 1].y * PART_WIDTH + 10 if snake.parts[i].y < snake.parts[i - 1].y else \
                    snake.parts[
                        i - 1].y * PART_WIDTH - 9
            if snake.parts[i].y == snake.parts[i - 1].y:
                x_konc = snake.parts[i - 1].x * PART_WIDTH + 10 if snake.parts[i].x < snake.parts[i - 1].x else \
                    snake.parts[
                        i - 1].x * PART_WIDTH - 9
            pygame.draw.line(window, WHITE, (x_pocz, y_pocz),
                             (x_konc,
                              y_konc),
                             20)
        else:
            x_pocz = snake.parts[i].x * PART_WIDTH + 1 if snake.parts[i].x > snake.parts[i - 1].x else snake.parts[
                                                                                                           i].x * PART_WIDTH
            x_konc = snake.parts[i - 1].x * PART_WIDTH + 1 if snake.parts[i].x > snake.parts[i - 1].x else snake.parts[
                                                                                                               i - 1].x * PART_WIDTH
            y_pocz = snake.parts[i].y * PART_HEIGHT + 1 if snake.parts[i].y > snake.parts[i - 1].y else snake.parts[
                                                                                                            i].y * PART_HEIGHT
            y_konc = snake.parts[i - 1].y * PART_HEIGHT + 1 if snake.parts[i].y > snake.parts[i - 1].y else snake.parts[
                                                                                                                i - 1].y * PART_HEIGHT

            pygame.draw.line(window, WHITE, (x_pocz, y_pocz),
                             (x_konc,
                              y_konc),
                             20)
    pygame.display.flip()
