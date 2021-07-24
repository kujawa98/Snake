from setup import BOARD_WIDTH, BOARD_HEIGHT


class CollisionHandler:
    def __init__(self, snake):
        self.snake = snake

    def check_collision(self):
        if self.snake.head.x + self.snake.direction[0] < 0 or self.snake.head.x + self.snake.direction[
            0] >= BOARD_WIDTH or self.snake.head.y + \
                self.snake.direction[1] < 0 or self.snake.head.y + self.snake.direction[1] >= BOARD_HEIGHT:
            return True
        for part in self.snake.parts:
            if part != self.snake.head and part.x == self.snake.head.x and part.y == self.snake.head.y:
                return True
        return False

    def food_collision(self, food):
        if self.snake.head.x + self.snake.direction[0] == food[0] and self.snake.head.y + self.snake.direction[1] == \
                food[1]:
            return True
        return False
