def check_collision(snake):
    if snake.head.x < 0 or snake.head.x >= 17 or snake.head.y < 0 or snake.head.y >= 17:
        return True
    for part in snake.parts:
        if part != snake.head and part.x == snake.head.x and part.y == snake.head.y:
            return True
    return False
