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

    def change_direction(self, new_direction):
        self.direction = new_direction

    def move(self):
        for i in range(len(self.parts) - 1, 0, -1):
            self.parts[i].x = self.parts[i - 1].x
            self.parts[i].y = self.parts[i - 1].y
        self.head.x += self.direction[0]
        self.head.y += self.direction[1]

    def append_part(self):
        xi = self.parts[len(self.parts) - 1].x
        yi = self.parts[len(self.parts) - 1].y
        self.parts.append(Part(xi, yi))

# TODO: sprawdzić, czy na następnym polu jakie będzie jest jedzenie, jeśli tak - append_part i move, inaczej razie tylko move
