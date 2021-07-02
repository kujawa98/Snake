from setup import DIRECTIONS


class Part:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake:
    def __init__(self):
        self.parts = [Part(4, j) for j in range(4, 7)]
        self.head = self.parts[0]
        self.direction = DIRECTIONS["up"]

    def move(self):
        for i in range(len(self.parts) - 1, 0, -1):
            self.parts[i].x = self.parts[i - 1].x
            self.parts[i].y = self.parts[i - 1].y
        self.head.x += self.direction[0]
        self.head.y += self.direction[1]

    def print(self):
        for part in self.parts:
            print(part.x)


sn = Snake()
sn.move()
sn.move()
sn.print()
