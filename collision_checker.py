from setup import BOARD_WIDTH, BOARD_HEIGHT


def check_collision(snake):
    if snake.head.x + snake.direction[0] < 0 or snake.head.x + snake.direction[0] >= BOARD_WIDTH or snake.head.y + \
            snake.direction[1] < 0 or snake.head.y + snake.direction[1] >= BOARD_HEIGHT:
        return True
    for part in snake.parts:
        if part != snake.head and part.x == snake.head.x and part.y == snake.head.y:
            return True
    return False


def food_collision(snake, food):
    if snake.head.x + snake.direction[0] == food[0] and snake.head.y + snake.direction[1] == food[1]:
        return True
    return False
