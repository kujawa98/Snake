from setup import BOARD_WIDTH, BOARD_HEIGHT


class CollisionHandler:
    def __init__(self, snake):
        self.snake = snake

    def check_collision(self):
        x = self.snake.head.x
        y = self.snake.head.y
        if x < 0 or x >= BOARD_WIDTH or y < 0 or y >= BOARD_HEIGHT:
            return True
        for part in self.snake.parts:
            if part != self.snake.head and part.x == self.snake.head.x and part.y == self.snake.head.y:
                return True
        return False

    def food_collision(self, food):
        x = self.snake.head.x
        y = self.snake.head.y
        if x == food[0] and y == food[1]:
            return True
        return False
